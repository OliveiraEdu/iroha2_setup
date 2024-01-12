from icecream import ic
import json
from iroha2 import Client
from iroha2.data_model.isi import Register, Mint
from iroha2.data_model.domain import Domain
from iroha2.data_model.account import Account
from iroha2.data_model import asset, account, expression, Value, Identifiable, Id
from iroha2.data_model.expression import Expression
from iroha2.data_model.events import FilterBox, pipeline, Event
from iroha2.crypto import KeyPair
from iroha2.data_model.query.asset import FindAssetById
from iroha2.data_model.query import Query

def wait_for_tx(cl: Client, hash: str):
    filter = FilterBox(
        pipeline.EventFilter(
            entity_kind=pipeline.EntityKind.Transaction(),
            status_kind=None,
            hash=None,
        ))
    ic(filter)

    listener = cl.listen(filter)

    ic(listener)
    
    for event in listener:
        ic(event)
        if isinstance(event, Event.Pipeline) and event.hash == hash:
            if isinstance(event.status, pipeline.Status.Committed):
                return
            elif isinstance(event.status, pipeline.Status.Validating):
                pass
            else:
                raise RuntimeError(f"Tx rejected: {event.status}")

def register_domain(cl: Client):
    domain_name = input("Enter domain name: ")
    domain = Domain(domain_name)
    register = Register.identifiable(domain)
    hash = cl.submit_isi(register)
    wait_for_tx(cl, hash)

def register_asset(cl: Client):
    asset_name = input("Enter asset name: ")
    domain_name = input("Enter domain name: ")
    value_type = asset.ValueType.Quantity()
    mintable = asset.Mintable.Infinitely()
    metadata={"a": Value.U32(10)}
    asset_definition = asset.Definition(f"{asset_name}#{domain_name}", value_type, mintable, metadata)
    register = Register.identifiable(asset_definition)
    hash = cl.submit_isi(register)
    wait_for_tx(cl, hash)

def register_asset_metadata(cl: Client):
    asset_name = input("Enter asset name: ")
    domain_name = input("Enter domain name: ")
    value_type = asset.ValueType.Store()
    mintable = asset.Mintable.Infinitely()
    metadata={"id": Value.Metadata("new_id")}
    asset_definition = asset.Definition(f"{asset_name}#{domain_name}", value_type, mintable)
    register = Register.identifiable(asset_definition)
    hash = cl.submit_isi(register)
    wait_for_tx(cl, hash)

def register_account(cl: Client):
    account_name = input("Enter account name: ")
    domain_name = input("Enter domain name: ")
    keypair = KeyPair()
    acct = account.Account(f"{account_name}@{domain_name}", signatories=[keypair.public])
    register = Register.identifiable(acct)
    hash = cl.submit_isi(register)
    wait_for_tx(cl, hash)

def mint_asset(cl: Client):
    account_name = input("Enter account name: ")
    domain_name = input("Enter domain name: ")
    asset_name = input("Enter asset name: ")
    quantity = int(input("Enter the quantity to mint: "))  # Added input for quantity
    asset_id = asset.Id(f"{asset_name}#{domain_name}", f"{account_name}@{domain_name}")
    account_id = f"{account_name}@{domain_name}"
    destination = Expression(Value.Id(Id.AssetId(asset_id)))
    amount = Expression(Value.U32(quantity))
    mint_amount = Mint(amount, destination)
    
    hash = cl.submit_isi(mint_amount)
    wait_for_tx(cl, hash)


def query_asset(cl: Client):
    account_name = input("Enter account name: ")
    domain_name = input("Enter domain name: ")
    asset_name = input("Enter asset name: ")
    query = FindAssetById.id(asset.Id(f"{asset_name}#{domain_name}", f"{account_name}@{domain_name}"))
    result = cl.query(query)
    print(result)

def query_asset_by_definition(cl: Client):
    domain_name = input("Enter domain name: ")
    asset_name = input("Enter asset name: ")
    query = FindAssetDefinitionById.id(asset.Id(f"{asset_name}#{domain_name}"))
    result = cl.query(query)
    print(result)

if __name__ == "__main__":
    cfg = json.loads(open("./config.json").read())
    cl = Client(cfg)

    while True:
        print("1. Register Domain")
        print("2. Register Asset")
        print("3. Register Asset Metadata")
        print("4. Register Account")
        print("5. Mint Asset")
        print("6. Query Asset by Account Id")
        print("7. Query Asset by Definition")
        print("8. Quit")

        choice = input("Select an option: ")

        if choice == "1":
            register_domain(cl)
        elif choice == "2":
            register_asset(cl)
        elif choice == "3":
            register_asset_metadata(cl)            
        elif choice == "4":
            register_account(cl)
        elif choice == "5":
            mint_asset(cl)
        elif choice == "6":
            query_asset(cl)
        elif choice == "7":
            query_asset_by_definition(cl)
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")
