#En este ejemplo, la red neuronal utiliza una capa oculta con 64 neuronas activadas por ReLU y una capa de salida con 10 neuronas activadas por softmax. 
# La función de pérdida utilizada es la entropía cruzada categórica y el optimizador es Adam. La red neuronal se entrena durante 10 épocas con un tamaño de lote de 128 
# y se evalúa en el conjunto de prueba.

from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import mnist
from keras.utils import to_categorical

# Cargar el conjunto de datos MNIST
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Preprocesar los datos
X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Crear la red neuronal
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(784,)))
model.add(Dense(10, activation='softmax'))

# Compilar la red neuronal
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar la red neuronal
model.fit(X_train, y_train, batch_size=128, epochs=10, validation_data=(X_test, y_test))

# Evaluar el rendimiento de la red neuronal
score = model.evaluate(X_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])