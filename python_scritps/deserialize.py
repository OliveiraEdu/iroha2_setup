import json
from iroha2 import Client

cfg = json.loads(open("config.json").read())

print ("-"*20)
print(cfg)

print(type (cfg))

print ("-"*20)

cl = Client(cfg)

print (cl)

