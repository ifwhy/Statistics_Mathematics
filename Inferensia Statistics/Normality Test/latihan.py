import numpy as np
import scipy.stats as ss
import pandas as pd

df = pd.read_csv('../../data_stat.csv')
data = df['Duration']
stat, p_value = ss.shapiro(data)

# Uji Shapiro Wilk
print(f"Stat : {stat}, p_value = {p_value}")

alpha = 0.05
if p_value < alpha:
    print("Data Tidak Normal")
else:
    print("Data Normal")