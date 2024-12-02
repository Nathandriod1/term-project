import matplotlib.pyplot as plt
f = open("sample_AAPL.txt", "r")
listItems = f.read().splitlines()
f.close()
appleprices = [float(price) for price in listItems]
days = list(range(1, len(appleprices) + 1))
plt.figure(figsize=(10, 6))  # Set the figure size
plt.plot(days, appleprices, color='blue', linewidth=2)
plt.title("Apple Stock Price, Nov 2019 to Nov 2020", fontsize=14)
plt.xlabel("Day", fontsize=12)
plt.ylabel("Trading price", fontsize=12)
plt.grid(alpha=0.4)
plt.show()
