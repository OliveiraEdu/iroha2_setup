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

    listener = cl.listen(filter)

    for event in listener:
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
    asset_definition = asset.Definition(f"{asset_name}#{domain_name}", value_type, mintable)
    register = Register.identifiable("{asset_name}#{domain_name}")
    hash = cl.submit_isi(register)
    wait_for_tx(cl, hash)

def register_account(cl: Client):
    account_name = input("Enter account name: ")
    domain_name = input("Enter domain name: ")
    keypair = KeyPair()
    ic(keypair)
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

if __name__ == "__main__":
    cfg = json.loads(open("./config.json").read())
    cl = Client(cfg)

    while True:
        print("1. Register Domain")
        print("2. Register Asset")
        print("3. Register Account")
        print("4. Mint Asset")
        print("5. Query Asset")
        print("6. Quit")

        choice = input("Select an option: ")

        if choice == "1":
            register_domain(cl)
        elif choice == "2":
            register_asset(cl)
        elif choice == "3":
            register_account(cl)
        elif choice == "4":
            mint_asset(cl)
        elif choice == "5":
            query_asset(cl)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
