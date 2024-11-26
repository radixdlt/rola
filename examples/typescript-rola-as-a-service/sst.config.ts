import { SSTConfig } from "sst";
import { NetworkId } from "@radixdlt/rola";
import { Parameter } from "sst/constructs/Parameter.js";
import { RadixNetworkConfig } from "@radixdlt/radix-dapp-toolkit";
import { StackContext, Api, Table } from "sst/constructs";

const network = process.env.NETWORK_NAME || "Stokenet";

const networkConfig = RadixNetworkConfig[network];

if (!networkConfig) throw new Error(`Unknown network ${network}`);

const config = {
  [NetworkId.Stokenet]: {
    origin: "http://localhost:4000",
    dAppDefinitionAddress:
      "account_tdx_2_12yf9gd53yfep7a669fv2t3wm7nz9zeezwd04n02a433ker8vza6rhe",
    stage: networkConfig.networkName,
  },
  [NetworkId.Mainnet]: {
    origin: "",
    dAppDefinitionAddress: "",
    stage: networkConfig.networkName,
  },
}[networkConfig.networkId];

export default {
  config(_input) {
    return {
      name: "my-sst-app",
      region: "eu-west-2",
      profile: "sandbox",
    };
  },
  stacks(app) {
    app.stack(function API({ stack }: StackContext) {
      const challengeTable = new Table(stack, "challenges", {
        fields: {
          challenge: "string",
          expiresAt: "number",
        },
        timeToLiveAttribute: "expiresAt",
        primaryIndex: { partitionKey: "challenge" },
      });

      const origin = new Parameter(stack, "origin", {
        value: config.origin,
      });

      const networkId = new Parameter(stack, "networkId", {
        value: networkConfig.networkId.toString(),
      });

      const dAppDefinitionAddress = new Parameter(
        stack,
        "dAppDefinitionAddress",
        {
          value: config.dAppDefinitionAddress,
        }
      );

      const api = new Api(stack, "api", {
        defaults: {
          function: {
            bind: [challengeTable, origin, networkId, dAppDefinitionAddress],
          },
        },
        routes: {
          "POST /create-challenge": "packages/functions/src/challenge.create",
          "POST /verify": "packages/functions/src/challenge.verify",
        },
      });

      stack.addOutputs({
        ApiEndpoint: api.url,
      });
    });
  },
} satisfies SSTConfig;
