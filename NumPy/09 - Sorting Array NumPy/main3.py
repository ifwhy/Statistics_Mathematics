import numpy as np

dtipe = [('nama', 'S10'), ('tinggi', int)]
data = [('udup', 150), ('Otong', 170), ('Mario', 50)]
a = np.array(data, dtype = dtipe)

print(np.sort(a, order='nama'))