import sys
import json
from iroha2 import Client
from iroha2.data_model.query.asset import FindAssetById
from iroha2.data_model.asset import Id

def query_asset_info(domain, account, asset):
    # Load the configuration from config.json
    with open("./config.json") as config_file:
        cfg = json.load(config_file)

    # Create an Iroha2 client
    cl = Client(cfg)

    # Create an asset ID based on the provided domain, account, and asset name
    asset_id = Id(f"{asset}#{domain}", f"{account}@{domain}")

    # Create a query to find the asset by the provided asset ID
    query = FindAssetById.id(asset_id)

    # Execute the query and return the result
    result = cl.query(query)
    return result

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python3 query_FindAssetById.py <domain> <account> <asset>")
        sys.exit(1)

    # Retrieve domain, account, and asset from command-line arguments
    domain = sys.argv[1]
    account = sys.argv[2]
    asset = sys.argv[3]

    # Call the function with the domain, account, and asset to perform the query
    asset_info = query_asset_info(domain, account, asset)
    print(asset_info)
