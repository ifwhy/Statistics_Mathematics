import numpy as np

# array python
a = [1,2,3,4,5]
b = [6,2,3,5,4]

# array numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,2,3,5,4])

# ELEMENTWISE operation
# Penjumlahan
hasil = a+b
hasil = anp + bnp

# Pengurangan
hasil = anp - bnp

# Perkalian
hasil = anp*bnp

# Pembagian
hasil = anp/bnp

# Eksponensial
hasil = anp**2

# Multidimensi array numpy
c = np.array([(1,2,3), (4,5,6)])
d = np.array([(7,5,2), (5,5,2)])

# Penjumlahan
hasil = c+d

# Perkalian
hasil = c*d

print(hasil)