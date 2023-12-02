import numpy as np

a = np.floor(np.random.randn(1,6)*10)

print(a)

# Mencari nilai max
print("Nilai Maksimum dari a adalah ", a.max())
print("Posisi max dari a adalah ", a.argmax())

# Mencari nilai min
print("Nilai Minimum dari a adalah ", a.min())
print("Posisi min dari a adalah ", a.argmin())

# Sorting dari paling kecil ke paling besar
print("Mengurutkan nilai a : ")
print(np.sort(a))
print(np.argsort(a))