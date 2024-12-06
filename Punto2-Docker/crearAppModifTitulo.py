import subprocess
from multiprocessing import Process
import re

def instalar_aplicacion_vm_google_cloud():

    # Clonar el repositorio
    subprocess.run(['git', 'clone', 'https://github.com/CDPS-ETSIT/practica_creativa2.git'])

    # Inspeccionar el código y modificar el título
    path_codigo = 'practica_creativa2/bookinfo/src/productpage/productpage_monolith.py'
    modificar_script(path_codigo)

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