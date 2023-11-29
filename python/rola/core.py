from rola.models.signed_challenge import SignedChallenge
from rola.utils.gateway import GatewayMetadataProvider
from rola.utils.helpers import create_public_key_hash
from rola.utils.ret import derive_address


class Rola:
    def __init__(
        self,
        network_id: int,
        dapp_address: str,
        expected_origin: str,
        application_name: str,
        gateway_metadata_provider: GatewayMetadataProvider,
    ):
        self.network_id = network_id
        self.dapp_address = dapp_address
        self.expected_origin = expected_origin
        self.application_name = application_name
        self.gateway_metadata_provider = gateway_metadata_provider

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
        entity_owner = self.gateway_metadata_provider.entity_owner(
            address=signed_challenge.address
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
