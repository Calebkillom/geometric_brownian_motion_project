import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.stats.stattools import durbin_watson

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

""" Calculate the mean squared error (MSE) """
mse = results.mse_resid

""" Use MSE as an estimate of sigma^2 """
sigma_squared = mse
print("Estimate of sigma^2:", sigma_squared)


""" Save regression results to a text file """
with open("regression_results.txt", "w") as f:
    f.write(str(results.summary()))

"""
    Determining the coefficient of R2 of the proposed model.
    Plot the estimated trend against the time plot.
    Compare the Two graphs
"""
r_squared = results.rsquared
print("Coefficient of determination (R-squared):", r_squared)

plt.figure(figsize=(10, 6))
plt.plot(
    historical_data['t'], historical_data['Ln_Prices'], 'o-',
    label='Observed Data', markersize=2)
plt.plot(
    historical_data['t'], results.fittedvalues, color='red',
    label='Estimated Trend')
plt.xlabel('Time')
plt.ylabel('Natural Logarithm of Prices')
plt.title('Estimated Trend vs. Observed Data')
plt.legend()
plt.grid(True)
plt.show()

""" Save the plot as a PDF """
plt.savefig('trend_analysis_plot.pdf')

"""
    Check if there is any trace of autocorrelation
"""
""" Calculate Durbin-Watson statistic """
dw_statistic = durbin_watson(results.resid)
print("Durbin-Watson statistic:", dw_statistic)

""" Interpret the Durbin-Watson statistic """
if dw_statistic < 1:
    print("Positive autocorrelation is present.")
elif dw_statistic > 3:
    print("Negative autocorrelation is present.")
else:
    print(
        "No significant autocorrelation observed (residuals are independent).")