#!/usr/bin/env python3
import json

from iroha2 import Client

from iroha2.data_model.isi import Register, Mint
from iroha2.data_model.domain import Domain
from iroha2.data_model.account import Account
from iroha2.data_model import asset, account, expression, Value, Identifiable, Id
from iroha2.data_model.expression import Expression
from iroha2.data_model.events import FilterBox, pipeline, Event
from iroha2.crypto import KeyPair
from iroha2.data_model.query.asset import FindAssetById, FindAssetsByAccountId, FindAllAssets
from iroha2.data_model.query import Query


cfg = json.loads(open("./config.json").read())
cl = Client(cfg)

# query = FindAssetById.id(asset.Id("rose#wonderland", "alice@wonderland"))
# print(cl.query(query))

# alice_id = "alice@wonderland"  # This should be a string, not an expression

# query = FindAssetsByAccountId(alice_id)  # Pass the account ID as a string
# print(cl.query(query))


query = FindAllAssets()
print(cl.query(query))