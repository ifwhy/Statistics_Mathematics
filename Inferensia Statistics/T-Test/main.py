import pandas as pd
import scipy.stats as ss
import numpy as np

df = pd.read_csv('../../data_stat.csv')
data1 = df['Calories']
data2 = df['Duration']

missing_value = df.isnull().sum()
print("Missing value : ")
print(missing_value)
df['Calories'].fillna(df['Calories'].mean(), inplace=True)

# Uji Independent Sample T Test
stat, p_value = ss.ttest_ind(data1, data2)
print("\nHasil uji T Independen")
print(f"stat    : {stat.round(3)}")
print(f"p_value : {p_value.round(3)}")

alpha = 0.05
if p_value < alpha:
    print("H0 diterima, tidak ada perbedaan rata-rata antara data pertama dan kedua")
else:
    print("H0 ditolak, ada perbedaan rata-rata antara data pertama dan kedua")

# Uji Paired Sample T Test
stat, p_value = ss.ttest_rel(data1, data2)
print("\nHasil uji T berpasangan")
print(f"stat    : {stat.round(3)}")
print(f"p_value : {p_value.round(3)}")

alpha = 0.05
if p_value < alpha:
    print("H0 diterima, tidak ada perbedaan rata-rata antara data pertama dan kedua")
else:
    print("H0 ditolak, ada perbedaan rata-rata antara data pertama dan kedua")