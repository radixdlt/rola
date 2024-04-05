import type { Result } from 'neverthrow'
import { err, ok } from 'neverthrow'
import { curve25519 } from '../crypto/curve25519'
import { secp256k1 } from '../crypto/secp256k1'
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
        const publicKey = curve25519.keyFromPublic(
          input.proof.publicKey,
          // @ts-ignore: incorrect type definition in EC lib
          'hex',
        )
        isValid = publicKey.verify(signatureMessageHex, input.proof.signature)
      } else {
        const signature = input.proof.signature.slice(2)
        const r = signature.slice(0, 64)
        const s = signature.slice(64, 128)
        isValid = secp256k1
          .keyFromPublic(input.proof.publicKey, 'hex')
          .verify(signatureMessageHex, { r, s })
      }
      return isValid ? ok(undefined) : err({ reason: 'invalidSignature' })
    } catch (error: any) {
      return err({ reason: 'invalidPublicKey', jsError: error })
    }
  }
