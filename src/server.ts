import express from 'express'
import { randomUUID } from 'node:crypto'
import { logger } from './logger'
import { config } from './config'
import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()

const app = express()
const port = config.port

app.get('/', async (req, res) => {
  const users = await prisma.user.findMany()
  res.send(users)
})

app.post('/', async (req, res) => {
  const user = await prisma.user.create({
    data: {
      identityAddress: randomUUID(),
      name: 'Alice',
    },
  })
  res.send(user)
})

app.listen(port, () => {
  logger.debug(`server listening on port ${port}`)
})
