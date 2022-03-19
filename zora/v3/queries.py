QUERY_COLLECTIONS = """
query QueryCollections {
  collections($params) {
    nodes {
      address
      name
      symbol
    }
  }
}
"""

QUERY_TOKENS = """
query QueryTokens {
  tokens($params) {
    nodes {
      tokenId
      collectionAddress
      name
    }
  }
}
"""

QUERY_EVENTS = """
query QueryEvents {
  events($params) {
      collectionAddress
    }
}
"""

QUERY_MARKETS = """
query QueryMarkets {
  markets($params) {
      collectionAddress
      marketType
      status
    }
}
"""


QUERY_SALES = """
query QuerySales {
  sales($params) {
    nodes {
      collectionAddress
      saleType
      sellerAddress
      buyerAddress
      tokenId
      price {
        ethPrice {
          decimal
          currency {
            name
            decimals
            address
          }
          raw
        }
        nativePrice {
          decimal
          raw
          currency {
            address
            decimals
            name
          }
        }
        usdcPrice {
          currency {
            address
            decimals
            name
          }
          raw
          decimal
        }
      }
    }
  }
}
"""
