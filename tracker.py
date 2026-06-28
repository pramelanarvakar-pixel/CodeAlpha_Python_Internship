# Task 2: Stock Portfolio Tracker - CodeAlpha
# Student ID: CA/DF1/174377

# Hardcoded stock prices as per task requirement
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130,
    "META": 300
}

portfolio = {}
total_investment = 0

print("=" * 40)
print(" CodeAlpha Task 2 - Stock Tracker")
print("=" * 40)
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Type 'done' when finished adding stocks\n")

while True:
    stock = input("Enter stock symbol: ").upper().strip()

    if stock == 'DONE':
        break

    if stock in stock_prices:
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            if quantity > 0:
                portfolio[stock] = portfolio.get(stock, 0) + quantity
                cost = stock_prices[stock] * quantity
                total_investment += cost
                print(f"Added: {quantity} x {stock} = ${cost}\n")
            else:
                print("Quantity must be positive\n")
        except ValueError:
            print("Please enter a valid number\n")
    else:
        print(f"Stock '{stock}' not found. Available: {list(stock_prices.keys())}\n")

# Display Results
print("\n" + "=" * 40)
print("YOUR PORTFOLIO SUMMARY")
print("=" * 40)

if portfolio:
    for stock, qty in portfolio.items():
        value = stock_prices[stock] * qty
        print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}")

    print("-" * 40)
    print(f"TOTAL INVESTMENT VALUE: ${total_investment}")
    print("=" * 40)

    # Optional: Save to file
    with open("portfolio_summary.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("=" * 30 + "\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} shares = ${stock_prices[stock] * qty}\n")
        f.write("-" * 30 + "\n")
        f.write(f"Total Investment: ${total_investment}\n")
    print("\nPortfolio saved to 'portfolio_summary.txt'")
else:
    print("No stocks added to portfolio.")
