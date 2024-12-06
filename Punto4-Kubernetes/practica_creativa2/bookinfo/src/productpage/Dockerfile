# Usar una imagen base de Python
FROM python:3.7.7-slim

# Establecer la variable de entorno GROUPO_NUMERO
ENV GROUP_NUMBER="Grupo 35"


RUN apt-get update
RUN apt-get install -y python3-pip
# Establecer el directorio de trabajo
WORKDIR /opt/microservices/

# Copiar los archivos necesarios
COPY . .

# Instalar las dependencias de la aplicación
RUN pip3 install -r requirements.txt

# Exponer el puerto 9080
EXPOSE 9080

# Comando para iniciar la aplicación
CMD ["python3" , "productpage.py" , "9080"]
