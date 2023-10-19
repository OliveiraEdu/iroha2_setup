import json
from iroha2 import Client
from iroha2.data_model.isi import *
from iroha2.data_model.domain import *

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
