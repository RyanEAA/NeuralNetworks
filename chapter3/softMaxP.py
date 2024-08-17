from softmax import Activation_Softmax

softmax = Activation_Softmax()
softmax.forward([[1, 2, 3]])
print(softmax.output)
