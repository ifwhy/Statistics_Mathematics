import numpy as np
import matplotlib.pyplot as plt
import cycler as cy

def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)
    y = amplitudo*np.sin(2*frekuensi*t+np.deg2rad(theta))
    return t, y

amplitudo = 1
frekuensi = 1
theta = 0
tAkhir = 4

t1, y1 = sinusGenerator(amplitudo, frekuensi, tAkhir, theta)
plt.plot(t1, y1)

# Menambahkan title
Judul = "Grafik Sinusoidal\n"
Rumus = r'$\mathcal(Y)$'
plt.title(Judul + Rumus)

# Menambahkan label (harus di bawah plot)
plt.xlabel('Waktu (Detik)')
plt.ylabel('Magnitude (cm)')

plt.show()