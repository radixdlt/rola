import requests
from radix_engine_toolkit import PublicKeyHash
from abc import ABC, abstractmethod

from typing import List

from rola.exceptions.gateway import EntityNotFound


class MetadataProvider(ABC):
    @abstractmethod
    def entity_owner(self, address: str) -> List[PublicKeyHash]:
        pass


class GatewayMetadataProvider:
    base_url: str

    def __init__(self, base_url: str = "https://mainnet.radixdlt.com") -> None:
        self.base_url = base_url

    @classmethod
    def for_mainnet(cls) -> "GatewayMetadataProvider":
        return cls("https://mainnet.radixdlt.com")

    @classmethod
    def for_stokenet(cls) -> "GatewayMetadataProvider":
        return cls("https://stokenet.radixdlt.com")

    def entity_owner(self, address: str) -> List[PublicKeyHash]:
        headers = {"accept": "application/json"}
        body = {"addresses": [address]}
        response = requests.post(
            url=f"{self.base_url}/state/entity/details", headers=headers, json=body
        )

        if response.status_code != 200:
            response.raise_for_status()

        items = response.json().get("items", [])
        if not items:
            raise EntityNotFound()

        metadata_items = items[0].get("metadata", {}).get("items", [])
        owner_keys_items = [
            item for item in metadata_items if item["key"] == "owner_keys"
        ][0]["value"]["typed"]
        assert owner_keys_items["type"] == "PublicKeyHashArray"
        return owner_keys_items["values"]
