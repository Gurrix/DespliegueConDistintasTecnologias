import os
import subprocess
from multiprocessing import Process
import re

def instalar_aplicacion_vm_google_cloud():

    # Clonar el repositorio
    subprocess.run(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git'])

    # Instalar dependencias
    subprocess.run(['sudo', 'apt-get', 'update'])
    subprocess.run(['sudo', 'apt', 'install', 'python3-pip'])
    subprocess.run(['pip3', 'install', '-r', 'practica_creativa2/bookinfo/src/productpage/requirements.txt'])

    # Variables de configuración
    os.environ['GRUPO_NUMERO'] = 'Grupo35'
    puerto_deseado_1 = 9080  # Primer puerto deseado para la aplicación
    puerto_deseado_2 = 9090  # Segundo puerto deseado para la aplicación

    # Inspeccionar el código y modificar el título
    path_codigo = 'practica_creativa2/bookinfo/src/productpage/productpage_monolith.py'
    modificar_script(path_codigo)

    # Obtener la dirección IP externa (subprocess.check_ipExternaBytes te devuelve el resultado en Bytes)
    ipExternaBytes = subprocess.check_output("curl ifconfig.me", shell=True)
    # Lo convertimos en un string:
    ipExterna = ipExternaBytes.decode('utf-8')
    # Direcciones  para acceder a la web
    print("Go to http://"+ipExterna+":9080/productpage")
    print("Go to http://"+ipExterna+":9090/productpage")

    # Arrancar la aplicación en los puertos deseados en paralelo
    p1 = Process(target=arrancar_aplicacion, args=(path_codigo, puerto_deseado_1))
    p2 = Process(target=arrancar_aplicacion, args=(path_codigo, puerto_deseado_2))

    # Iniciar los procesos
    p1.start()
    p2.start()

    # Esperar a que ambos procesos terminen
    p1.join()
    p2.join()

def arrancar_aplicacion(path_codigo, puerto):
    subprocess.run(['python3', path_codigo, str(puerto)])

def modificar_script(file_path):
    # Lee el contenido del archivo
    with open(file_path, 'r') as file:
        content = file.read()

    # Encuentra la función getProducts y modifica sus valores
    pattern = r"(def getProducts\(\):[\s\S]*?])"
    replacement = r"group_number = os.getenv('GRUPO_NUMERO')\nprint(group_number)\n\1"

    modified_content = re.sub(pattern, replacement, content, flags=re.MULTILINE)

    # Modifica las líneas dentro de la función getProducts
    modified_content = re.sub(r"'title': '(.*?)',", r"'title': group_number + ' - ' + '\1',", modified_content)

    # Escribe el contenido modificado de vuelta al archivo
    with open(file_path, 'w') as file:
        file.write(modified_content)

if __name__ == "__main__":
    instalar_aplicacion_vm_google_cloud()