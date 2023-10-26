import { NetworkId } from '@radixdlt/radix-engine-toolkit'
import { Rola } from './rola'
import type { SignedChallenge } from './types'

describe('Rola', () => {
  const { verifySignedChallenge } = Rola({
    networkId: NetworkId.Stokenet,
    applicationName: 'test',
    dAppDefinitionAddress:
      'account_tdx_2_12xdm5g7xdhh73zkh7xkty0dsxw4rw0jl0sq4lr3erpc3xdn54zx0le',
    expectedOrigin: 'https://stokenet-dashboard.radixdlt.com',
  })

  it('should verify signed challenge', async () => {
    for (const proof of [
      {
        challenge:
          'fe81d4fddaa22d0c103198f61df8437d8b8899102633c08021ecc41c5ab61dfd',
        proof: {
          publicKey:
            'a6b8a053f51c1f945317bef5f5344321783b243821e919448c5963b9a8a20552',
          signature:
            '7f3730ae82ba7dfcfad7497a9159381451dc11b77b02fd46f67406752f50800e81ad180a59f37a4642f71845272f3ab605a322acd40de80ee650743d7afe4902',
          curve: 'curve25519',
        },
        address:
          'identity_tdx_2_12gc7ajs0araj6ph78dqqd0cvzzcegfygu55jst77vnee2nd05vp8wc',
        type: 'persona',
      },
    ] satisfies SignedChallenge[]) {
      const result = await verifySignedChallenge(proof)
      if (result.isErr()) throw result.error.jsError
    }
  })
})
