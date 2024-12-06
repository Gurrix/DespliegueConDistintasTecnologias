# Imagen base a utilizar
FROM node:12.18.1-slim

# Establecer el directorio de trabajo
WORKDIR /opt/microservices

# Copiar los ficheros package.json y ratings.js a la ruta /opt/microservices/ dentro del contenedor
COPY ./package.json .
COPY ./ratings.js .

# Especificar la variable de entorno
ENV SERVICE_VERSION=v1

# Instalar las dependencias
RUN npm install

# Exponer el puerto 9080
EXPOSE 9080

# Ejecutar el fichero ratings.js
CMD ["node", "ratings.js", "9080"]
