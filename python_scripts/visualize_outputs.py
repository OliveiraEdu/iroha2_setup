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
from iroha2.data_model.query.asset import FindAssetById
from iroha2.data_model.query import Query

cfg = json.loads(open("config.json").read())

print(cfg)

cl = Client(cfg)


filter = EventFilter.Pipeline(
    pipeline.EventFilter(
        entity=pipeline.EntityType.Transaction(),
        hash=None,
    ))
    
listener = cl.listen(filter)

for event in listener:
    print(event)

    if event["Pipeline"]["status"] == "Committed" \
        and event["Pipeline"]["hash"] == hash:
        break
