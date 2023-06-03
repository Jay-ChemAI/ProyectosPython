#Este ejemplo de red neuronal es un clasificador binario que aprende a realizar la función lógica XOR. 
#Aunque es un ejemplo sencillo, demuestra los pasos básicos para crear y entrenar una red neuronal en Python utilizando la biblioteca Keras de TensorFlow.
import numpy as np
from tensorflow import keras

# Datos de entrenamiento
#crea una matriz de cuatro filas y dos columnas utilizando la biblioteca NumPy de Python. 
# Cada fila de la matriz representa un ejemplo de entrenamiento y cada columna representa una característica o variable de entrada.
#array hace que el arreglo de números sea en matrices o vectores
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Definición del modelo de red neuronal
# define una red neuronal de dos capas utilizando la biblioteca Keras de TensorFlow.
# En la primera línea, se define un objeto de modelo llamado model utilizando la clase Sequential de Keras, 
# que permite construir redes neuronales secuenciales. Dentro de los corchetes, se definen las capas de la red neuronal.
model = keras.Sequential([
    keras.layers.Dense(4, input_shape=(2,), activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

# Compilación del modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenamiento del modelo
model.fit(X, y, epochs=1000, batch_size=4)

# Predicciones
predictions = model.predict(X)

# Impresión de las predicciones
print(predictions)


test = model.predict([[0, 1], [0, 1], [1, 1], [1, 1]])
print(str(test))