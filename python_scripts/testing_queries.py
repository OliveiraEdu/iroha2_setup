#!/usr/bin/env python3

from icecream import ic

import json
from os import name

from iroha2 import Client

from iroha2.data_model.isi import Register, Mint
from iroha2.data_model.domain import Domain
from iroha2.data_model.account import Account
from iroha2.data_model import asset, account, expression, Value, Identifiable, Id
from iroha2.data_model.expression import Expression
from iroha2.data_model.events import FilterBox, pipeline, Event
from iroha2.crypto import KeyPair
from iroha2.data_model.query.asset import FindAssetById, FindAssetsByAccountId, FindAllAssets, FindAssetsByName
from iroha2.data_model.query import Query


cfg = json.loads(open("./config.json").read())
cl = Client(cfg)

query = FindAssetById.id(asset.Id("rose#wonderland", "alice@wonderland"))
ic(query)
# print(cl.query(query))
ic(cl.query(query))


alice_id = "alice@wonderland"
asset_name = "pint#wonderland"

query = FindAssetsByAccountId.account.id(alice_id)
ic(query)
# print(cl.query(query))



# let alice_id =
#     AccountId::from_str("alice@wonderland")?;
# let query = QueryBox::FindAssetsByAccountId(
#     FindAssetsByAccountId::new(alice_id)
#   );

