import { NetworkId } from '@radixdlt/radix-engine-toolkit'
import type { SignedChallenge } from './rola'
import { Rola } from './rola'

describe('Rola verifySignedChallenge', () => {
  it('should verify signed challenge', async () => {
    for (const { rolaInput, signedChallenge } of [
      {
        rolaInput: {
          networkId: NetworkId.Stokenet,
          applicationName: 'test',
          dAppDefinitionAddress:
            'account_tdx_2_12xdm5g7xdhh73zkh7xkty0dsxw4rw0jl0sq4lr3erpc3xdn54zx0le',
          expectedOrigin: 'https://stokenet-dashboard.radixdlt.com',
        },
        signedChallenge: {
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
        } satisfies SignedChallenge,
      },
      {
        rolaInput: {
          networkId: NetworkId.Mainnet,
          applicationName: 'test',
          dAppDefinitionAddress:
            'account_rdx12y7md4spfq5qy7e3mfjpa52937uvkxf0nmydsu5wydkkxw3qx6nghn',
          expectedOrigin: 'https://dev-sandbox.rdx-works-main.extratools.works',
        },
        signedChallenge: {
          proof: {
            publicKey:
              '0fe0e99bbb51b26af94195d4d61aebbff9b087397a616711c6e7d1600f7c1ebf',
            signature:
              'bfb5edb7238815b0e9baadab2c59e15bf0d110ca3eb90b1528ebaa90a04225363ac168d2fcc3c606676fac948ade3fc625f9ad8d26eaa496124b1963c7d5d007',
            curve: 'curve25519',
          },
          address:
            'account_rdx12yqa5qxme69f0km0uknampsfe8qa0umxkf6sgk4l0hs6jss6vw9zez',
          challenge:
            '722c39c0256213a4fc5b5c2b7856bf8a9c048da4fc64d9089be2f19ca52b58a3',
          type: 'account',
        } satisfies SignedChallenge,
      },
      {
        rolaInput: {
          networkId: NetworkId.Mainnet,
          applicationName: 'test',
          dAppDefinitionAddress:
            'account_rdx12y7md4spfq5qy7e3mfjpa52937uvkxf0nmydsu5wydkkxw3qx6nghn',
          expectedOrigin: 'https://dev-sandbox.rdx-works-main.extratools.works',
        },
        signedChallenge: {
          proof: {
            publicKey:
              '028704afaadc0020d50d634c8c5ef6ae9e918db1da59ab11a21a26e24a919b4bff',
            signature:
              '01762e65c4d01df7bdda9d6ec2b6c1d1df7233e2bb57cf0c6e3e6ccf9f750fb777333e041232c5bedd831ab0e70bcaae08b4f390b122ae5e7e801fb3fba155ed98',
            curve: 'secp256k1',
          },
          address:
            'account_rdx16xtfz7339kx27nhzelg6p9d933x9fjwv6nxa9cyy8pvcmmvfaxslu4',
          challenge:
            'ed45e21bdcfabb47e0c0513cf7179497b41742c368f1a23f37af9a9c43ab1b27',
          type: 'account',
        } satisfies SignedChallenge,
      },
    ]) {
      const result = await Rola(rolaInput).verifySignedChallenge(
        signedChallenge as SignedChallenge,
      )
      if (result.isErr()) throw result.error.jsError
    }
  })

  it('should return error for invalid public key', async () => {
    const result = await Rola({
      networkId: NetworkId.Mainnet,
      applicationName: 'test',
      dAppDefinitionAddress:
        'account_rdx12y7md4spfq5qy7e3mfjpa52937uvkxf0nmydsu5wydkkxw3qx6nghn',
      expectedOrigin: 'https://dev-sandbox.rdx-works-main.extratools.works',
    }).verifySignedChallenge({
      proof: {
        publicKey: '028704afaadc0020d5asdfae9e918db1da59ab11a21a2ff',
        signature:
          '01762e65c4d01df7bdda9d6ec2b6c1d1df7233e2bb57cf0c6e3e6ccf9f750fb777333e041232c5bedd831ab0e70bcaae08b4f390b122ae5e7e801fb3fba155ed98',
        curve: 'secp256k1',
      },
      address:
        'account_rdx16xtfz7339kx27nhzelg6p9d933x9fjwv6nxa9cyy8pvcmmvfaxslu4',
      challenge:
        'ed45e21bdcfabb47e0c0513cf7179497b41742c368f1a23f37af9a9c43ab1b27',
      type: 'account',
    } satisfies SignedChallenge)

    if (result.isOk()) throw new Error('Expected error')
    expect(result.error.reason).toBe('invalidPublicKey')
  })
})
