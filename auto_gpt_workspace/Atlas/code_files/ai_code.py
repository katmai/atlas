# This is a sample Python code for implementing a simple neural network

import numpy as np

# Define the sigmoid function

def sigmoid(x, derivative=False):
    if derivative:
        return sigmoid(x) * (1 - sigmoid(x))
    else:
        return 1 / (1 + np.exp(-x))

# Define the neural network class

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.weights1 = np.random.randn(input_size, hidden_size)
        self.weights2 = np.random.randn(hidden_size, output_size)

    def forward(self, X):
        self.z = np.dot(X, self.weights1)
        self.z2 = sigmoid(self.z)
        self.z3 = np.dot(self.z2, self.weights2)
        o = sigmoid(self.z3)
        return o

# Test the neural network

X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
y = np.array([[0], [1], [1], [0]])
n = NeuralNetwork(3, 4, 1)
for i in range(10000):
    n.forward(X)
    n.error = y - n.z3
    n.delta3 = n.error * sigmoid(n.z3, derivative=True)
    n.weights2 += np.dot(n.z2.T, n.delta3)
    n.delta2 = np.dot(n.delta3, n.weights2.T) * sigmoid(n.z2, derivative=True)
    n.weights1 += np.dot(X.T, n.delta2)
print(n.forward(X))
