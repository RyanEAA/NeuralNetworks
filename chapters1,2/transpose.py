import numpy as np

a = [1, 2, 3]

# axis = 0 results in a row array
print("row array")
print(np.expand_dims(np.array(a), axis = 0))

# axis = 1 results in a col array
print("\ncol array")
print(np.expand_dims(np.array(a), axis = 1))

