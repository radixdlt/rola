class ChallengeWrongLength(Exception):
    def __init__(self):
        super().__init__("Challenge has to be 32 bytes long")


class DappAddressWrongLength(Exception):
    def __init__(self):
        super().__init__("Dapp address has to be 45 chars long")
