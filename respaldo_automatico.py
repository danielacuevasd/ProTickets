import time
import shutil
import datetime
import os

# Rutas
origen = "logs"
destino = f"backups/backup_{datetime.date.today()}.zip"

# Crear carpeta de respaldos si no existe
os.makedirs("backups", exist_ok=True)

# Función de respaldo
def hacer_respaldo():
    print(f"Realizando respaldo: {destino}")
# Crear carpeta logs si no existe
os.makedirs("logs", exist_ok=True)

    shutil.make_archive(destino.replace(".zip", ""), "zip", origen)
    print("Respaldo completado.")

# Ejecutar respaldo cada 60 segundos (simulación de tarea automática)
while True:
    hacer_respaldo()
    print("Esperando 1 minuto para el próximo respaldo...")
    time.sleep(60)  # Espera de 60 segundos para pruebas
