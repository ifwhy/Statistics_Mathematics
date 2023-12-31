import numpy as np
import scipy.stats as ss
import pandas as pd

data = np.random.normal(loc=80, scale=10, size=45)
df = pd.DataFrame({'DATA :' : data})
print(df.to_string)

# Uji Shapiro Wilk
stat, p_value = ss.shapiro(data)
print(f"Shapiro Wilk test : stat = {stat}, p_value = {p_value}")

# Normality Test using Kolmogorov Smirnov test
stat, p_value = ss.kstest(data, 'norm')
print(f"KS test : stat = {stat}, p_value = {p_value}")

# Uji Anderson-Darling
result = ss.anderson(data)
print(f"Shapiro Wilk test : stat = {result.statistic}, significance = {result.significance_level}, critical value = {result.critical_values}")

alpha = 0.05
if p_value < alpha:
    print("Data Tidak Normal")
else:
    print("Data Normal")
