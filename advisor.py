print("Welcome to the AI Wealth Advisor Simulator!")

time_horizon = int(input("How many years will you invest for? (example: 10) "))
risk = int(input("Risk tolerance from 1 to 10? (1 = very safe, 10 = very aggressive) "))

stocks = 0
bonds = 0
cash = 0

if time_horizon <= 3:
    stocks = 20
    bonds = 50
    cash = 30
elif time_horizon <= 7:
    if risk <= 4:
        stocks = 40
        bonds = 50
        cash = 10
    else:
        stocks = 55
        bonds = 40
        cash = 5
else:
    if risk <= 4:
        stocks = 55
        bonds = 40
        cash = 5
    elif risk <= 7:
        stocks = 70
        bonds = 25
        cash = 5
    else:
        stocks = 85
        bonds = 10
        cash = 5

print("\n--- Recommended Portfolio ---")
print("Stocks:", stocks, "%")
print("Bonds :", bonds, "%")
print("Cash  :", cash, "%")

print("\n--- Explanation ---")
if time_horizon <= 3:
    print("Because your time horizon is short, this portfolio is more conservative.")
else:
    print("Because you have more time, you can take more risk for growth.")

if risk <= 4:
    print("Your risk score is lower, so we added more bonds for stability.")
elif risk <= 7:
    print("Your risk score is moderate, so this portfolio balances growth and safety.")
else:
    print("Your risk score is high, so we increased stocks to focus on growth.")

