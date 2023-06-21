import numpy as np

class NeuralNetwork:
    def __init__(self, input_dim, hidden_dim, output_dim):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.W1 = np.random.randn(self.input_dim, self.hidden_dim)
        self.W2 = np.random.randn(self.hidden_dim, self.output_dim)

    def forward(self, X):
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        y_hat = self.sigmoid(self.z3)
        return y_hat

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def sigmoid_prime(self, z):
        return self.sigmoid(z) * (1 - self.sigmoid(z))

    def cost_function(self, X, y):
        self.y_hat = self.forward(X)
        J = 0.5 * np.sum((y - self.y_hat) ** 2)
        return J

    def cost_function_prime(self, X, y):
        self.y_hat = self.forward(X)
        delta3 = np.multiply(-(y - self.y_hat), self.sigmoid_prime(self.z3))
        dJdW2 = np.dot(self.a2.T, delta3)
        delta2 = np.dot(delta3, self.W2.T) * self.sigmoid_prime(self.z2)
        dJdW1 = np.dot(X.T, delta2)
        return dJdW1, dJdW2


def test_neural_network():
    # Define the training set
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    # Create the neural network
    n = NeuralNetwork(2, 3, 1)

    # Train the neural network
    n.train(X, y, iterations=10000, learning_rate=0.1, reg_lambda=0.01)

    # Test the neural network
    assert np.allclose(n.predict(X), y, atol=1e-2, rtol=1e-2)

if __name__ == '__main__':
    test_neural_network()