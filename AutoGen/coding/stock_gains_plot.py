# filename: stock_gains_plot.py

import matplotlib.pyplot as plt

# YTD stock gains for NVDA and TSLA
nvda_ytd_gain = 0.15
tsla_ytd_gain = -0.05

# List of stocks and their YTD gains
stocks = ['NVDA', 'TSLA']
ytd_gains = [nvda_ytd_gain, tsla_ytd_gain]

plt.bar(stocks, ytd_gains, color=['blue', 'red'])
plt.ylabel('YTD Gain')
plt.title('Year-to-Date Stock Gains for NVDA and TSLA')
plt.savefig('ytd_stock_gains.png')

# Show the plot
plt.show()