import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,11,1)
y = 2*x+3
print(x)
print(y)

plt.plot(x, y)
plt.show()

# Plotting Lingkaran
jari2 = 5
sudut = np.arange(0, 2*np.pi +1, 0.1)
x1 = np.cos(sudut)
y1 = np.sin(sudut)

plt.plot(x1, y1)
plt.show()