import numpy as np

a = np.array([(1,2), (3,4), (3,4)])
b = np.ones((2,2))

print(a)
print(b)

# Perkalian matriks secara matematika
c1 = np.dot(a,b)
c2 = a.dot(b)
print(c2)


print(a.ndim)
