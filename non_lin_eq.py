import numpy as np
import pandas as pd
import statsmodels.api as sm


file_path = "XOM_historical_data_2018-03-09_2024-03-10.csv"
historical_data = pd.read_csv(file_path)

if not historical_data.empty:
    print("csv file read successfully")
    print(historical_data.head())
else:
    print("An error occurred!!!")

""" time index can be based on the sequential order of observations """
historical_data['t'] = range(1, len(historical_data) + 1)

historical_data["Price"] = historical_data["Adj Close"]
print("Historical data")
print(historical_data.tail())

""" Transform the data by taking natural logarithm of Price """
historical_data["Ln_Prices"] = np.log(historical_data["Price"])

""" Define the independent variable (time index) """
X = sm.add_constant(historical_data["t"])

""" Fit the linear regression model """
model = sm.OLS(historical_data['Ln_Prices'], X)
results = model.fit()

""" Print the regression results """
print(results.summary())
