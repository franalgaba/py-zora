import asyncio
import aiohttp

from zora.indexer.utils import run_zora_query
from zora.indexer.queries import (
    TOKEN_QUERY,
    CONTRACT_QUERY,
    METADATA_QUERY,
    TOKEN_TRANSFERS_QUERY,
    TRANSACTION_QUERY,
)
from zora.indexer.base import BaseToken


class NFT(BaseToken):

    """
    Class for NFT interaction from Zora
    """

    def __init__(self, address) -> None:

        """
        Initialize NFT Contract class from metadata

        Args:
            address (str): NFT contract address
        """

        response = self._get_contract(address)
        response = response["data"]["TokenContract"][0]
        # Dynamic attribute generation based on ZORA response
        for k, v in response.items():
            setattr(self, k, v)

    def _get_contract(self, address):

        """
        Get NFT Contract metadata from ZORA

        Args:
            address (str): NFT contract address

        Returns:
            dict: dict with response from ZORA
        """
        variables = {"address": address}
        return run_zora_query(CONTRACT_QUERY, variables)

    def get_items(self):

        """
        Get all NFT collection items and metadata

        Returns:
            List[Token]: list of Token objects with items metadata
        """

        variables = {"address": self.address}
        response = run_zora_query(TOKEN_QUERY, variables)
        result = []
        for token in response["data"]["Token"]:
            result.append(Token(token))
        return result

    def get_metadata(self):

        """
        Get all metadata from items in NFT Collection

        Returns:
            List[Metadata]: list of Metadata objects
        """
        variables = {"address": self.address}
        response = run_zora_query(METADATA_QUERY, variables)
        result = []
        for token in response["data"]["TokenMetadata"]:
            result.append(Meatadata(token))
        return result

    def get_transfers(self):

        """
        Get all NFT Collection transactions

        Returns:
            List[str]: list with transaction hashes from collection
        """

        variables = {"address": self.address}
        response = run_zora_query(TOKEN_TRANSFERS_QUERY, variables)

        result = []
        for tx in response["data"]["Token"]:
            for tx_id in tx["transferEvents"]:
                result.append(tx_id["id"].split("-")[0])
        return result

    async def _get_transaction(self, transactions):

        """
        Get all transaction information from ZORA
        """

        async def get_tx(session, query, variables=None):

            """
            Get transaction information given transaction hash

            Returns:
                dict: response from ZORA request
            """

            body = {"query": query}
            if variables is not None:
                body["variables"] = variables

            async with session.post(
                "https://indexer-prod-mainnet.ZORA.co/v1/graphql",
                json=body,
                headers={"X-Hasura-Role": "anonymous"},
            ) as resp:
                response = await resp.json()
                return response

        volume = 0

        async with aiohttp.ClientSession() as session:
            tasks = []
            for tx in transactions:
                variables = {"hash": tx}
                tasks.append(
                    asyncio.ensure_future(get_tx(session, TRANSACTION_QUERY, variables))
                )

            processed_list = await asyncio.gather(*tasks)
            for response in processed_list:
                response = response["data"]["Transaction"][0]
                volume += float(response["value"]) / (10 ** 18)

        return volume

    def get_volume(self, transactions=None):

        """
        Calculate transfered ETH volume from the collection

        Args:
            transactions (List[str], optional): List of transactions. Defaults to None.

        Returns:
            float: ETH transferred volume
        """

        volume = 0

        if not transactions:
            transactions = self.get_transfers()

        volume = asyncio.run(self._get_transaction(transactions))
        volume = float("{:.4f}".format(volume))
        return volume


class Meatadata(BaseToken):

    """
    Class for Token metadata
    """

    def __init__(self, token):
        for k, v in token.items():
            setattr(self, k, v)


class Token(BaseToken):

    """
    Class for Token information
    """

    def __init__(self, token):
        for k, v in token.items():
            setattr(self, k, v)
