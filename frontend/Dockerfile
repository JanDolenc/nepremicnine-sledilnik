# Stage 1: Compile and Build Angular app

FROM node:18-alpine as build

WORKDIR /usr/local/app

COPY package.json package-lock.json ./

RUN npm install

COPY ./ /usr/local/app/

RUN npm run build


# Stage 2: Serve the app with Nginx server

FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf

COPY --from=build /usr/local/app/dist/frontend/browser /usr/share/nginx/html

EXPOSE 80
