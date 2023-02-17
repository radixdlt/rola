const getEnv = (key: string) => {
  const env = process.env[key]
  if (env) {
    return env
  }
  throw `missing env: ${key}`
}

type Config = {
  logLevel: number
  port: number
  nodeEnv: string
}

export const config: Config = {
  logLevel: parseInt(getEnv('LOG_LEVEL')),
  port: parseInt(getEnv('PORT')),
  nodeEnv: getEnv('NODE_ENV'),
}
