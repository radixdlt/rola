import { NetworkId } from '@radixdlt/radix-engine-toolkit'
import { Rola } from './rola'
import type { SignedChallenge } from '@radixdlt/radix-dapp-toolkit'

describe('Rola', () => {
  const { verifySignedChallenge } = Rola({
    networkId: NetworkId.RCNetV3,
    applicationName: 'test',
    dAppDefinitionAddress:
      'account_tdx_e_128uml7z6mqqqtm035t83alawc3jkvap9sxavecs35ud3ct20jxxuhl',
    expectedOrigin:
      'https://radix-dapp-toolkit-dev.rdx-works-main.extratools.works',
  })

  it('should verify signed challenge', async () => {
    for (const proof of [
      {
        challenge:
          'b519902dd21c9669b81bb5023687879d178e5c4991ba1d0ee9e131cee365bafa',
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
      },
      {
        proof: {
          publicKey:
            '5bc0bb873ca3faeeb18c6c056abf50897fd224f4be3c646aaf77f8131b23f373',
          signature:
            '1e36fedc212ac607d13d8c7db4eb67e049230ff9e40b40d63a28147d285f1663a59d59dc3d8cec845b4512aab9bf6f08680c5885ec9dca41681b12c68e29c60d',
          curve: 'curve25519',
        },
        address:
          'account_tdx_e_12yna5ce4lcmkhadsealv4umqmzyftcrrnhvhyqk7n6yu6kuu5mwv9f',
        challenge:
          'b519902dd21c9669b81bb5023687879d178e5c4991ba1d0ee9e131cee365bafa',
        type: 'account',
      },
    ] satisfies SignedChallenge[]) {
      const result = await verifySignedChallenge(proof)
      if (result.isErr()) throw result.error.jsError
    }
  })
})
