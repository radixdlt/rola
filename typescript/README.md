[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# ROLA (Radix Off-Ledger Authentication)

ROLA is a method of authenticating something claimed by the user connected to your dApp with the Radix Wallet. It uses the capabilities of the Radix Network to make this possible in a way that is decentralized and flexible for the user.

ROLA is intended for use in the server backend portion of a Full Stack dApp. It runs "off-ledger" alongside backend business and user management logic, providing reliable authentication of claims of user control using "on-ledger" data from the Radix Network.

## Resources

[What is ROLA](https://docs-babylon.radixdlt.com/main/frontend/rola.html)

## Getting started

`npm install @radixdlt/rola isomorphic-fetch`

## How to use

```typescript
import 'isomorphic-fetch'
import { Rola, SignedChallenge } from '@radixdlt/rola'
import { NetworkId } from '@radixdlt/babylon-gateway-api-sdk'

const { verifySignedChallenge } = Rola({
  networkId: NetworkId.Stokenet,
  applicationName: 'Gumball Club',
  dAppDefinitionAddress:
    'account_tdx_e_128uml7z6mqqqtm035t83alawc3jkvap9sxavecs35ud3ct20jxxuhl',
  expectedOrigin:
    'https://radix-dapp-toolkit-dev.rdx-works-main.extratools.works',
})

// signed challenge response returned from wallet
const signedChallenge = {
  challenge: 'b519902dd21c9669b81bb5023687879d178e5c4991ba1d0ee9e131cee365bafa',
  proof: {
    publicKey:
      '1456b4da4ee62da249459f2180b83e5ebd5db8bad2ed1d8f35f51e7ec2cc98ce',
    signature:
      '8335e38096b3f0ac943c04e4c0b286af8cb711cb5f603a023d1d387fdd0cfae1a0255bcdb5d75cd43690413798959bd4c05af9b86f30d6ff74561bb9c8869202',
    curve: 'curve25519',
  },
  address:
    'identity_tdx_e_122mta8gr4tnjwywlxp5pdt03wfrd68pckne5z3cg2ce4kl3lw48ucy',
  type: 'persona',
}

const result = await verifySignedChallenge(signedChallenge)

// handle error response
if (result.isErr()) throw result.error
```

## Examples

[Full stack example](https://github.com/radixdlt/rola-examples)

- [Typescript full-stack](/examples/typescript-full-stack/README.md)

# License

The ROLA code and examples is released under [Apache 2.0 license](LICENSE). Binaries are licensed under the [Radix Software EULA](http://www.radixdlt.com/terms/genericEULA)
