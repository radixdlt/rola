from secrets import token_bytes

from ecdsa import SigningKey, SECP256k1
from radix_engine_toolkit import Curve

from rola.models.challenge import ChallengeType
from rola.models.proof import Proof
from rola.models.signed_challenge import SignedChallenge
from rola.utils.helpers import create_signature_message


def test_verify_signature_for_a_ed25519_curve():
    challenge = bytes.fromhex(
        "fe81d4fddaa22d0c103198f61df8437d8b8899102633c08021ecc41c5ab61dfd"
    )
    publicKey = bytes.fromhex(
        "a6b8a053f51c1f945317bef5f5344321783b243821e919448c5963b9a8a20552"
    )
    dapp_definition_address = (
        "account_tdx_2_12xdm5g7xdhh73zkh7xkty0dsxw4rw0jl0sq4lr3erpc3xdn54zx0le"
    )
    signature = bytes.fromhex(
        "7f3730ae82ba7dfcfad7497a9159381451dc11b77b02fd46f67406752f50800e81ad180a59f37a4642f71845272f3ab605a322acd40de80ee650743d7afe4902"
    )

    signed_challenge = SignedChallenge(
        challenge=challenge,
        proof=Proof(public_key=publicKey, signature=signature, curve=Curve.ED25519),
        address="identity_tdx_2_12gc7ajs0araj6ph78dqqd0cvzzcegfygu55jst77vnee2nd05vp8wc",
        challenge_type=ChallengeType.PERSONA,
    )
    signature_message = create_signature_message(
        challenge=signed_challenge.challenge,
        dapp_definition_address=dapp_definition_address,
        origin="https://stokenet-dashboard.radixdlt.com",
    )

    signature_verified = signed_challenge.verify_signature(signature_message)
    assert signature_verified


def _test_verify_signature_for_a_secp256k1_curve():
    challenge = "fe81d4fddaa22d0c103198f61df8437d8b8899102633c08021ecc41c5ab61dfd"
    publicKey = "a6b8a053f51c1f945317bef5f5344321783b243821e919448c5963b9a8a20552"
    dapp_definition_address = (
        "account_tdx_2_12xdm5g7xdhh73zkh7xkty0dsxw4rw0jl0sq4lr3erpc3xdn54zx0le"
    )
    signature = "7f3730ae82ba7dfcfad7497a9159381451dc11b77b02fd46f67406752f50800e81ad180a59f37a4642f71845272f3ab605a322acd40de80ee650743d7afe4902"

    signed_challenge = SignedChallenge(
        challenge=challenge,
        proof=Proof(public_key=publicKey, signature=signature, curve=SECP256k1),
        address="identity_tdx_2_12gc7ajs0araj6ph78dqqd0cvzzcegfygu55jst77vnee2nd05vp8wc",
        type="persona",
    )
    signature_message = create_signature_message(
        challenge=signed_challenge.challenge,
        dapp_definition_address=dapp_definition_address,
        origin="https://stokenet-dashboard.radixdlt.com",
    )

    signature_verified = signed_challenge.verify_signature(signature_message)
    assert signature_verified


def test_verify_signed_challenge_with_secp256k1_curve():
    challenge = token_bytes(32)
    message = create_signature_message(
        challenge=challenge,
        dapp_definition_address="account_tdx",
        origin="test-origin",
    )

    priv_key = SigningKey.generate(curve=SECP256k1)
    public_key = priv_key.get_verifying_key().to_string("compressed")
    signature = priv_key.sign(message)

    signed_challenge = SignedChallenge(
        challenge=challenge,
        proof=Proof(public_key=public_key, signature=signature, curve=Curve.SECP256K1),
        address="identity",
        challenge_type=ChallengeType.PERSONA,
    )

    assert signed_challenge.verify_signature(message)
