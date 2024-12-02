f = open("sample_AAPL.txt", "r")
listItems = f.read().splitlines()
f.close()
appleprices = [float(price) for price in listItems]
current_max_val = 0  
max_profit_val = 0   
for price in reversed(appleprices):
    current_max_val = max(current_max_val, price)  
    potential_profit = current_max_val - price   
    max_profit_val = max(potential_profit, max_profit_val) 
print(f"Largest possible profit: ${max_profit_val:.2f}")

