### STAGE 1: Build ###
FROM node:12.7-alpine AS build
WORKDIR /app
COPY . . 
RUN npm install
COPY . .
RUN npm run build

### STAGE 2: Run ###
FROM nginx:1.18.0-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist/aston-villa-app /usr/share/nginx/html
# docker build
# sudo docker build -t jos99/bigdata-maps .

# docker run
# sudo docker run --name jacqueline-bidata-maps -p 8090:8080 jos99/bigdata-maps

