stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

total = 0
portfolio = []

print("📈 Stock Portfolio Tracker")

while True:
    name = input("Enter stock name (or done): ").upper()
    if name == "DONE":
        break

    if name in stocks:
        qty = int(input("Enter quantity: "))
        value = stocks[name] * qty
        total += value
        portfolio.append(f"{name} x {qty} = ${value}")
    else:
        print("Stock not found!")

print("\nYour Portfolio:")
for item in portfolio:
    print(item)

print("💰 Total Investment Value = $", total)

with open("portfolio.txt", "w") as file:
    file.write("\n".join(portfolio))
    file.write(f"\nTotal = ${total}") 

print("Saved to portfolio.txt")
