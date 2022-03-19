TOKEN_QUERY = """
        query GetTokens($address: String) {
            Token(
                where: { address: { _eq: $address } },
                order_by: { tokenId: asc }
            ) {
                tokenId
                address
                minter
                owner
                metadata {
                json
                }
            }
        }
        """

TOKEN_TRANSFERS_QUERY = """
        query GetTransferTokens($address: String) {
            Token(
                where: { address: { _eq: $address } },
                order_by: { tokenId: asc }
            ) {
                transferEvents { id }
            }
        }
        """

CONTRACT_QUERY = """
query GetContract($address: String) {
        TokenContract(
            where: { address: { _eq: $address } }
        ) {
            address
            name
            supportsMetadata
            symbol
        }
    }
"""

LIST_NFT_QUERY = """
    {
        TokenContract {
        address
        name
        supportsMetadata
        symbol
        }
    }
"""

METADATA_QUERY = """
query GetMetadata($address: String) {
        TokenMetadata(
            where: { address: { _eq: $address } }
        ) {
    address # Token address
    id # uuid, ignore
    json # data blob
    tokenId
    tokenURI
  }
}
"""

TRANSACTION_QUERY = """
query GetTransferTokens($hash: String) {
            Transaction(
                where: { hash: { _eq: $hash } }
    ) {
    # Fields
    blockHash
    blockNumber
    blockTimestamp
    failureReason
    from
    gas
    gasPrice
    hash
    input
    network
    nonce
    status
    to
    transactionIndex
    value

    # Relationships
    eventLogs {
      id
    }
    mediaMints {
      id
    } # see MediaMint table for context
  }
}
"""
