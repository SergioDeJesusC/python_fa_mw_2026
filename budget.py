# get info from user

(gross_income = "what is your gross monthly income ")
(housing = "what do you spend on your rent or mortgage? ")
(phone = "what do you spend on your phone each month? ")


net income = gross_ income * .8

total_expenses = phone  + housing
remaining = net_income - total_expenses


print(f"You spent a total of {total_expenses:,.2f}")
print(f"That was {total_expenses/net_income: .2%} of your income: .2%")