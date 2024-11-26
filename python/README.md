[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# ROLA (Radix Off-Ledger Authentication)

ROLA is a method of authenticating something claimed by the user connected to your dApp with the Radix Wallet. It uses the capabilities of the Radix Network to make this possible in a way that is decentralized and flexible for the user.

ROLA is intended for use in the server backend portion of a Full Stack dApp. It runs "off-ledger" alongside backend business and user management logic, providing reliable authentication of claims of user control using "on-ledger" data from the Radix Network.

## Resources

[What is ROLA](https://docs-babylon.radixdlt.com/main/frontend/rola.html)

## Getting started

`pip install .`

## How to use

```python
>>> from ecdsa import Ed25519, SECP256k1
>>>
>>> from rola.models.proof import Proof
>>> from rola.models.signed_challenge import SignedChallenge
>>> from rola.utils.helpers import create_signature_message

>>> challenge = "fe81d4fddaa22d0c103198f61df8437d8b8899102633c08021ecc41c5ab61dfd"
>>> publicKey = "a6b8a053f51c1f945317bef5f5344321783b243821e919448c5963b9a8a20552"
>>> dapp_definition_address = (
...     "account_tdx_2_12xdm5g7xdhh73zkh7xkty0dsxw4rw0jl0sq4lr3erpc3xdn54zx0le"
... )
>>> signature = "7f3730ae82ba7dfcfad7497a9159381451dc11b77b02fd46f67406752f50800e81ad180a59f37a4642f71845272f3ab605a322acd40de80ee650743d7afe4902"
>>>
>>> signed_challenge = SignedChallenge(
...     challenge=challenge,
...     proof=Proof(public_key=publicKey, signature=signature, curve=Ed25519),
...     address="identity_tdx_2_12gc7ajs0araj6ph78dqqd0cvzzcegfygu55jst77vnee2nd05vp8wc",
...     type="persona",
... )
>>> signature_message = create_signature_message(
...     challenge=challenge,
...     dapp_definition_address=dapp_definition_address,
...     origin="https://stokenet-dashboard.radixdlt.com",
... )
>>>
>>> signature_verified = signed_challenge.verify_signature(signature_message)
>>>
>>>
>>> signature_verified
True
```

# License

The executable components of the Radix Transaction Manifest Extension Code are licensed under the [Radix Software EULA](http://www.radixdlt.com/terms/genericEULA).

The Radix Transaction Manifest Extension Code is released under the [Apache 2.0](LICENSE) license:

      Copyright 2023 Radix Publishing Ltd

      Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.

      You may obtain a copy of the License at: http://www.apache.org/licenses/LICENSE-2.0

      Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

      See the License for the specific language governing permissions and limitations under the License.
