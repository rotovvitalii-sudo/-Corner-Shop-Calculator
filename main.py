earnings = {
    "Bubblegum": 202,
    "Toffee": 118,
    "Ice cream": 2250,
    "Milk chocolate": 1680,
    "Doughnut": 1075,
    "Pancake": 80,
}

print("Earned amount:")
for item, amount in earnings.items():
    print(f"{item}: ${amount}")

income = float(sum(earnings.values()))
print()
print(f"Income: ${income}")
print("Staff expenses:")
staff_expenses = int(input())
print("Other expenses:")
other_expenses = int(input())

net_income = income - staff_expenses - other_expenses
print(f"Net income: ${net_income}")