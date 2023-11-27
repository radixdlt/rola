from ecdsa import Ed25519, SECP256k1
from radix_engine_toolkit import (
    derive_virtual_identity_address_from_public_key,
    PublicKey, Address)

from rola.models.signed_challenge import SignedChallenge


def derive_address(
        network_id: int,
        signed_challenge: SignedChallenge) -> Address:

    public_key_bytes = bytes.fromhex(signed_challenge.proof.public_key)
    public_key_int_list = [byte for byte in public_key_bytes]
    if signed_challenge.type == "persona":
        return derive_virtual_identity_address_from_public_key(
            network_id=network_id,
            public_key=PublicKey.ED25519(public_key_int_list)
        )
    elif signed_challenge.type == "account":
        if signed_challenge.proof.curve == Ed25519:
            return derive_virtual_identity_address_from_public_key(
                network_id=network_id,
                public_key=PublicKey.ED25519(public_key_int_list)
            )
        elif signed_challenge.proof.curve == SECP256k1:
            return derive_virtual_identity_address_from_public_key(
                network_id=network_id,
                public_key=PublicKey.SECP256K1(public_key_int_list)
            )
        else:
            raise Exception
    else:
        raise Exception

    # TODO add custom exceptions for each error
