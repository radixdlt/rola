from rola.utils.gateway import get_entity_owner


def test_gateway_returns_entity_owner():
    entity_owner = get_entity_owner(
        network_id="2",
        address="identity_tdx_2_12gc7ajs0araj6ph78dqqd0cvzzcegfygu55jst77vnee2nd05vp8wc"
    )
    print(entity_owner)