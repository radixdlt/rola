import { defineConfig } from 'tsup'

export default defineConfig({
  entry: ['src/rola.ts'],
  dts: true,
  format: ['esm', 'cjs'],
})
