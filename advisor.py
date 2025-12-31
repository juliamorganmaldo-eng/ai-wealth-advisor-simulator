print("Welcome to the AI Wealth Advisor Simulator!")

def get_int(prompt, min_value=None, max_value=None):
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if min_value is not None and value < min_value:
                print(f"Please enter a number >= {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Please enter a number <= {max_value}.")
                continue
            return value
        except ValueError:
            print("Please enter a whole number (example: 10).")

time_horizon = get_int("How many years will you invest for? (example: 10) ", min_value=1, max_value=60)
risk = get_int("Risk tolerance from 1 to 10? (1 = very safe, 10 = very aggressive) ", min_value=1, max_value=10)

stocks = bonds = cash = 0

if time_horizon <= 3:
    stocks, bonds, cash = 20, 50, 30
elif time_horizon <= 7:
    if risk <= 4:
        stocks, bonds, cash = 40, 50, 10
    else:
        stocks, bonds, cash = 55, 40, 5
else:
    if risk <= 4:
        stocks, bonds, cash = 55, 40, 5
    elif risk <= 7:
        stocks, bonds, cash = 70, 25, 5
    else:
        stocks, bonds, cash = 85, 10, 5

print("\n--- Recommended Portfolio ---")
print(f"Stocks: {stocks}%")
print(f"Bonds : {bonds}%")
print(f"Cash  : {cash}%")

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

print("\nNote: This is an educational simulator, not financial advice.")

