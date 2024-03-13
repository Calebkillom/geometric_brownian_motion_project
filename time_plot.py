import pandas as pd
import matplotlib.pyplot as plt

""" Read csv File and convert it to a dataframe """
file_path = "XOM_historical_data_2018-03-09_2024-03-10.csv"
historical_data = pd.read_csv(file_path)

if not historical_data.empty:
    print("csv file read successfully")
    print(historical_data.head())
else:
    print("An error occurred!!!")

""" Create a new column of Price which is the daily adjusted closing stock """
historical_data["Price"] = historical_data["Adj Close"]
print(historical_data.head())

""" Convert the Date column to datetime Object """
historical_data["Date"] = pd.to_datetime(
    historical_data["Date"], format='%d/%m/%Y')

""" Set the 'Date' column as the index """
historical_data.set_index("Date", inplace=True)

""" Plot the "Price" column """
historical_data["Price"].plot(
    figsize=(10, 6), color="blue",linewidth=0.5)

""" Set the title and labels """
plt.title(
    'Daily adjusted closing stock price-XOM' 
    ' observed over 09/03/2018 to 08/03/2024')
plt.xlabel('Date')
plt.ylabel('Price')

""" Show the plot """
plt.grid(True)
plt.show()