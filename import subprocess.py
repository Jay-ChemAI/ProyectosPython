import subprocess
import time

# Ruta del archivo de código que deseas iniciar automáticamente
archivo_codigo = 'C:/Users/javie/Desktop/Python/#BOTS.py'

# Tiempo de espera en segundos
tiempo_espera = 30

while True:
    # Inicia el código
    proceso = subprocess.Popen(['python', archivo_codigo])

    # Espera el tiempo definido
    time.sleep(tiempo_espera)

    # Cierra el código
    proceso.kill()

    # Espera un tiempo adicional
    time.sleep(5)