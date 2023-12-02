import numpy as np

a = np.array(([1,2,3], [4,5,6]))
print("Matriks a dengan ukuran ", a.shape)
print(a)

# Transpose Matriks
print(a.transpose())
print(np.transpose(a))
print(a.T)

# Flatten array, vektor baris
print("Flatten matriks a adalah", a.ravel())
print("Flatten matriks a adalah", np.ravel(a))

# Reshapee matriks
print("Reshape matriks a adalah \n", a.reshape(3,2))

# Resize matriks
print("Resize matriks a adalah ")
a.resize(3,2)
print(a) #sama kayak reshape, tetapi mengubah a