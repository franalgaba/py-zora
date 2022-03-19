# **ZORA Protocol Python SDK**

This repository contains a tool for interacting with NFT metadata using ZORA Protocol in a decentralized and permissionless way. The aim of this tool is to ease exploration and analysis of on-chain data for Ethereum NFTs without the need of centralized entity or API limitations.

* **Get all tracked NFT collections** in Ethereum.
* **Get NFT Collection information**.
* **Get all token and its metadata** from a given NFT Collection.
* **Get transactions and activity** from any NFT collection.

**ZORA V3 Community API** inital integration for `collections`, `tokens` and `sales`. For every supported entity there is filtering based on `pagination`, `query`, `sort` and `filter`. See [reference](#zora-v3-community-api-usage) for installation and usage details.

## **Installation**

`pip install zora`

## **Usage**

### List all NFT collections

```python
from zora import list_nft

all_collections = list_nft()
for collection in all_collections:
    if "Cool Cat" in collection.name:
        cool_cats = collection
        address = collection.address
        break

print(collection)
```

### Get NFT collection

```python
from zora import NFT

address = "0x1A92f7381B9F03921564a437210bB9396471050C" # Cool Cats

nft = NFT(address)
print(nft)
```

### Get all items from NFT Collection

```python
from zora import NFT

address = "0x1A92f7381B9F03921564a437210bB9396471050C" # Cool Cats

nft = NFT(address)

# It returns a list of objects of type Token with metadata
items = nft.get_items()
# Printing the object gives a pretty representation of the token
print(items[0])
```

### Get all attributes from items in NFT Collection

```python
from zora import NFT

address = "0x1A92f7381B9F03921564a437210bB9396471050C" # Cool Cats

nft = NFT(address)

# Get all attribute information from items in collection
metadata = nft.get_metadata()
print(metadata[0])
```

### Get all transactions and volume from NFT Collection

```python
from zora import NFT

address = "0x1A92f7381B9F03921564a437210bB9396471050C" # Cool Cats

nft = NFT(address)

items = nft.get_items()
# Retrieve all the transactions hashes of this collection activity
transfers = nft.get_transfers()
print(transfers[0])

# Get all the traded volume by a single collection in ETH
volume = nft.get_volume(transfers)
print(volume)
```

## **ZORA V3 Community API Usage**

The usage of the Community API integration has support for the main entities implemented by ZORA Protocol in their [API documentation](https://ourzora.notion.site/Zora-Community-API-Testing-e68aae68838c4b878d7b1dab4e6e697b)

### **Installation**

`pip install zora`

### **Usage**

#### Query Collections Entity

Using the `collections` entity you can retrieve information about supported NFT collections.

```python
from zora import query_collections

# Response returns a DataFrame
collections_df = query_collections(pagination_limit=2, sort_key="CREATED", sort_direction="ASC")
```

#### Query Tokens

Using the `tokens` entity you can retrieve information about tokens in a certain `collection`.

```python
from zora import query_tokens

# Response returns a DataFrame
tokens_df = query_tokens(pagination_limit=5, sort_key="MINTED", sort_direction="ASC")
```

#### Query Sales

Using the `sales` entity you cand retrieve all the sale information about a specific `collection`.

```python
from zora import query_sales

# Response returns a DataFrame
sales_df = query_sales(pagination_limit=10, sort_key="ETH_PRICE", sort_direction="ASC", query_collection="0xabefbc9fd2f806065b4f3c237d4b59d9a97bcac7")
```
