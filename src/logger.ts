import { config } from './config'
import { Logger } from 'tslog'

export const logger = new Logger({ minLevel: config.logLevel })
