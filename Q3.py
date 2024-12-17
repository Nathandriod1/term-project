with open("sample_AAPL.txt", "r") as f:
    listItems = f.read().splitlines()

appleprices = [float(price) for price in listItems]

current_max_val = 0
max_profit_val = 0
buy_day = 0
sell_day = 0

for i in range(len(appleprices) - 1, -1, -1):
    price = appleprices[i]
    if price > current_max_val:
        current_max_val = price 
        sell_day = i  
    
    potential_profit = current_max_val - price 
    if potential_profit > max_profit_val:
        max_profit_val = potential_profit  
        buy_day = i  
print(f"Largest possible profit: ${max_profit_val:.2f}")
print(f"Buy on day {buy_day + 1} (Price: ${appleprices[buy_day]:.2f})")
print(f"Sell on day {sell_day + 1} (Price: ${appleprices[sell_day]:.2f})")

