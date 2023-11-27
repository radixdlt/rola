from ecdsa.curves import Curve


class Proof:

    def __init__(self,
                 public_key: str,
                 signature: str,
                 curve: Curve):
        self.public_key = public_key
        self.signature = signature
        self.curve = curve


