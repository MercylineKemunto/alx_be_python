#!/usr/bin/python3
#Prompt the user for monthly income and expenses
monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")
#Convert to float and calculate monthly savings
monthly_savings = float(monthly_income) - float(monthly_expenses)
#Calculate projected annual savings, inclusing 5% interest
projected_savings =monthly_savings * 12 + (monthly_savings * 12 * 0.05)
#Output the results as integers
print(f"Your monthly savings are ${int(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")
