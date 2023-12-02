import numpy as np

a = np.array(([1,2], [2,8]))
print(a)

# Mencari invers matriks
inversA = np.linalg.inv(a)
print(inversA) 
# print(np.dot(a, np.linalg.inv(a)))

# Mencari determinan matriks
detA = np.linalg.det(a)
print(detA)