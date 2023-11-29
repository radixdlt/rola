import logging

import ed25519
from ecdsa import BadSignatureError, Ed25519, SECP256k1, SigningKey
from rola.models.proof import Proof

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class SignedChallenge:
    def __init__(self, challenge: str, proof: Proof, address: str, type: str):
        self.challenge = bytes.fromhex(challenge)
        self.proof = proof
        self.address = address
        self.type = type

    def verify_signature(self, signature_message: str) -> bool:
        # Create a verifying key object from the public key
        if self.proof.curve == Ed25519:
            verify_key = ed25519.VerifyingKey(self.proof.public_key)
            try:
                verify_key.verify(self.proof.signature, signature_message)
                return True
            except BadSignatureError:
                logger.info("Signature is invalid.")
                return False
        elif self.proof.curve == SECP256k1:
            verify_key = SigningKey.from_string(
                self.proof.public_key, curve=SECP256k1
            ).verifying_key

            # Verify the signature
            try:
                # Verifying the signature for the given message
                verify_key.verify(self.proof.signature, signature_message)
                logger.info("Signature is invalid.")
                return True
            except Exception as e:
                return False
