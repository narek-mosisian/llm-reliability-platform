FROM node:22-bookworm-slim
# takes a finished Node.js image with Node.js 22 and Debian Bookworm slim

WORKDIR /app

ENV NEXT_TELEMETRY_DISABLED=1
# disables Next.js telemetry (Next.js would otherwise send anonymous usage data)
ENV COREPACK_ENABLE_DOWNLOAD_PROMPT=0
# prevents interactive prompts from Corepack during the Docker build

RUN corepack enable && corepack prepare pnpm@10.32.1 --activate

COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile
# the lock file must not be changed

COPY next.config.ts tsconfig.json eslint.config.mjs next-env.d.ts ./
COPY src ./src

RUN pnpm build

EXPOSE 3000

CMD ["pnpm", "exec", "next", "start", "--hostname", "0.0.0.0", "--port", "3000"]
