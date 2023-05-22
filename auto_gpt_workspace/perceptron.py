# Code for building a perceptron neural network

import numpy as np


class Perceptron:
    def __init__(self, learning_rate=0.01, n_iters=1000):
        '''
        Initializes the Perceptron class.
        
        Parameters:
        learning_rate (float): The learning rate for the perceptron.
        n_iters (int): The number of iterations for the perceptron.
        '''
        self.lr = learning_rate
        self.n_iters = n_iters
        self.activation_func = self._unit_step_func
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        '''
        Fits the Perceptron model to the training data.
        
        Parameters:
        X (numpy array): The training data.
        y (numpy array): The target labels.
        '''
        n_samples, n_features = X.shape

        # init parameters
        self.weights = np.zeros(n_features)
        self.bias = 0

        y_ = np.array([1 if i > 0 else 0 for i in y])

        # gradient descent
        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation_func(linear_output)

                # Perceptron update rule
                update = self.lr * (y_[idx] - y_predicted)

                self.weights += update * x_i
                self.bias += update

    def predict(self, X):
        '''
        Predicts the target labels for the input data.
        
        Parameters:
        X (numpy array): The input data.
        
        Returns:
        y_predicted (numpy array): The predicted target labels.
        '''
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self.activation_func(linear_output)
        return y_predicted

    def _unit_step_func(self, x):
        '''
        The activation function for the perceptron.
        
        Parameters:
        x (float): The input value.
        
        Returns:
        1 or 0 (int): The output value of the activation function.
        '''
        return np.where(x >= 0, 1, 0)


if __name__ == '__main__':
    X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    y = np.array([0, 1, 1])

    perceptron = Perceptron()
    perceptron.fit(X, y)

    test_input = np.array([[1, 4, 7]])
    print(perceptron.predict(test_input))