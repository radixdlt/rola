from radix_engine_toolkit import Curve

from rola.core import Rola
from rola.models.challenge import ChallengeType
from rola.models.proof import Proof
from rola.models.signed_challenge import SignedChallenge
from rola.utils.gateway import GatewayMetadataProvider


def test_verify_signed_challenge_with_ed25519_curve():
    challenge = bytes.fromhex(
        "fe81d4fddaa22d0c103198f61df8437d8b8899102633c08021ecc41c5ab61dfd"
    )
    publicKey = bytes.fromhex(
        "a6b8a053f51c1f945317bef5f5344321783b243821e919448c5963b9a8a20552"
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

    rola = Rola(
        network_id=2,
        dapp_address="account_tdx_2_12xdm5g7xdhh73zkh7xkty0dsxw4rw0jl0sq4lr3erpc3xdn54zx0le",
        expected_origin="https://stokenet-dashboard.radixdlt.com",
        application_name="TestApp",
        gateway_metadata_provider=GatewayMetadataProvider.for_stokenet(),
    )

    assert rola.verify_signed_challenge(signed_challenge)
