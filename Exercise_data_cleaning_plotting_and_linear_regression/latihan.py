import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv('data_corr.csv')
missing_value = df.isnull().sum()
print(f"Missing value : \n{missing_value}")

print(df.describe())
print("Analisis Korelasi Pearson : ")
print(df.corr())
df.plot(kind = 'scatter', x='Duration', y='Calories')

df['Calories'].fillna(df['Calories'].mean(), inplace=True)
X = df[['Duration']]
y = df[['Calories']]
df.dropna(subset=['Calories'], inplace=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xlabel('Duration')
plt.ylabel('Calories')
plt.title('Linear Regression')

plt.show()