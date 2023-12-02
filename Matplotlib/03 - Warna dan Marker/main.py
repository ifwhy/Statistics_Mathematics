import numpy as np
import matplotlib.pyplot as plt
"""
    1. Membuat Data
    2. Membuat Plot
    3. Menampilkan Plot
"""

# 1. Membuat Data
def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)
    y = amplitudo*np.sin(2*frekuensi*t+np.deg2rad(theta))
    return t, y

# 2. Membuat Plot
t1, y1 = sinusGenerator(1,1,4,0)
plt.plot(t1, y1)

t2, y2 = sinusGenerator(1,1,4,30)
plt.plot(t2,y2, 'g') # warha hijau

t3, y3 = sinusGenerator(1,1,4,60)
plt.plot(t3, y3, 'b--') # menjadi strip jika --

t4, y4 = sinusGenerator(1,1,4,60)
plt.plot(t4, y4, 'b-o') # ada markernya

# 3. Menampilkan Plot
plt.show()