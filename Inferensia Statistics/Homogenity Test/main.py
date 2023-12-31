import numpy as np
import scipy.stats as ss
import pandas as pd

df = pd.read_csv('../../data_stat.csv')

missing_value = df.isnull().sum()
print("Missing Value : ")
print(missing_value)

df['Calories'].fillna(df['Pulse'].mean(), inplace=True)

data1 = df['Pulse']
data2 = df['Calories']

# Levene Test:Homogenity
stat, p_value = ss.levene(data1, data2)
print("Result of Levene Test")
print(f"Stat = {stat}, p_value = {p_value}")

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. Variances are significantly different.")
else:
    print("Fail to reject the null hypothesis. Variances are not significantly different.")