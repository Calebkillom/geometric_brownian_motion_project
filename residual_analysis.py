import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


file_path =  "XOM_historical_data_2018-03-09_2024-03-10.csv"
historical_data = pd.read_csv(file_path)

""" Calculate the natural logarithm of the adjusted close values """
historical_data['Log_Adjusted_Close'] = np.log(historical_data["Adj Close"])

""" Shift the adjusted close values by one row """
historical_data["Prev_Log_Adj_Close"] =\
    historical_data["Log_Adjusted_Close"].shift(1)

"""
Calculate the difference between the natural logarithm
of the adjusted close values of each row and its previous row
this will be the log returns
"""
historical_data["Log Returns"] = historical_data["Log_Adjusted_Close"]\
    - historical_data["Prev_Log_Adj_Close"]

""" Drop the first row which will have NaN due to the shift """
historical_data = historical_data.dropna()

""" (a) Autocorrelation Analysis """
autocorrelation = historical_data["Log Returns"].autocorr()
print("Autocorrelation:", autocorrelation)

""" (b) Box Plot and Histogram """
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.boxplot(y=historical_data["Log Returns"])
plt.title("Box Plot of Log Returns")

plt.subplot(1, 2, 2)
sns.histplot(historical_data["Log Returns"], kde=True)
plt.title("Histogram of Log Returns")
plt.xlabel("Log Returns")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

""" (c) Basic Statistics of Residuals """
residuals = historical_data["Log Returns"]
basic_stats = {
    "Mean": np.mean(residuals),
    "Mode": stats.mode(residuals)[0],
    "Median": np.median(residuals),
    "Skewness": stats.skew(residuals),
    "Excess Kurtosis": stats.kurtosis(residuals)
}
print("Basic Statistics of Residuals:")
for stat, value in basic_stats.items():
    print(f"{stat}: {value}")

""" (d) Fitting Normal Distribution to Residuals """
plt.figure(figsize=(8, 6))
sns.histplot(residuals, kde=True, label="Empirical Density")
x = np.linspace(np.min(residuals), np.max(residuals), 100)
pdf = stats.norm.pdf(x, np.mean(residuals), np.std(residuals))
plt.plot(x, pdf, color='red', linestyle='--', label="Fitted Normal Density")
plt.title("Comparison of Empirical and Fitted Normal Density")
plt.xlabel("Residuals")
plt.ylabel("Density")
plt.legend()
plt.show()

""" (e) Shapiro-Wilk Test for Normality """
shapiro_stat, shapiro_p = stats.shapiro(residuals)
print(f"Shapiro-Wilk Test Statistic: {shapiro_stat}, p-value: {shapiro_p}")
if shapiro_p > 0.05:
    print("The residuals are normally distributed (p > 0.05)")
else:
    print("The residuals are not normally distributed (p <= 0.05)")