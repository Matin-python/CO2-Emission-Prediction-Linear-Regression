import numpy as np
import pandas as pd
import seaborn as sns

from sklearn import linear_model
import sklearn.metrics as sm
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt


df = pd.read_csv('co2.csv')

sns.countplot (x= 'out1', data= df)

plt.subplots(figsize = (6, 6))
sns.heatmap(df.corr(), annot= True)
plt.show()

x = df.drop(["out1"], axis=1) 
y = df.out1

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

reg_linear = linear_model.LinearRegression()
reg_linear.fit(x_train, y_train)

out_pred = reg_linear.predict(x_test)

err = np.abs(y_test - out_pred) / y_test * 100
err_max = err.max()
err_min = err.min()
err_mean = err.mean()

plt.scatter(x_test.engine, y_test, color= 'blue')
plt.xlabel('1 = Engine')
plt.ylabel('CO2 production')
plt.title('CO2 \'Engine\'')
plt.show()


plt.scatter(x_test.cylandr, y_test, color= 'red')
plt.xlabel('2 = cylandr')
plt.ylabel('CO2 production')
plt.title('CO2 \'cylandr\'')
plt.show()


plt.scatter(x_test.fuelcomb, y_test, color= 'green')
plt.xlabel('3 = Fuelcomb')
plt.ylabel('CO2 production')
plt.title('CO2 \'Fuelcomb\'')
plt.show()


p206 = np.array([[1.36, 4, 5]])
co2 = reg_linear.predict(p206)
print("-"*50)
print("Peugeot 206 co2_emission_prediction= ", co2, "g/km")
print("Peugeot 206 Real co2_emission= 149 g/km")
print("-"*50)

print("err mean= ", err_mean)
print("sm.mean_absolute_error= ", sm.mean_absolute_error(y_test, out_pred))
print("sm.mean_squared_error= ", sm.mean_squared_error(y_test, out_pred))

plt.figure(figsize=(6,6))
plt.scatter(y_test, out_pred)
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    'r--'
)

plt.xlabel("Actual CO₂ Emission")
plt.ylabel("Predicted CO₂ Emission")
plt.title("Actual vs Predicted")
plt.show()
