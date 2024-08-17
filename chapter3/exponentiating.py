import math

# values from a previous ouput 
layer_ouputs = [4.8, 1.21, 2.385]

# eulers' constant
E = math.e

exp_values = []
for output in layer_ouputs:
    exp_values.append(E ** output)
print("Exponentiated Values")
print(exp_values)

# now normalize values
norm_base = sum(exp_values) # sums all values
norm_values = []

for value in exp_values:
    norm_values.append(value / norm_base)
    
print('Normalized exponentiated values:')
print(norm_values)
print('Sum of normalized values:', sum(norm_values))