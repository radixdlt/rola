import hashlib
import logging

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
        verify_key = VerifyingKey.from_string(
            bytes.fromhex(self.proof.public_key),
            curve=self.proof.curve)
        # Verify the signature
        try:
            verify_key.verify(self.proof.signature.encode(), signature_message.encode())
            return True
        except BadSignatureError:
            logger.info("Signature is invalid.")
            return False
