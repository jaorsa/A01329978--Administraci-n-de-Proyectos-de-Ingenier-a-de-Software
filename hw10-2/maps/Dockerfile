### STAGE 1: Build ###
FROM node:12.7-alpine AS build
WORKDIR /app
COPY . . 
RUN npm install
RUN npm run build

### STAGE 2: Run ###
FROM nginx:alpine
COPY --from=build /app/dist/bigdata-maps /usr/share/nginx/html
# docker build
# sudo docker build -t jos99/bigdata-maps .

# docker run
# sudo docker run --name jacqueline-springboot-jwt -p 8120:8080 jos99/springboot-jwt

