import numpy as np

a = np.array([1,2,3])
b = np.array([3,4,5])

# Perkalian dot
dot = np.dot(a,b)

# Perkalian cross
cross1 = np.cross(a, b)
cross2 = np.cross(b,a)
print(cross2)