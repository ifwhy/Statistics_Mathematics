import numpy as np

a = np.arange(10)**2

print(a)

# Mengambil nilai
print("Elemen ke-1 dari a adalah ", a[0])
print("Elemen ke-1 dari a adalah ", a[6]) #elemen ke-7
print("Elemen terakhir dari a adalah ", a[-1])

# Slicing
print("Elemen dari 1-6 adalah ", a[0:6]) #[start, end-1]

print("elemen dari 4 terakhir adalah ", a[3:]) #dari elemen ke-3 sampai akhir
print("Elemen dari awal sampai 5 adalah ", a[:5])

for i in a:
    print("value : ", i)

n = np.linspace(1, 2, 5)
print(n)

x = np.logspace(-2, 2, 5)
print(x)