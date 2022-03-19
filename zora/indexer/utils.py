import requests

from zora.core.constants import INDEXER_ENDPOINT


def run_zora_query(query, variables=None):

    """
    Execute query in ZORA

    Returns:
        dict: json response from ZORA
    """

    body = {"query": query}

    if variables is not None:
        body["variables"] = variables

    response = requests.post(
        INDEXER_ENDPOINT, json=body, headers={"X-Hasura-Role": "anonymous"}
    )
    return response.json()
