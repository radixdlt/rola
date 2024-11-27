import Pino from "pino";

export type AppLogger = typeof appLogger;
export const appLogger = Pino({ level: "trace" });
