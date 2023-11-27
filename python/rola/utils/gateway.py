import requests
from rola.config.network import NETWORKS


def get_entity_owner(
        address: str,
        network_id: str) -> str:

    headers = {"accept": "application/json"}
    body = {"addresses": [address]}
    metadata_items = requests.post(
        url=f"{NETWORKS[network_id]}/state/entity/details",
        headers=headers,
        json=body
    ).json()["items"][0]["metadata"]["items"]
    owner_keys = [item for item in metadata_items if item["key"] == "owner_keys"]
    return owner_keys[0]["value"]["raw_hex"] if len(owner_keys) == 1 else ""
