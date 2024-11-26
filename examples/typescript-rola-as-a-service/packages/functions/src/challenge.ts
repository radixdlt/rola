import { ApiHandler } from "sst/node/api";
import { authController } from "../../auth/controller";
import { appLogger } from "../../helpers/logger";
import { SignedChallenge } from "@radixdlt/radix-dapp-toolkit";

export const create = ApiHandler(async (_evt) => {
  const result = await authController.createChallenge();
  if (result.isErr()) {
    appLogger.error(result.error);
    return {
      statusCode: 500,
      body: "Internal server error",
    };
  }
  return {
    statusCode: 200,
    body: JSON.stringify({ challenge: result.value.data.challenge }),
  };
});

const parseJSON = (value: unknown) => {
  try {
    return JSON.parse(value as string);
  } catch (e) {
    return [];
  }
};

export const verify = ApiHandler(async (_evt) => {
  appLogger.debug(_evt);
  const signedChallenges = parseJSON(_evt?.body);

  const result = await authController.verify(signedChallenges);

  if (result.isErr()) {
    appLogger.error(result.error);
    return {
      statusCode: result.error.httpResponseCode,
      body: JSON.stringify({ error: result.error.reason }),
    };
  }
  return {
    statusCode: 200,
    body: JSON.stringify(result.value.data),
  };
});
