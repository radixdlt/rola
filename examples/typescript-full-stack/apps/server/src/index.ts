import express from 'express'
import { secureRandom } from './secure-random'
import cors from 'cors'
import { Rola, SignedChallenge } from '@radixdlt/rola'
import { ResultAsync } from 'neverthrow'

const app = express()
app.use(cors())
app.use(express.json())

const port = 3000

// A simple in-memory store for challenges. A database should be used in production.
const ChallengeStore = () => {
  const challenges = new Map<string, { expires: number }>()

  const create = () => {
    const challenge = secureRandom(32) // 32 random bytes as hex string
    const expires = Date.now() + 1000 * 60 * 5 // expires in 5 minutes
    challenges.set(challenge, { expires }) // store challenge with expiration

    return challenge
  }

  const verify = (input: string) => {
    const challenge = challenges.get(input)

    if (!challenge) return false

    challenges.delete(input) // remove challenge after it has been used
    const isValid = challenge.expires > Date.now() // check if challenge has expired

    return isValid
  }

  return { create, verify }
}

const challengeStore = ChallengeStore()

const { verifySignedChallenge } = Rola({
  applicationName: 'Rola Full Stack Typescript Example',
  dAppDefinitionAddress:
    'account_tdx_2_12yf9gd53yfep7a669fv2t3wm7nz9zeezwd04n02a433ker8vza6rhe', // address of the dApp definition
  networkId: 2, // network id of the Radix network
  expectedOrigin: 'http://localhost:4000', // origin of the client making the wallet request
})

app.get('/create-challenge', (req, res) => {
  res.send({ challenge: challengeStore.create() })
})

app.post<{}, { valid: boolean }, SignedChallenge[]>(
  '/verify',
  async (req, res) => {
    const challenges = [
      ...req.body
        .reduce((acc, curr) => acc.add(curr.challenge), new Set<string>())
        .values(),
    ]
    const isChallengeValid = challenges.every((challenge) =>
      challengeStore.verify(challenge)
    )

    if (!isChallengeValid) return res.send({ valid: false })

    const result = await ResultAsync.combine(
      req.body.map((signedChallenge) => verifySignedChallenge(signedChallenge))
    )

    if (result.isErr()) return res.send({ valid: false })

    // The signature is valid and the public key is owned by the user
    res.send({ valid: true })
  }
)

app.listen(port, () => {
  console.log(`server listening on port http://localhost:${port}`)
})
