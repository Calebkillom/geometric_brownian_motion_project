import yfinance as yf
import os
"""
Fetches historical stock data for Exxon Mobil Corporation (stock symbol: XOM)
from Yahoo Finance from 2018 to 2024. The data is saved to a CSV file
with a filename that includes the stock symbol and the time period.
"""

""" Specify the stock symbol and time period """
stock_symbol = "XOM"
start_date = "2018-03-09"
end_date = "2024-03-10"

""" Fetch historical data """
data = yf.download(stock_symbol, start=start_date, end=end_date)

if not data.empty:
    """ Format the dates for the filename """
    filename = f"{stock_symbol}_historical_data_{start_date}_{end_date}.csv"

    """ Save the data to a CSV file """
    data.to_csv(filename)

    if os.path.isfile(filename):
        print(f"Data was successfully saved to '{filename}'")
    else:
        print("Failed to save data to CSV")

else:
    print("No data available for the specified time period")
