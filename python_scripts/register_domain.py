import json
from iroha2 import Client
from iroha2.data_model.isi import *
from iroha2.data_model.domain import *

cfg = json.loads(open("config.json").read())

print(cfg)

cl = Client(cfg)

domain = Domain("looking_glass")
register = Register(Expression(Value(Identifiable(domain))))

hash = cl.submit_isi(register)
