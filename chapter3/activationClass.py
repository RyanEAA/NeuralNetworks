
import numpy as np

# ReLU activation
class Activation_ReLU:
    
    #forward pass
    def forward(self, inputs):
        # calculate output values from input
        self.output = np.maximum(0, inputs)