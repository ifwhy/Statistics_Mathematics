import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data_stat.csv')

# Terdapat kekosongan data di kolom Calories sebanyak 5 data dan akan diisi dengan nilai average
df['Calories'].fillna(df['Calories'].mean(), inplace=True)

# Data
data_x = np.array(df['Duration'])
data_y = np.array(df['Calories'])

# Plotting ke dalam scatter plot
df.plot(kind='scatter', x='Duration', y='Calories', title='Regresi Linear Sederhana', color='b')

# Regresi Linear 
data_x = data_x.reshape(-1, 1)
model = LinearRegression()
model.fit(data_x, data_y)
r_sq = model.score(data_x, data_y)
slope = model.coef_.round(3)
intercept = model.intercept_.round(3)

def garis_regresi(x):
    y = slope * x + intercept
    return y
plt.plot(df['Duration'], garis_regresi(df['Duration']), color='r', label='Regresi Linear')
plt.legend()
plt.show()