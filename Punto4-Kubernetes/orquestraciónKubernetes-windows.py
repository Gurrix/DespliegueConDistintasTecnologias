import os
import subprocess


# Cambiar al directorio adecuado
os.chdir("./practica_creativa2/bookinfo/src/reviews")

# Ejecutar el primer comando
subprocess.call('docker run --rm -u root -v "{$PWD}":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build', shell=True)

# Volver al directorio anterior
os.chdir("..")

# Construir la imagen de Docker con docker-compose
subprocess.call("docker-compose build", shell=True)

#Volver al directorio practica_creativa2
os.chdir("..")
os.chdir("..")
# Aplicar los archivos YAML con kubectl
subprocess.call("kubectl apply -f ./bookinfo/platform/kube/productpage.yaml", shell=True)
subprocess.call("kubectl apply -f ./bookinfo/platform/kube/details.yaml", shell=True)
subprocess.call("kubectl apply -f ./bookinfo/platform/kube/ratings.yaml", shell=True)
subprocess.call("kubectl apply -f ./bookinfo/platform/kube/reviews-svc.yaml", shell=True)
subprocess.call("kubectl apply -f ./bookinfo/platform/kube/reviews-v3-deployment.yaml", shell=True)
