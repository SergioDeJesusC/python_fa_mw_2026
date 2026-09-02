# get info from user

gross_income = float(input("what is your gross monthly income  ")) 
housing =float(input("what do you spend on your rent or mortgage?  "))
phone = float(input("what do you spend on your phone each month?   "))


net_income = gross_income * .8

total_expenses = phone  + housing
remaining = net_income - total_expenses


print(f"You spent a total of {total_expenses:,.2f}")
print(f"That was {total_expenses/net_income: .2%} of your income")




# Without conversion:
num1 = input("Enter 5: ")   # "5"
num2 = input("Enter 5: ")   # "5"
print(num1 + num2)          # Output: 55 (concatenation, not addition!)


# Proper conversion:
age = int(input("Enter your age: "))
hourly_wage = float(input("Enter hourly pay: $"))



pay = 2344.522
print(f"Pay: ${pay:,.2f}")
# Output: Pay: $2,344.52


score = 0.857
# The .1 tells Python one decimal place
print(f"Your grade is {score:.1%}")
# Output: Your grade is 85.7%



# --- 1. GET INPUT ---
gross_pay = float(input("Enter Monthly Gross Pay: $"))

# --- 2. CALCULATIONS ---
fed_tax = gross_pay * 0.20
net_pay = gross_pay - fed_tax

# --- 3. FORMATTED OUTPUT ---
print(f"Gross Pay:      ${gross_pay:,.2f}")
print(f"Net Pay:        ${net_pay:,.2f}")