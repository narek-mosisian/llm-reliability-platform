import { defineConfig, globalIgnores } from "eslint/config";
import nextCoreWebVitals from "eslint-config-next/core-web-vitals";
import nextTypescript from "eslint-config-next/typescript";

export default defineConfig([
  ...nextCoreWebVitals,
  // The three dots represent the spread operator.
  // It unpacks the contents of an array individually.
  // (otherwise it would be nested)
  ...nextTypescript,
  globalIgnores([
    ".next/**",
    "out/**",
    "build/**",
    "next-env.d.ts"
  ])
]);
