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

    def verify_signature(self) -> bool:
        # Convert hex strings to bytes
        signature = bytes.fromhex(self.proof.signature)

        # Create a verifying key object from the public key
        verify_key = VerifyingKey.from_string(self.proof.public_key, curve=self.proof.curve)

        # Hash the data (you might need to hash your data before verification)
        hashed_data = hashlib.sha256(self.challenge.encode()).digest()

        # Verify the signature
        try:
            verify_key.verify(signature, hashed_data)
            return True
        except BadSignatureError:
            logger.info("Signature is invalid.")
            return False
