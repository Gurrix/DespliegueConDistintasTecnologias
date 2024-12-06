# Imagen base a utilizar
FROM ruby:2.7.1-slim

# Establecer el directorio de trabajo
WORKDIR /opt/microservices

# Copiar el fichero details.rb en la ruta /opt/microservices/ dentro del contenedor
COPY ./details.rb .

# Especificar las dos variables de entorno
ENV SERVICE_VERSION=v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE=true

# Exponer el puerto 9080
EXPOSE 9080

# Ejecutar el fichero details.rb
CMD ["ruby" , "details.rb" , "9080"]
