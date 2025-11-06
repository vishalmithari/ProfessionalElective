import numpy as np


a = np.array([1, 2, 3, 4, 5])

print("Original array:", a)

print("Square root:", np.sqrt(a))


print("Exponential:", np.exp(a))


print("Sine:", np.sin(a))


b = np.array([10, 20, 30, 40, 50])
print("Addition:", np.add(a, b))


print("Multiplication:", np.multiply(a, b))



def add_numbers(x, y):
    return x + y


ufunc_add = np.frompyfunc(add_numbers, 2, 1)

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

result = ufunc_add(a, b)


print("UFunc Add Result:", result)
