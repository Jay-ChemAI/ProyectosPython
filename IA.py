#Sí, es posible programar una IA en Python. Python es un lenguaje de programación muy popular en el campo de la inteligencia artificial debido 
# a su facilidad de uso y su amplia gama de bibliotecas y herramientas específicas para la IA.

#Para programar una IA en Python, necesitarás aprender algunos conceptos fundamentales de la inteligencia artificial, como el aprendizaje automático y el procesamiento del lenguaje natural, entre otros. 
# También deberás aprender a utilizar algunas de las bibliotecas y herramientas más populares de Python para la IA, como TensorFlow, PyTorch, Scikit-learn, Keras, entre otras.

#Existen muchos recursos disponibles en línea para aprender a programar IA en Python, como cursos en línea, tutoriales y libros. Si eres nuevo en la programación o en la IA,
#  es recomendable empezar con un curso o tutorial que te guíe a través de los conceptos básicos y te ayude a construir gradualmente tu comprensión y habilidades.

#Con el tiempo y la práctica, podrás crear tus propias aplicaciones de inteligencia artificial en Python y contribuir a este campo en constante evolución.


import tensorflow as tf
import numpy as np

celsius = np.array([-40, -10, 0 , 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype= float)

capa = tf.keras.layers.Dense(units = 1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print('Comenzando entrenamiento...')
historial = modelo.fit(celsius,fahrenheit, epochs=1000, verbose=False)
print('Modelo entrenado!')

resultado = modelo.predict([100.0])
print('el resultado es' + str(resultado) + 'fahrenheit')

import tensorflow as tf
import numpy as np

cl = np.array ([-40, -10, 0 , 8, 15, 22, 38], dtype=float)
fh = np.array ([-40, 14, 32, 46, 59, 72, 100], dtype=float)


cp = tf.keras.layers.Dense(units = 1, input_shape=[1])
md = tf.keras.Sequential([cp])


