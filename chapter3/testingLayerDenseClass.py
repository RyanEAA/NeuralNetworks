import numpy as np
import nnfs
import matplotlib.pyplot as plt
from nnfs.datasets import spiral_data
from denseLayer import Layer_Dense
# creates dataset
x, y = spiral_data(samples = 100, classes = 3)


# creates dense layer with 2 input features and 3 output values
dense1 = Layer_Dense(2, 3)

# perform a forward pass of our training data 
dense1.forward(x)

# prints output of of the forward pass  
print(dense1.output[:5])


