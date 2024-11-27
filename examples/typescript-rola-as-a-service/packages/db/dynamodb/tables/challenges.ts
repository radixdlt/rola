import type { Challenge } from "../../type";
import { DynamoDbAdapter } from "../dynamodb";

const { AWS_REGION, SST_Table_tableName_challenges } = process.env;

export const challengeTable = DynamoDbAdapter<Challenge, "challenge">({
  primaryKey: "challenge",
  tableName: SST_Table_tableName_challenges!,
  region: AWS_REGION!,
});
