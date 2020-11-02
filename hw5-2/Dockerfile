# Start with a base image containing Java runtime
FROM node:12.7-alpine as node

# Add Maintainer Info
LABEL maintainer="adsoft@live.com.mx"

WORKDIR /app

COPY . .

RUN npm install 

RUN npm run build --prod

#Stage 2

FROM nginx:1.13.8-alpine

COPY nginx.conf /etc/nginx/nginx.conf

COPY --from=node /app/dist/maps /usr/share/nginx/html


# docker build
# sudo docker build -t jos99/springboot-jwt .

# docker run
# sudo docker run --name jacqueline-springboot-jwt -p 8120:8080 jos99/springboot-jwt

