import numpy as np

# 2x + 3y = 23
# x + 2y = 14

konstanta = np.array(([23], [14]))
koefisien = np.array(([2, 3], [1, 2]))

variabel = np.dot(np.linalg.inv(koefisien), konstanta)
variabel = np.linalg.solve(koefisien, konstanta)
print(variabel)