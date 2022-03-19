import requests

from zora.core.constants import V3_ENDPOINT


def build_network(network: str = "ETHEREUM", chain: str = "MAINNET"):

    return f"network: {{network: {network}, chain: {chain} }}"


def build_filter(event: str):

    allowed_filter_event = ["TRANSFER_EVENT"]

    if isinstance(event, str) and event not in allowed_filter_event:
        raise TypeError("Selected event order not allowed")

    params = []
    params.append(f"eventTypes: [{event}]")

    params = ", ".join(params)
    return "filter: {{ {} }}".format(params)


def build_sorting(key: str, direction: str):

    allowed_sorting = ["ASC", "DESC"]
    allowed_keys = ["ETH_PRICE", "CREATED", "MINTED"]

    if isinstance(key, str) and key not in allowed_keys:
        raise TypeError("Selected key order not allowed")

    if isinstance(direction, str) and direction not in allowed_sorting:
        raise TypeError("Selected direction order not allowed")

    params = []
    if key is not None:
        params.append(f"sortKey: {key}")
    if direction is not None:
        params.append(f"sortDirection: {direction}")

    params = ", ".join(params)
    return "sort: {{ {} }}".format(params)


def build_pagination(limit: int = None, offset: int = 0):

    params = []

    if limit is not None:
        params.append(f"limit: {limit}")
        if offset is not None:
            params.append(f"offset: {offset}")

    params = ", ".join(params)
    return "pagination: {{ {} }}".format(params)


def build_query(collection_address: str = None, owner_address: str = None):

    params = []
    if collection_address is not None:
        params.append(f'collectionAddresses: ["{collection_address}"]')

    if owner_address is not None:
        params.append(f'ownerAddresses: ["{owner_address}"]')

    params = ", ".join(params)
    return "query: {{ {} }}".format(params)


def run_zora_query(query, variables=None):

    """
    Execute query in ZORA

    Returns:
        dict: json response from ZORA
    """

    body = {"query": query}

    if variables is not None:
        body["variables"] = variables

    response = requests.post(V3_ENDPOINT, json=body)
    return response.json()
