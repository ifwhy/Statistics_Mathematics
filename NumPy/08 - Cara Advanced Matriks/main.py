import numpy as np

# Membuat matriks dengan tipe data tertentu
a = np.array(([1,2,3], [3,4,5]), dtype= float)
# print(a[a%2 == 0])
# Membuat array dengan menggunakan function
def kuadrat(baris, kolom):
    return kolom**2
def jumlah(baris, kolom):
    return baris + kolom

b = np.array(([0,1,2,3,4,5,6,7,8,9]))
c = np.fromfunction(kuadrat, [1,10], dtype= int)
d = np.fromfunction(jumlah, [4,4], dtype= float)

# Membuat matriks dengan iterasi
iterable = (x**2 for x in range(5))
e = np.fromiter(iterable, dtype= int)

# Multitype array
dtipe = [('nama', 'S5255'), ('tinggi', int)]

data = [('ucup', 150), ('otong', 160), ('Mario', 180)]
e = np.array(data, dtype = dtipe)

x = np.empty([2, 2])
print(x)
y = [1, 2, 3]
z = np.array(y)
print(z)