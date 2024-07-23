from requests import HTTPError
from rola.exceptions.gateway import EntityNotFound
from rola.utils.gateway import GatewayMetadataProvider


def test_gateway_returns_entity_owner_for_stokenet():
    gateway_metadata_provider = GatewayMetadataProvider.for_stokenet()
    entity_owners = gateway_metadata_provider.entity_owner(
        address="identity_tdx_2_12gc7ajs0araj6ph78dqqd0cvzzcegfygu55jst77vnee2nd05vp8wc"
    )
    assert (
        entity_owners[0]["hash_hex"]
        == "31eeca0fe8fb2d06fe3b4006bf0c10b1942488e529282fde64f3954daf"
    )
    assert entity_owners[0]["key_hash_type"] == "EddsaEd25519"


def test_gateway_raises_400_error_when_invalid_address():
    gateway_metadata_provider = GatewayMetadataProvider.for_mainnet()
    try:
        gateway_metadata_provider.entity_owner(address="identity_tdx_test")
    except HTTPError as e:
        assert e.response.status_code == 400
