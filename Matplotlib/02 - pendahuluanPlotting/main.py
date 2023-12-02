import matplotlib.pyplot as plt
import numpy as np

#  Membuat data
x = np.array(([1,2,3,4,5]))
y1 = np.array(([1,4,9,16,25]))
y2 = np.array([5,4,3,2,1])
#  Membuat plot
plt.plot(x, y1)
plt.plot(x, y2)

#  Menampilkan plot 
plt.show()