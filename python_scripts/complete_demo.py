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

cfg = json.loads(open("./config.json").read())
cl = Client(cfg)

domain = Domain("beatles")
register = Register.identifiable(domain)
hash = cl.submit_isi(register)

asset_definition = asset.Definition(
    "letitbe#beatles",
    asset.ValueType.Quantity(),
    asset.Mintable.Infinitely(),
)
register = Register.identifiable(asset_definition)
hash = cl.submit_isi(register)

keypair = KeyPair()
acct = account.Account("paul@beatles", signatories=[keypair.public])
register = Register.identifiable(acct)
hash = cl.submit_isi(register)

#condition = account.SignatureCheckCondition(Expression.Equal(expression.Equal(Value.U32(1), Value.U32(1))))
#account_id = Expression(Value(Id(account.Id("paul", "beatles"))))
#mint = Mint(condition, account_id)
#hash = cl.submit_isi(mint)

amount = Expression(Value(U32(42)))
destination = Expression(Value(Identifiable(asset.DefinitionId.parse("letitbe#beatles"))))
mint_amount = Mint(amount, destination)
cl.submit_isi(mint_amount)

query = FindAssetById.id(asset.Id("rose#wonderland", "alice@wonderland"))
print(cl.query(query))
