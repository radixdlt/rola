import logging

import ed25519
from ecdsa import VerifyingKey, BadSignatureError, Ed25519, SECP256k1, SigningKey
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
        public_key_bytes = bytes.fromhex(self.proof.public_key)
        if self.proof.curve == Ed25519:
            verify_key = ed25519.VerifyingKey(public_key_bytes)
            try:
                verify_key.verify(
                    bytes.fromhex(self.proof.signature),
                    bytes.fromhex(signature_message))
                return True
            except BadSignatureError:
                logger.info("Signature is invalid.")
                return False
        elif self.proof.curve == SECP256k1:
            verify_key = SigningKey.from_string(
                public_key_bytes,
                curve=SECP256k1).verifying_key

            # Verify the signature
            try:
                # Verifying the signature for the given message
                verify_key.verify(
                    bytes.fromhex(self.proof.signature),
                    bytes.fromhex(signature_message))
                print("Signature is valid.")
            except Exception as e:
                print("Signature is invalid:", e)
