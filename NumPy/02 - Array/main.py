import numpy as np

# membuat vector
a = np.array([1,2,3,4,5])
b = np.array([1.5, 2.5, 5.5])

# Membuat vektor dengan range
c = np.arange(1,10,2)

# membuat linespace
d = np.linspace(1,10,4)

# Array multidimensi (matriks)
e = np.array([(1,2,3), (4,5,6)])

# Matriks dengan semua elemen 0
f = np.zeros(5)
g = np.zeros((5,5))

# Matriks dengan semua elemen 1
h = np.ones(5)
i = np.ones((2,2))

# Matriks identitas
j = np.identity(5)
j2 = np.eye(5)

# Arrange and diagonal arrange
k = np.arange(4)
k1 = np.diag(np.arange(4))
# display
print(k)
print(k1)