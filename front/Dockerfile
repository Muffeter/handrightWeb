# Stage 1: Build the frontend
FROM node:20-slim AS base
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable

FROM base AS build
COPY . /app/hr_front
WORKDIR /app/hr_front
RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install --frozen-lockfile
RUN pnpm run -r build

FROM base AS app
COPY --from=build /app/hr_front /app/hr_front
WORKDIR /app/hr_front
EXPOSE 5000
CMD ["pnpm", "run", "dev", "--host"]

