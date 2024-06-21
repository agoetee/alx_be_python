# This program does financial calculations

month_income = int(input("Enter your monthly income: "))
month_expense = int(input("Enter your monthly expenses: "))

month_savings = month_income - month_expense

projected_saving = month_savings * 12 + (month_savings * 12 * 0.05)

print("Your monthly savings are:", month_savings)
print("Projected savings after one year, with interest, is", projected_saving)
