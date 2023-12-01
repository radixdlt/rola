import hashlib
import logging
from hashlib import blake2b

from rola.exceptions.helpers import ChallengeWrongLength, DappAddressWrongLength

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def create_public_key_hash(public_key: bytes) -> str:
    hex_encoded = ""
    try:
        hashed = blake2b(public_key, digest_size=32).digest()
        result = hashed[-29:]
        hex_encoded = result.hex()
    except Exception:
        logger.info("Failed to create a hash from the public key")
    return hex_encoded


def create_signature_message(
    challenge: bytes, dapp_definition_address: str, origin: str
) -> bytes:
    """
    Format
        Y = 82 (R in ASCII for ROLA)
        32 raw bytes of the challenge
        1 byte - the length of the UTF-8-encoded bech32-encoded dapp-definition address
        The bytes of the UTF-8-encoded bech32-encoded address
        The bytes of the origin UTF-8 encoded
    """
    prefix = "R".encode()
    if len(challenge) != 32:
        raise ChallengeWrongLength
    length_of_dapp_def_address = len(dapp_definition_address)
    if length_of_dapp_def_address != 69:
        raise DappAddressWrongLength
    length_of_dapp_def_address_bytes = length_of_dapp_def_address.to_bytes(
        1, byteorder="big"
    )

    dapp_def_address_bytes = bytes([ord(c) for c in dapp_definition_address])
    origin_bytes = bytes([ord(c) for c in origin])

    message = b"".join(
        [
            prefix,
            challenge,
            length_of_dapp_def_address_bytes,
            dapp_def_address_bytes,
            origin_bytes,
        ]
    )

    hash_result = hashlib.blake2b(message, digest_size=32).hexdigest()
    return bytes.fromhex(hash_result)
