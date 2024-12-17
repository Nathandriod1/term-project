with open("sample_AAPL.txt", "r") as f:
    listItems = f.read().splitlines()

appleprices = [float(price) for price in listItems]

mean_price = sum(appleprices) / len(appleprices)

variance = sum((price - mean_price) ** 2 for price in appleprices) / len(appleprices)

std_deviation = variance ** 0.5

print(f"Mean Price: {mean_price}")
print(f"Standard Deviation: {std_deviation}")
