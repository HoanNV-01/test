

import numpy as np

n = int(input("Enter n: "))

a = np.random.randint(1, 100, n)
b = np.random.randint(1, 100, n)

print("A = ", a)
print("B = ", b)

print("A + B = ", a + b)
print("A - B = ", a - b)    
print("A dot B = ", np.dot(a, b))
print("A x B = ", np.cross(a, b))
#Chuẩn hóa (normalize) vector a
print("Normalize A = ", a / np.linalg.norm(a))