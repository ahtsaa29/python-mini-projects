# Calculate income tax for the given income by adhering to the below rules

income = int(input("enter the income : "))

if income <= 10000:
    tax = 0
elif income <= 20000:
    tax = income * 0.1

elif income > 20000:
    tax = income * 0.2


print(income)

print(tax)
