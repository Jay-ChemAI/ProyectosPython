import numpy as np

# definir la función sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# definir la clase de la red neuronal
class NeuralNetwork:
    
    def __init__(self, input_size, hidden_size, output_size):
        # inicializar los pesos aleatoriamente
        self.weights1 = np.random.randn(input_size, hidden_size)
        self.weights2 = np.random.randn(hidden_size, output_size)
    
    def forward(self, X):
        # calcular la salida de la red neuronal
        self.hidden = sigmoid(np.dot(X, self.weights1))
        self.output = sigmoid(np.dot(self.hidden, self.weights2))
    
    def backward(self, X, y, learning_rate):
        # calcular el error de la red neuronal
        output_error = y - self.output
        output_delta = output_error * (self.output * (1 - self.output))
        
        # retropropagar el error a la capa oculta
        hidden_error = output_delta.dot(self.weights2.T)
        hidden_delta = hidden_error * (self.hidden * (1 - self.hidden))
        
        # ajustar los pesos
        self.weights2 += self.hidden.T.dot(output_delta) * learning_rate
        self.weights1 += X.T.dot(hidden_delta) * learning_rate

# definir los datos de entrada y salida
X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
y = np.array([[0], [1], [1], [0]])

# crear la red neuronal
nn = NeuralNetwork(3, 4, 1)

# entrenar la red neuronal
for i in range(100000):
    nn.forward(X)
    nn.backward(X, y, 0.1)

# probar la red neuronal
test = np.array([[0, 0, 1]])
nn.forward(test)
print(nn.output)