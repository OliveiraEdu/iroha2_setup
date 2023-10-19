from iroha2.data_model.isi import *
from iroha2.data_model.account import *

public_key = \u2026 # Get this from white_rabbit.
bunny = Account("white_rabbit@looking_glass", signatories=[public_key])
register = Register(Expression(Value(Identifiable(bunny))))
