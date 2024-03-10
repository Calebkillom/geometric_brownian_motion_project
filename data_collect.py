import yfinance as yf
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

""" Format the dates for the filename """
filename = f"{stock_symbol}_historical_data_{start_date}_{end_date}.csv"

""" Print the data """
print(data)

data.to_csv(filename)
