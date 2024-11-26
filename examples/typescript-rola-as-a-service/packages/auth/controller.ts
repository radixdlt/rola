import { appLogger, type AppLogger } from "../helpers/logger";
import type { ControllerOutput } from "../_types";

import { hasChallengeExpired } from "./helpers/has-challenge-expired";
import { Rola } from "@radixdlt/rola";
import { SignedChallenge } from "@radixdlt/radix-dapp-toolkit";

import { err, errAsync, ok } from "neverthrow";
import { AuthModel } from "./model";
import { challengeTable } from "../db/dynamodb/tables";
import { ResultAsync } from "neverthrow";

const {
  SST_Parameter_value_origin,
  SST_Parameter_value_dAppDefinitionAddress,
  SST_Parameter_value_networkId,
} = process.env;

export type AuthController = ReturnType<typeof AuthController>;
export const AuthController = ({
  authModel,
  logger,
  expectedOrigin,
  dAppDefinitionAddress,
  networkId,
}: {
  authModel: AuthModel;
  expectedOrigin: string;
  dAppDefinitionAddress: string;
  networkId: number;
  logger: AppLogger;
}) => {
  const { verifySignedChallenge } = Rola({
    applicationName: "",
    expectedOrigin,
    dAppDefinitionAddress,
    networkId,
  });

  const createChallenge = (): ControllerOutput<{ challenge: string }> =>
    authModel
      .createChallenge()
      .map((challenge) => ({ data: { challenge }, httpResponseCode: 201 }));

  const verify = (
    signedChallenges: SignedChallenge[]
  ): ControllerOutput<{
    valid: boolean;
  }> => {
    logger?.debug("Verifying signed challenge", signedChallenges);

    const isValid = signedChallenges.every(
      (value) => SignedChallenge.safeParse(value).success
    );

    if (!isValid)
      return errAsync({
        httpResponseCode: 400,
        reason: "invalidRequestBody",
      });

    const challenge = signedChallenges[0].challenge;
    const isSameChallenge = signedChallenges.every(
      (value) => value.challenge === challenge
    );

    if (!isSameChallenge)
      return errAsync({
        httpResponseCode: 400,
        reason: "invalidRequestBody",
      });

    return authModel
      .getAndDelete(challenge)
      .andThen((challenge) =>
        challenge
          ? ok(challenge)
          : err({ reason: "challengeNotFound", jsError: undefined })
      )
      .andThen(hasChallengeExpired)
      .andThen(() =>
        ResultAsync.combine(
          signedChallenges.map((signedChallenge) =>
            verifySignedChallenge(signedChallenge)
          )
        )
      )
      .mapErr(({ reason, jsError }) => ({
        httpResponseCode: 400,
        reason,
        jsError,
      }))
      .map(() => ({
        data: { valid: true },
        httpResponseCode: 200,
      }));
  };

  return {
    createChallenge,
    verify,
    options: { expectedOrigin, dAppDefinitionAddress, networkId },
  };
};

const options = {
  expectedOrigin: SST_Parameter_value_origin || "",
  networkId: parseInt(SST_Parameter_value_networkId || ""),
  dAppDefinitionAddress: SST_Parameter_value_dAppDefinitionAddress || "",
};

export const authController = AuthController({
  ...options,
  logger: appLogger,
  authModel: AuthModel(challengeTable),
});
