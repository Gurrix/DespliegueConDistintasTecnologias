# Usar una imagen base de Python
FROM python:3.7.7-slim

# Actualizar el índice de paquetes e instalar dependencias
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y python3-pip

# Establecer la variable de entorno GROUPO_NUMERO
ENV GRUPO_NUMERO="Grupo 35"

# Establecer el directorio de trabajo
WORKDIR /punto2

# Copiar los archivos necesarios
COPY ./practica_creativa2/bookinfo/src/productpage .

# Instalar las dependencias de la aplicación
RUN pip3 install --no-cache-dir -r requirements.txt

# Exponer el puerto 9080
EXPOSE 9080

# Comando para iniciar la aplicación
CMD ["python3", "productpage_monolith.py", "9080"]