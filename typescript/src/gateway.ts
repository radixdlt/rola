export type GatewayService = ReturnType<typeof GatewayService>
import {
  GatewayApiClient,
  RadixNetworkConfigById,
} from '@radixdlt/babylon-gateway-api-sdk'
import { ResultAsync } from 'neverthrow'
import { typedError } from './helpers/typed-error'

export type GatewayServiceInput = {
  networkId: number
  applicationName: string
  gatewayApiClient?: GatewayApiClient
}
export const GatewayService = (input: GatewayServiceInput) => {
  const { networkId, applicationName } = input
  const config = RadixNetworkConfigById[networkId]

  if (!config) throw new Error(`Network ${networkId} not found`)

  const { state } =
    input.gatewayApiClient ??
    GatewayApiClient.initialize({
      basePath: config.gatewayUrl,
      applicationName,
    })

  const getEntityDetails = (address: string) =>
    ResultAsync.fromPromise(
      state.getEntityDetailsVaultAggregated(address),
      typedError,
    )

  return {
    getEntityOwnerKeys: (address: string) =>
      getEntityDetails(address).map(
        (response) =>
          response?.metadata?.items.find((item) => item.key === 'owner_keys')
            ?.value.raw_hex ?? '',
      ),
  }
}
