# 构建 luxuBack 项目
FROM node:18.18.2-slim AS handright
WORKDIR /app/hr_front
COPY . /app/hr_front
RUN corepack enable
RUN pnpm install --frozen-lockfile 

# 创建运行 luxuBack 项目的容器
FROM handright AS hr
EXPOSE 3000
CMD [ "pnpm", "start" ]
