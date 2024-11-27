from radix_engine_toolkit import Curve


class Proof:
    def __init__(self, public_key: bytes, signature: bytes, curve: Curve):
        self.public_key = public_key
        self.signature = signature
        self.curve = curve
