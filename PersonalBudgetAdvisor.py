def track_budget():
    income = float(input("Enter your monthly income: ₹"))
    expenses = {}
    total_expense = 0
    while True:
        name = input("Enter expense category (or 'done'): ")
        if name == 'done':
            break
        amount = float(input(f"Enter amount for {name}: ₹"))
        expenses[name] = amount
        total_expense += amount

    print("\nSummary:")
    for category, amount in expenses.items():
        print(f"{category}: ₹{amount} ({(amount/total_expense)*100:.2f}%)")

    savings = income - total_expense
    print(f"\nTotal Expenses: ₹{total_expense}")
    print(f"Savings: ₹{savings}")
    if savings < income * 0.2:
        print("Suggestion: Try to save at least 20% of your income.")

# track_budget()  # Uncomment to run interactively
