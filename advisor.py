"""
AI Wealth Advisor (Beginner-Friendly CLI)
Run with: python3 advisor.py
"""

def ask_float(prompt, min_value=None, max_value=None):
    while True:
        raw = input(prompt).strip().replace(",", "")
        try:
            value = float(raw)
            if min_value is not None and value < min_value:
                print(f"Please enter a number >= {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Please enter a number <= {max_value}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number (example: 5000).")


def ask_choice(prompt, choices):
    """
    choices: dict like {"1": "Conservative", "2": "Moderate", "3": "Aggressive"}
    returns the selected value (e.g., "Conservative")
    """
    while True:
        print(prompt)
        for k, v in choices.items():
            print(f"  {k}) {v}")
        pick = input("Select an option: ").strip()
        if pick in choices:
            return choices[pick]
        print("Please choose one of the listed options.\n")


def recommend_allocation(risk_level):
    # Simple, beginner-friendly allocations
    if risk_level == "Conservative":
        return {"Bonds": 70, "Stocks": 25, "Cash": 5}
    if risk_level == "Moderate":
        return {"Bonds": 40, "Stocks": 55, "Cash": 5}
    # Aggressive
    return {"Bonds": 15, "Stocks": 80, "Cash": 5}


def explain(risk_level, years):
    if risk_level == "Conservative":
        return (
            "You chose a lower-risk style. This typically aims for smoother returns "
            "with fewer big ups/downs, which can feel more comfortable during market drops."
        )
    if risk_level == "Moderate":
        return (
            "You chose a balanced approach. This typically mixes growth (stocks) and stability (bonds). "
            "Many long-term investors choose something like this."
        )
    return (
        "You chose a higher-growth style. This typically has bigger swings (up and down), "
        "but may have higher long-term growth potential—especially over longer time periods."
    )


def main():
    print("\n==============================")
    print("      AI WEALTH ADVISOR 💸")
    print("==============================\n")

    name = input("What is your name? ").strip() or "Investor"
    print(f"\nHi {name}! Answer a few quick questions and I’ll give you a simple recommendation.\n")

    portfolio = ask_float("Current portfolio balance ($): ", min_value=0)
    monthly = ask_float("Monthly contribution ($): ", min_value=0)
    years = ask_float("How many years do you plan to invest? (ex: 10): ", min_value=1)

    risk_level = ask_choice(
        "\nWhat is your risk comfort level?",
        {"1": "Conservative", "2": "Moderate", "3": "Aggressive"}
    )

    goal = ask_choice(
        "\nWhat is your main goal?",
        {"1": "Long-term growth", "2": "Retirement planning", "3": "Saving for something big"}
    )

    allocation = recommend_allocation(risk_level)

    print("\n--------------------------------")
    print("RECOMMENDATION")
    print("--------------------------------")
    print(f"Name: {name}")
    print(f"Goal: {goal}")
    print(f"Time Horizon: {int(years)} years")
    print(f"Risk Level: {risk_level}")
    print("\nSuggested simple allocation:")
    for k, v in allocation.items():
        print(f"  - {k}: {v}%")

    print("\nWhy this fits:")
    print(explain(risk_level, years))

    print("\nImportant note:")
    print("This is educational, not financial advice. Consider fees, taxes, and your full financial situation.\n")

    print("✅ Done! Thanks for using AI Wealth Advisor.\n")


if __name__ == "__main__":
    main()

