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


cfg = json.loads(open("./config.json").read())
cl = Client(cfg)

domain = Domain("rabbit_hole")
register = Register.identifiable(domain)
hash = cl.submit_isi(register)
wait_for_tx(cl, hash)

#asset_definition = asset.Definition(
#    "jar_of_marmelade#rabbit_hole",
#    asset.ValueType.Quantity(),
#    asset.Mintable.Infinitely(),
#)

jar_of_marmelade = asset.Definition(
    value_type=asset.ValueType.Quantity,
    id=asset.DefinitionId(name="jar_of_marmelade", domain_name="rabbit_hole"),
    metadata={"a": Value.U32(10)},
    mintable=False
)

register = Register.identifiable(jar_of_marmelade)
hash = cl.submit_isi(register)
wait_for_tx(cl, hash)

keypair = KeyPair()
acct = account.Account("dodo@rabbit_hole", signatories=[keypair.public])
register = Register.identifiable(acct)
hash = cl.submit_isi(register)
wait_for_tx(cl, hash)

condition = account.SignatureCheckCondition(Expression.Equal(expression.Equal(Value.U32(1), Value.U32(1))))
account_id = Expression(Value(Id(account.Id("dodo", "rabbit_hole"))))
mint = Mint(condition, account_id)
hash = cl.submit_isi(mint)
wait_for_tx(cl, hash)

query = FindAssetById.id(asset.Id("jar_of_marmelade#rabbit_hole", "dodo@rabbit_hole"))
print(cl.query(query))
