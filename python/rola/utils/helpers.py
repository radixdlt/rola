import hashlib
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


def create_signature_message(challenge, dapp_definition_address, origin):
    # Convert challenge to bytes from hex
    challenge_bytes = bytes.fromhex(challenge)
    # Convert dAppDefinitionAddress to bytes using utf-8 encoding
    dAppDefinitionAddress_bytes = dapp_definition_address.encode('utf-8')
    # Convert origin to bytes using utf-8 encoding
    origin_bytes = origin.encode('utf-8')
    # Create a prefix buffer from ASCII character 'R'
    prefix = b'R'
    # Convert length of dAppDefinitionAddress to bytes using hex encoding
    length_of_dAppDefinitionAddress_bytes = bytes([len(dapp_definition_address)])
    # Concatenate all the buffers
    message_buffer = (prefix +
                      challenge_bytes +
                      length_of_dAppDefinitionAddress_bytes +
                      dAppDefinitionAddress_bytes +
                      origin_bytes)
    # Hash the message using Blake2b
    hashed_message = hashlib.blake2b(message_buffer).hexdigest()
    return hashed_message
