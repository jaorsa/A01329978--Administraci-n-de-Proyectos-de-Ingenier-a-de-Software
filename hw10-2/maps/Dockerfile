# Start with a base image containing Java runtime
FROM node:12.7-alpine as node

WORKDIR /app

COPY . .

RUN npm install 

RUN npm run build --prod

COPY --from=node app/bigdata-maps /usr/share/nginx/html

# docker build
# sudo docker build -t jos99/bigdata-maps .

# docker run
# sudo docker run --name jacqueline-springboot-jwt -p 8120:8080 jos99/springboot-jwt

