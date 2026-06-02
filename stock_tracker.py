
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 400,
    "AMZN": 200
}

total_investment = 0
portfolio_details = []

print("----- Stock Portfolio Tracker -----")

num_stocks = int(input("How many different stocks do you own? : "))

for i in range(num_stocks):
    print(f"\nStock {i + 1}")

    stock_name = input("Enter stock symbol (AAPL, TSLA, GOOG, MSFT, AMZN): ").upper()

    if stock_name not in stock_prices:
        print("Stock not found! Skipping...")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock_name]
    investment_value = price * quantity

    total_investment += investment_value

    portfolio_details.append(
        f"{stock_name} | Quantity: {quantity} | Price: ${price} | Value: ${investment_value}"
    )

print("\n----- Portfolio Summary -----")

for item in portfolio_details:
    print(item)

print(f"\nTotal Investment Value: ${total_investment}")

with open("portfolio.txt", "w") as file:
    file.write("----- Portfolio Summary -----\n\n")

    for item in portfolio_details:
        file.write(item + "\n")

    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\nPortfolio saved successfully to portfolio.txt")