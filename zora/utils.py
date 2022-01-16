import requests


def run_zora_query(query, variables=None):
    endpoint = "https://indexer-prod-mainnet.ZORA.co/v1/graphql"

    body = {"query": query}

    if variables is not None:
        body["variables"] = variables

    response = requests.post(
        endpoint, json=body, headers={"X-Hasura-Role": "anonymous"}
    )
    return response.json()
