
import numpy as np
import nnfs
import matplotlib.pyplot as plt
from nnfs.datasets import spiral_data
from denseLayer import Layer_Dense
from activationClass import Activation_ReLU


# sets the seed as zero
nnfs.init()

# create dataset
X, y =  spiral_data(samples = 100, classes = 3)

# create dense layer with 2 inputs and 3 output values
dense1 = Layer_Dense(2, 3)

# create ReLU activation 
activation1 = Activation_ReLU()


# make a forward pass of our training data through this layer
dense1.forward(X)

activation1.forward(dense1.output)

print(activation1.output[:5])



