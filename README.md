# **ZORA Protocol Python SDK**

This repository contains a tool for interacting with NFT metadata using ZORA Protocol in a decentralized and permissionless way. The aim of this tool is to ease exploration and analysis of on-chain data for Ethereum NFTs without the need of centralized entity or API limitations.

* Get all tracked NFT collections in Ethereum.
* Get NFT Collection information
* Get all token and its metadata from a given NFT Collection.
* Get transactions and activity from any NFT collection.

## **Installation**

`pip install zora`

## **Usage**

### **List all NFT collections**

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

