# we will now be implementing the calculation of outputs using a for loop

#three neurons

#each neuron has 4 inputs
inputs = [1, 2, 3, 2.5]

# lists of weights for inputs ex. weights[n] for inputs[n]


weights = [[0.2, 0.8, -0.5, 1],
             [0.5, -0.91, 0.26, -0.5],
             [-0.26, -0.27, 0.17, 0.87]]


#biases for the three neurons
biases = [2, 3, 0.5] 

#output of current layer
layer_outputs = []
my_layer_output_attempt = []


#my attempt of understanding the programming logic behind the math
for weight_list, bias in zip(weights, biases):
    output_neuron = 0
    
    for weight, input in zip(weight_list, inputs):
        output_neuron += weight*input
        
    output_neuron+= bias
    my_layer_output_attempt.append(output_neuron)
    
print("my output neuron attemt: ", my_layer_output_attempt)


neuron_num = 0 # keep track of which neurons

for neuron_weights, neuron_bias in zip(weights, biases): #goes through the weights lists and biases list
    # zeroed output of given neuron
    neuron_ouput=0
    # for each input and weight to the neuron
    
    print("neuron num", neuron_num)
    for n_input, weight in zip(inputs, neuron_weights): #goes through the values in the neuron weights and inputs
        # multiply this input by associated weight
        # and add to the neuron's output variable
        neuron_ouput += n_input*weight
        print("input ",n_input, ". neuron weight ", weight)
        
    neuron_ouput += neuron_bias
    neuron_num+=1
    layer_outputs.append(neuron_ouput)
    print("\n")
    
print(layer_outputs)
        