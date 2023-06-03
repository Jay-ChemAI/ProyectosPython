#TIMER
#POMODORO

import time
from tensorflow import keras
import numpy as np


def temporizador(segundos):
    while segundos:
        minutos, seg = divmod(segundos, 60)
        tiempo = '{:02d}:{:02d}'.format(minutos, seg)
        print(tiempo, end='\r')
        time.sleep(1)
        segundos -= 1
    print('¡Tiempo finalizado!')

# Ejemplo de uso: Temporizador de 5 minutos
temporizador(5)