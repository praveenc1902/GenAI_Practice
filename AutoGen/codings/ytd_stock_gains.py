# filename: ytd_stock_gains.py
from functions import get_stock_prices, plot_stock_prices
import pandas as pd

# Current date
today_date = '2024-06-04'

# Start date for Year-To-Date
ytd_start_date = today_date[:4] + '-01-01'

# Get stock prices for NVDA and TLSA from the start of the year to today
stock_symbols = ['NVDA', 'TLSA']
stock_prices_ytd = get_stock_prices(stock_symbols, ytd_start_date, today_date)

# Calculate stock gains as of today
stock_gains_ytd = ((stock_prices_ytd.iloc[-1] / stock_prices_ytd.iloc[0] - 1) * 100).to_frame()

# Plot and save the figure
plot_stock_prices(stock_gains_ytd, 'ytd_stock_gains.png')