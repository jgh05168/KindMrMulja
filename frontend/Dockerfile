FROM node:20.11.1

WORKDIR /kind-mulja

COPY package.json .
COPY package-lock.json .

# 의존성 모듈 삭제후
RUN rm -rf node_modules
# npm install 로 의존성 설치 후 구동
RUN npm i

COPY . .

## EXPOSE [Port you mentioned in the vite.config file]

## vite 환경과 동일하게 포트 설정
EXPOSE 5173/tcp

CMD ["npm", "run", "dev"]