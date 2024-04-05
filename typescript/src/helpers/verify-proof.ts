import type { Result } from 'neverthrow'
import { err, ok } from 'neverthrow'
import { secp256k1 } from '@noble/curves/secp256k1'
import { ed25519 } from '@noble/curves/ed25519'
import type { SignedChallenge } from '../types'

const supportedCurves = new Set(['curve25519', 'secp256k1'])

export const verifyProofFactory =
  (input: SignedChallenge) =>
  (
    signatureMessageHex: string,
  ): Result<undefined, { reason: string; jsError?: Error }> => {
    const isSupportedCurve = supportedCurves.has(input.proof.curve)
    if (!isSupportedCurve) return err({ reason: 'unsupportedCurve' })

    try {
      let isValid = false

      if (input.proof.curve === 'curve25519') {
        isValid = ed25519.verify(
          input.proof.signature,
          signatureMessageHex,
          input.proof.publicKey,
        )
      } else {
        const signature = input.proof.signature.slice(2)
        isValid = secp256k1.verify(
          signature,
          signatureMessageHex,
          input.proof.publicKey,
        )
      }
      return isValid ? ok(undefined) : err({ reason: 'invalidSignature' })
    } catch (error: any) {
      return err({ reason: 'invalidPublicKey', jsError: error })
    }
  }
