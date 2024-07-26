a = [1, 2, 3]
b = [2, 3, 4]

result = 0

for i in range(len(a)):
    result += a[i]*b[i]
    
print(result)