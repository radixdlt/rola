from radix_engine_toolkit import (
    derive_virtual_identity_address_from_public_key,
    PublicKey,
    Address,
    Curve,
    derive_virtual_account_address_from_public_key,
)

from rola.models.challenge import ChallengeType
from rola.models.signed_challenge import SignedChallenge


def derive_address(network_id: int, signed_challenge: SignedChallenge) -> Address:
    public_key_int_list = [byte for byte in signed_challenge.proof.public_key]
    if signed_challenge.challenge_type == ChallengeType.PERSONA:
        return derive_virtual_identity_address_from_public_key(
            network_id=network_id, public_key=PublicKey.ED25519(public_key_int_list)
        )
    elif signed_challenge.challenge_type == ChallengeType.ACCOUNT:
        if signed_challenge.proof.curve == Curve.ED25519:
            return derive_virtual_account_address_from_public_key(
                network_id=network_id, public_key=PublicKey.ED25519(public_key_int_list)
            )
        elif signed_challenge.proof.curve == Curve.SECP256K1:
            return derive_virtual_identity_address_from_public_key(
                network_id=network_id,
                public_key=PublicKey.SECP256K1(public_key_int_list),
            )
        else:
            raise Exception
    else:
        raise Exception

    # TODO add custom exceptions for each error
