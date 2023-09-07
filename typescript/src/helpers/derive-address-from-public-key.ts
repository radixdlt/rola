import type { SignedChallenge } from '../types'
import { PublicKey, RadixEngineToolkit } from '@radixdlt/radix-engine-toolkit'
import { ResultAsync, errAsync } from 'neverthrow'
import { typedError } from './typed-error'

export const deriveVirtualIdentityAddress = (
  publicKey: string,
  networkId: number,
) =>
  ResultAsync.fromPromise(
    RadixEngineToolkit.Derive.virtualIdentityAddressFromPublicKey(
      new PublicKey.Ed25519(publicKey),
      networkId,
    ),
    typedError,
  )

export const deriveVirtualEddsaEd25519AccountAddress = (
  publicKey: string,
  networkId: number,
) =>
  ResultAsync.fromPromise(
    RadixEngineToolkit.Derive.virtualAccountAddressFromPublicKey(
      new PublicKey.Ed25519(publicKey),
      networkId,
    ),
    typedError,
  )

export const deriveVirtualEcdsaSecp256k1AccountAddress = (
  publicKey: string,
  networkId: number,
) =>
  ResultAsync.fromPromise(
    RadixEngineToolkit.Derive.virtualAccountAddressFromPublicKey(
      new PublicKey.Secp256k1(publicKey),
      networkId,
    ),
    typedError,
  )

export const deriveVirtualAddress = (
  signedChallenge: SignedChallenge,
  networkId: number,
) => {
  if (signedChallenge.type === 'persona')
    return deriveVirtualIdentityAddress(
      signedChallenge.proof.publicKey,
      networkId,
    )
  else if (
    signedChallenge.type === 'account' &&
    signedChallenge.proof.curve === 'curve25519'
  )
    return deriveVirtualEddsaEd25519AccountAddress(
      signedChallenge.proof.publicKey,
      networkId,
    )
  else if (
    signedChallenge.type === 'account' &&
    signedChallenge.proof.curve === 'secp256k1'
  )
    return deriveVirtualEcdsaSecp256k1AccountAddress(
      signedChallenge.proof.publicKey,
      networkId,
    )

  return errAsync(new Error('Could not derive virtual address'))
}
