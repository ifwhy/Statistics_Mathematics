import numpy as np
import matplotlib.pyplot as plt
import os
os.system('cls')

# 1/ Membuat Data
def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)
    y = amplitudo*np.sin(2*frekuensi*t+np.deg2rad(theta))
    return t, y

# 2. Membuat Plot
t1, y1 = sinusGenerator(1,1,4,0)

plt.plot(t1, y1)
# Setting axis
plt.xlim(0, 4)
plt.ylim(-2, 2)

# 3. Menampilkan Plot
plt.show()