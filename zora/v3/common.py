from zora.v3.queries import (
    QUERY_COLLECTIONS,
    QUERY_EVENTS,
    QUERY_SALES,
    QUERY_TOKENS,
    QUERY_MARKETS,
)
from zora.v3.utils import (
    build_filter,
    run_zora_query,
    build_network,
    build_pagination,
    build_query,
    build_sorting,
)

import pandas as pd


def _generate_query(
    query_type: str,
    pagination_limit: int = None,
    pagination_offset: int = None,
    sort_key: str = None,
    sort_direction: str = None,
    query_collection: str = None,
    query_owner: str = None,
    filter_event: str = None,
):
    # join query params
    params = []
    params.append(build_network())

    if pagination_limit or pagination_offset is not None:
        params.append(build_pagination(pagination_limit, pagination_offset))

    if sort_key or sort_direction is not None:
        params.append(build_sorting(sort_key, sort_direction))

    if query_collection or query_owner is not None:
        params.append(build_query(query_collection, query_owner))

    if filter_event is not None:
        params.append(build_filter(filter_event))

    params = ", ".join(params)
    rsql_query = query_type.replace("$params", params)

    result = run_zora_query(rsql_query)
    if result["data"] is None and "errors" in result:
        raise Exception(f"Errors found in query: {result['errors'][0]['message']}")

    return result["data"]


def query_tokens(
    pagination_limit: int = None,
    pagination_offset: int = 0,
    sort_key: str = None,
    sort_direction: str = None,
    query_collection: str = None,
    query_owner: str = None,
):

    return pd.DataFrame(_generate_query(QUERY_TOKENS, **locals())["tokens"]["nodes"])


def query_sales(
    pagination_limit: int = None,
    pagination_offset: int = 0,
    sort_key: str = None,
    sort_direction: str = None,
    query_collection: str = None,
    query_owner: str = None,
):
    return pd.DataFrame(_generate_query(QUERY_SALES, **locals())["sales"]["nodes"])


def query_collections(
    pagination_limit: int = None,
    pagination_offset: int = 0,
    sort_key: str = None,
    sort_direction: str = None,
    query_collection: str = None,
    query_owner: str = None,
):
    return pd.DataFrame(
        _generate_query(QUERY_COLLECTIONS, **locals())["collections"]["nodes"]
    )
