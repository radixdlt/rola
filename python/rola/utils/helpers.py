import logging
from hashlib import blake2b

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def create_public_key_hash(public_key: str) -> str:
    hex_encoded = ""
    try:
        hashed = blake2b(bytes.fromhex(public_key)).digest()
        result = hashed[-29:]
        hex_encoded = result.hex()
    except Exception:
        logger.info("Failed to create a hash from the public key")
    return hex_encoded
