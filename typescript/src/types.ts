export type SignedChallenge = {
  address: string
  type: 'persona' | 'account'
  challenge: string
  proof: {
    publicKey: string
    signature: string
    curve: 'curve25519' | 'secp256k1'
  }
}
