import time
import shutil
import os
import datetime

# Crear carpetas si no existen
os.makedirs("logs", exist_ok=True)
os.makedirs("backups", exist_ok=True)

# Ruta de origen (carpeta que se va a respaldar)
origen = "logs"

# Bucle para respaldar cada minuto (60 segundos)
while True:
    # Crear nombre del archivo de respaldo con fecha
    fecha = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_respaldo = f"backups/respaldo_{fecha}"

    # Crear respaldo comprimido
    shutil.make_archive(nombre_respaldo, "zip", origen)
    print(f"✅ Respaldo creado: {nombre_respaldo}.zip")

    # Esperar 60 segundos antes del próximo respaldo
    time.sleep(60)
