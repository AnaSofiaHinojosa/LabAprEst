import matplotlib.pyplot as plt

# Assuming buy_signals and sell_signals are boolean arrays or Series
plt.figure(figsize=(12,6))
plt.plot(price.index, price, label='Price', color='lightblue')

# Scatter for Buy signals
plt.scatter(price.index[buy_signals], price[buy_signals], 
            label='Buy', marker='^', color='darkseagreen', s=80)

# Scatter for Sell signals
plt.scatter(price.index[sell_signals], price[sell_signals], 
            label='Sell', marker='v', color='tomato', s=80)

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Price with Buy/Sell Signals')
plt.legend()
plt.show()
