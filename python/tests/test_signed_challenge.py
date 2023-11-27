from ecdsa import Ed25519

from rola.models.proof import Proof
from rola.models.signed_challenge import SignedChallenge
from rola.utils.helpers import create_signature_message


def test_verify_signature():
    challenge = 'b519902dd21c9669b81bb5023687879d178e5c4991ba1d0ee9e131cee365bafa'
    publicKey = 'a6b8a053f51c1f945317bef5f5344321783b243821e919448c5963b9a8a20552'
    dapp_definition_address = "account_tdx_2_12xdm5g7xdhh73zkh7xkty0dsxw4rw0jl0sq4lr3erpc3xdn54zx0le"
    signature = 'ff90cc1fba1bf027b07d1c676a755f0136a71002684acd6353346ae1f5e3197fec35c20a35e50fafb4caffdfff25a9f6b4df943e81955d4e756fb21c7962c0f3'

    signed_challenge = SignedChallenge(
        challenge=challenge,
        proof=Proof(
            public_key=publicKey,
            signature=signature,
            curve=Ed25519
        ),
        address="",
        type=""
    )
    signature_message = create_signature_message(
        challenge=challenge,
        dapp_definition_address=dapp_definition_address,
        origin="https://stokenet-dashboard.radixdlt.com")
    signature_verified = signed_challenge.verify_signature(signature_message)
    print((signature_verified))