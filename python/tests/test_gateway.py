from requests import HTTPError
from rola.exceptions.gateway import EntityNotFound
from rola.utils.gateway import GatewayMetadataProvider


def test_gateway_returns_entity_owner_for_mainnet():
    gateway_metadata_provider = GatewayMetadataProvider.for_mainnet()
    entity_owner = gateway_metadata_provider.entity_owner(
        address="identity_tdx_2_12gc7ajs0araj6ph78dqqd0cvzzcegfygu55jst77vnee2nd05vp8wc")
    assert entity_owner is not None


def test_gateway_returns_entity_owner_for_stokenet():
    gateway_metadata_provider = GatewayMetadataProvider.for_stokenet()
    entity_owner = gateway_metadata_provider.entity_owner(
        address="identity_tdx_2_12gc7ajs0araj6ph78dqqd0cvzzcegfygu55jst77vnee2nd05vp8wc")
    assert entity_owner is not None


def test_gateway_raises_400_error_when_invalid_address():
    gateway_metadata_provider = GatewayMetadataProvider.for_mainnet()
    try:
        gateway_metadata_provider.entity_owner(address="identity_tdx_test")
    except HTTPError as e:
        assert e.response.status_code == 400


def test_gateway_raises_entity_not_found_error():
    gateway_metadata_provider = GatewayMetadataProvider.for_stokenet()
    try:
        gateway_metadata_provider.entity_owner(
            address="validator_rdx1s0g5uuw3a7ad7akueetzq5lpejzp9uw5glv2qnflvymgendvepgduj")
    except EntityNotFound:
        assert True

