import numpy as np
import scipy.stats as ss
import pandas as pd

a = np.array([2, 3, 1, 5, 6, 10, 12, 14, 23, 14])
b = np.linspace(0, 100, 200)

# Sum
sum = np.sum(a)
print("Sum of a is ", sum)

# Average
average = np.average(a)
print("Average of a is ", average)

# Median (Q2)
median = np.median(a)
print("Median of a is ", median)

# Mode
mode = ss.mode(a)
print("Mode of a is", mode)

# Standard Deviation
std = np.std(a)
print("Standard Deviation of a is ", std)

# variance
var1 = std**2
var2 = np.var(a)
print("Variance of a is ", var1.round(2))
print("Variance of a is ", var2)

# Percentile
percentile = np.percentile(a, 75)
print('Percentile 10 of a is ', percentile)

# Statistik deskriptif dari data .csv
df = pd.read_csv('../data_stat.csv')
missing_value = df.isnull().sum()
print("Missing Value : ")
print(missing_value)
print()
df['Calories'].fillna(df['Calories'].mean(), inplace=True)
print(df.describe().round(2))

# Data standar deviasi, ragam, persentil
print(f"\nStandar Deviasi Kolom Duration  : {np.std(df['Duration']).round(3)}")
print(f"Ragam kolom Pulse               : {np.var(df['Pulse']).round(3)}")
print(f"Persentil kolom Calories        : {np.percentile(df['Calories'].round(3), 75)}")