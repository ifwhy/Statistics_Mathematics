import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy import stats

df = pd.read_csv('../../data_stat.csv')
df['Calories'].fillna(df['Calories'].mean(), inplace=True)
data1 = np.array(df['Duration']).reshape(-1, 1)
data2 = df['Calories']

model = LinearRegression()
model.fit(data1, data2)
r_sq = model.score(data1, data2)
print("Koefisien Determinasi ", r_sq.round(3))

intersep = model.intercept_
slope = model.coef_
print(f"Persamaan regresi : {slope.round(3)}x + {intersep.round(3)}")

df.plot(kind='scatter', x='Duration', y='Calories')

def garisRegresi(x):
    return slope * x + intersep

plt.plot(data1, garisRegresi(data1), color='r')
plt.title("Duration vs Calories")
plt.show()