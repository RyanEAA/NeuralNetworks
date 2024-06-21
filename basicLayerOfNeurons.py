#layers are nothing more than a group of neurons
#each neuron in a layer will take the same input but each neuron has different weights and their own bias
#this leads to unique outputs

inputs = [1, 2, 3, 2.5]

weights1 = [0.2, 0.8, -0.5, 1]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5

outputs = [ #this is going to be outputting an array of outputs based on inputs, weights and biases
          
          # Neuron 1: is basically doing inputs[n]*weights1[n] + bias for first neuron
          inputs[0]*weights1[0] +
          inputs[1]*weights1[1] +
          inputs[2]*weights1[2] +
          inputs[3]*weights1[3] + bias1,
          
          # Neuron 2: is basically doing inputs[n]*weight2[n] + bias for second neuron
          inputs[0]*weights2[0] +
          inputs[1]*weights2[1] +
          inputs[2]*weights2[2] +
          inputs[3]*weights2[3] + bias2,
          
          # Neuron 3: is basically doing inputs[n]*weights3[n] + bias for third neuron
          inputs[0]*weights3[0] +
          inputs[1]*weights3[1] +
          inputs[2]*weights3[2] +
          inputs[3]*weights3[3] + bias3]


 
 
print(outputs)
