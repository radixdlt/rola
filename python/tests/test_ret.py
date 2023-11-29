from ecdsa import Ed25519

from rola.models.proof import Proof
from rola.models.signed_challenge import SignedChallenge
from rola.utils.ret import derive_address


def test_derive_address_from_proof_with_type_person():
    challenge = "b519902dd21c9669b81bb5023687879d178e5c4991ba1d0ee9e131cee365bafa"
    publicKey = "1456b4da4ee62da249459f2180b83e5ebd5db8bad2ed1d8f35f51e7ec2cc98ce"
    signature = "8335e38096b3f0ac943c04e4c0b286af8cb711cb5f603a023d1d387fdd0cfae1a0255bcdb5d75cd43690413798959bd4c05af9b86f30d6ff74561bb9c8869202"

    signed_challenge = SignedChallenge(
        challenge=challenge,
        proof=Proof(public_key=publicKey, signature=signature, curve=Ed25519),
        address="",
        type="persona",
    )
    address = derive_address(network_id=2, signed_challenge=signed_challenge)
    print(address)
