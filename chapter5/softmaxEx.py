import numpy as np

softmax_outputs = np.array([[0.7, 0.1, 0.2],
                   [0.1, 0.5, 0.4],
                   [0.02, 0.9, 0.08]])

class_targets = [0, 1, 1]

for targ_idx, distribution in zip(class_targets, softmax_outputs):
    print(distribution[targ_idx])
    
# simplified way of doing the same
print(softmax_outputs[[0, 1, 2], class_targets])


print(range(len(softmax_outputs)), class_targets)


print("\n Here's the negative log of the value giving us the loss value")
neg_log = -np.log(softmax_outputs[range(len(softmax_outputs)), class_targets])
print(neg_log)

print("\nAverage Mean:")
average_loss = np.mean(neg_log)
print(average_loss)