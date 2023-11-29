from radix_engine_toolkit import (
    derive_virtual_account_address_from_public_key,
    PublicKey,
)

from rola.models.signed_challenge import SignedChallenge
from rola.utils.gateway import get_entity_owner
from rola.utils.helpers import create_public_key_hash
from rola.utils.ret import derive_address


class Rola:
    def __init__(
        self,
        expected_origin: str,
        dapp_address: str,
        application_name: str,
        network_id: str,
    ):
        self.expected_origin = expected_origin
        self.dapp_address = dapp_address
        self.application_name = application_name
        self.network_id = network_id

    def verify_signed_challenge(self, signed_challenge: SignedChallenge) -> bool:
        # create public key hex hash
        public_key_hash_hex = create_public_key_hash(signed_challenge.proof.public_key)
        if public_key_hash_hex == "":
            return False

        # verify the signed challenge signature

        if not signed_challenge.verify_signature():
            return False

        # check that the signed challenge address entity owner contains the
        # public key hash
        entity_owner = get_entity_owner(
            network_id=self.network_id, address=signed_challenge.address
        )
        if not public_key_hash_hex == entity_owner:
            return False

        # derive address from public key
        derived_address = derive_address(
            network_id=int(self.network_id), signed_challenge=signed_challenge
        )
        if not derived_address == signed_challenge.address:
            return False

        return True
