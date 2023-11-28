import logging

import ed25519
from ecdsa import VerifyingKey, BadSignatureError
from rola.models.proof import Proof

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class SignedChallenge:

    def __init__(self,
                 challenge: str,
                 proof: Proof,
                 address: str,
                 type: str):
        self.challenge = challenge
        self.proof = proof
        self.address = address
        self.type = type

    def verify_signature(self, signature_message: str) -> bool:
        # Create a verifying key object from the public key
        verify_key = ed25519.VerifyingKey(bytes.fromhex(self.proof.public_key))
        try:
            verify_key.verify(
                bytes.fromhex(self.proof.signature),
                bytes.fromhex(signature_message))
            return True
        except BadSignatureError:
            logger.info("Signature is invalid.")
            return False
