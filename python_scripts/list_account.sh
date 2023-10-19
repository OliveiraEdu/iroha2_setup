#!/usr/bin/env python3
import json

from iroha2 import Client

from iroha2.data_model.isi import Register
from iroha2.data_model.domain import Domain
from iroha2.data_model.account import Account
from iroha2.data_model import asset, account
from iroha2.data_model.events import FilterBox, pipeline
from iroha2.crypto import KeyPair

cfg = json.loads(open("./config.json").read())
cl = Client(cfg)

