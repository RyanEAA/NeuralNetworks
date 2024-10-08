#representation of 1 neuron with 3 inputs
inputs = [1.0, 2.0 , 3.0 , 2.5]

weights= [0.2, 0.8, -0.5, 1.0]

#bias is an inheretly associated with inputs in contrast with weights
bias = 2

#calculated output based on inputs and weights and bias
output =  (inputs[0]*weights[0] + 
          inputs[1]*weights[1] +
          inputs[2]*weights[2] +
          inputs[3]*weights[3]+ bias)

print(output)