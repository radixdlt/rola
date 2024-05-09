// @ts-ignore
if (!globalThis.self) globalThis.self = globalThis

import { ResultAsync, err, errAsync, ok } from 'neverthrow'
import { createSignatureMessage } from './helpers/create-signature-message'
import { verifyProofFactory } from './helpers/verify-proof'
import { deriveVirtualAddress } from './helpers/derive-address-from-public-key'
import { createPublicKeyHash } from './helpers/create-public-key-hash'
import { GatewayService } from './gateway'
import type { GatewayApiClient } from '@radixdlt/babylon-gateway-api-sdk'
import type { SignedChallenge } from './types'

export type RolaError = { reason: string; jsError?: Error }
export type * from './types'

export type VerifyOwnerKeyOnLedgerFn = (
  address: string,
  publicKeyHex: string,
) => ResultAsync<undefined, RolaError>

export type RolaInput = {
  expectedOrigin: string
  dAppDefinitionAddress: string
  applicationName: string
  networkId: number
  gatewayApiClient?: GatewayApiClient
}
export const Rola = (input: RolaInput) => {
  const { expectedOrigin, dAppDefinitionAddress, networkId, applicationName } =
    input

  const gatewayService = GatewayService({
    networkId,
    applicationName,
    gatewayApiClient: input.gatewayApiClient,
  })

  const verifySignedChallenge = (
    signedChallenge: SignedChallenge,
  ): ResultAsync<void, RolaError> => {
    const result = createPublicKeyHash(signedChallenge.proof.publicKey)

    if (result.isErr()) return errAsync({ reason: 'couldNotHashPublicKey' })

    const hashedPublicKey = result.value

    const verifyProof = verifyProofFactory(signedChallenge)

    const getDerivedAddress = () =>
      deriveVirtualAddress(signedChallenge, networkId).mapErr((jsError) => ({
        reason: 'couldNotDeriveAddressFromPublicKey',
        jsError,
      }))

    const queryLedger = () =>
      gatewayService
        .getEntityOwnerKeys(signedChallenge.address)
        .mapErr((jsError) => ({
          reason: 'couldNotVerifyPublicKeyOnLedger',
          jsError,
        }))
        .map((ownerKeys) => ({
          ownerKeysMatchesProvidedPublicKey: ownerKeys
            .toUpperCase()
            .includes(hashedPublicKey.toUpperCase()),
          ownerKeysSet: !!ownerKeys,
        }))

    const deriveAddressFromPublicKeyAndQueryLedger = () =>
      ResultAsync.combine([getDerivedAddress(), queryLedger()])

    return createSignatureMessage({
      dAppDefinitionAddress,
      origin: expectedOrigin,
      challenge: signedChallenge.challenge,
    })
      .andThen(verifyProof)
      .asyncAndThen(deriveAddressFromPublicKeyAndQueryLedger)
      .andThen(
        ([
          derivedAddress,
          { ownerKeysMatchesProvidedPublicKey, ownerKeysSet },
        ]) => {
          const derivedAddressMatchesPublicKey =
            !ownerKeysSet && derivedAddress === signedChallenge.address

          return ownerKeysMatchesProvidedPublicKey ||
            derivedAddressMatchesPublicKey
            ? ok(undefined)
            : err({ reason: 'invalidPublicKey' })
        },
      )
  }

  return { verifySignedChallenge }
}
