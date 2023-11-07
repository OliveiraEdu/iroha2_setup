import sys
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

def register_domain(cl: Client, domain: Domain) -> str:
    register = Register.identifiable(domain)
    hash = cl.submit_isi(register)
    wait_for_tx(cl, hash)
    return hash

def register_asset_definition(cl: Client, asset_definition: asset.Definition) -> str:
    register = Register.identifiable(asset_definition)
    hash = cl.submit_isi(register)
    wait_for_tx(cl, hash)
    return hash

def register_account(cl: Client, account: Account) -> str:
    register = Register.identifiable(account)
    hash = cl.submit_isi(register)
    wait_for_tx(cl, hash)
    return hash

def mint_asset(cl: Client, condition: Expression, account_id: Expression) -> str:
    mint = Mint(condition, account_id)
    hash = cl.submit_isi(mint)
    wait_for_tx(cl, hash)
    return hash

def query_asset_info(cl: Client, asset_id: asset.Id) -> Query.Result:
    query = FindAssetById.id(asset_id)
    return cl.query(query)

def interactive_menu():
    # Read the configuration from the config.json file
    with open("./config.json", "r") as f:
        cfg = json.load(f)

    # Create an Iroha2 client
    cl = Client(cfg)

    print("Welcome to the Iroha interactive menu!")

    # Get the user input
    domain = input("Enter the domain name: ")
    asset_definition = input("Enter the asset definition: ")
    account_name = input("Enter the account name: ")
    asset_id = input("Enter the asset ID: ")

    # Register the domain
    domain_hash = register_domain(cl, domain)

    # Register the asset definition
    asset_definition_hash = register_asset_definition(cl, asset_definition)

    # Register the account
    account = Account(account_name)
    account_hash = register_account(cl, account)

    # Mint the asset
    condition = account.SignatureCheckCondition(Expression.Equal(expression.Equal(Value.U32(1), Value.U32(1))))
    account_id = Expression(Value(Id(account.Id(account_name))))
    mint_hash = mint_asset(cl, condition, account_id)

    # Query for the asset information
    asset_info = query_asset_info(cl, asset.Id(asset_id))

    # Print the asset information
    print(asset_info)
