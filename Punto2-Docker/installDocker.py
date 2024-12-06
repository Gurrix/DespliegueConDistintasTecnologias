import subprocess

# Instalar Docker
subprocess.run("sudo apt install -y docker.io", shell=True)

# Instalar Docker Compose
subprocess.run("sudo apt install -y docker-compose", shell=True)
