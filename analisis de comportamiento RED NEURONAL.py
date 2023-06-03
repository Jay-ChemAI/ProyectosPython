import numpy as np
from keras.models import Sequential
from keras.layers import Dense

#Datos de entrada
X= np.array[([0,0], [0,1], [1,0], [1,1])]
#Etiquetas correspondientes a los comportamientos
y = np.array([0,1,1,0])

# Inicializar el modelo
model = Sequential()
# Agregar una capa oculta con 2 neuronas y función de activación relu
model.add(Dense(2, input_dim=2, activation='relu'))
# Agregar una capa de salida con 1 neurona y función de activación sigmoidal
model.add(Dense(1, activation='sigmoid'))

# Compilar el modelo con la función de pérdida y optimizador adecuados
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Entrenar el modelo con los datos de entrada y etiquetas correspondientes
model.fit(X, y, epochs=100, batch_size=1)
# Realizar predicciones para nuevos datos
new_data = np.array([[0, 0], [0, 1]])
predictions = model.predict(new_data)
print(predictions)
