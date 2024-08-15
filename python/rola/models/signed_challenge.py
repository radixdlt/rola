import logging

import ed25519
from ecdsa import SECP256k1, VerifyingKey
from radix_engine_toolkit import Curve
from rola.models.challenge import ChallengeType
from rola.models.proof import Proof

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class SignedChallenge:
    def __init__(
        self,
        challenge: bytes,
        proof: Proof,
        address: str,
        challenge_type: ChallengeType,
    ):
        self.challenge = challenge
        self.proof = proof
        self.address = address
        self.challenge_type = challenge_type

    def verify_signature(self, signature_message: bytes) -> bool:
        # Create a verifying key object from the public key
        if self.proof.curve == Curve.ED25519:
            try:
                verify_key = ed25519.VerifyingKey(self.proof.public_key)
                verify_key.verify(self.proof.signature, signature_message)
                return True
            except ed25519.BadSignatureError:
                logger.info("Signature is invalid.")
                return False
            except AttributeError as e:
                logger.info(f"Signature is invalid: {e}")
                return False
            except AssertionError as e:
                logger.info(f"Signature is invalid: {e}")
                return False
            except Exception as e:
                logger.info(f"Verify signature exception: {e}")
                return False
        elif self.proof.curve == Curve.SECP256K1:
            try:
                verify_key = VerifyingKey.from_string(
                    string=self.proof.public_key, curve=SECP256k1
                )
                verify_key.verify(self.proof.signature, signature_message)
                logger.info("Signature is valid.")
                return True
            except Exception as e:
                return False
        else:
            return False
