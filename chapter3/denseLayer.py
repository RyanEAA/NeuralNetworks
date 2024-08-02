
import numpy as np
import nnfs
from nnfs.datasets import spiral_data
nnfs.init()

# creating a dense layer class of neural networks
# this means that every neuron is connected every neuron in the following layer
class Layer_Dense:
    
    # Layer initialization
    def __init__(self, n_inputs, n_neurons):
        # initialize weights and biases
        
        # weights are being set to random
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        
        # biases are being set to zero
        self.biases = np.zeros((1, n_neurons))
    
    
    # Forward pass
    def forward(self, inputs):
        # calculate output values from inputs, weights and biases
        self.output = np.dot(inputs, self.weights) + self.biases
