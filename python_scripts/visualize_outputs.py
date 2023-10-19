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
