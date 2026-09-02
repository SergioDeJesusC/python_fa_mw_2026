# ""
# fstring formatting in Python-
# this makes it easier to use variable, format numbers, left aling, right aling
# etc. there is a python  F-string
# ""

# ❕ fstrings for variables

#     name = "Sergio"
#     age = "19"

# print(f"{name} is {age} and will be {age + 1} next year.")


#   Alingment
#  the number after the colon and symbol is your colum width

# print(f"{name:<30}")
# print(f"{name:>30}")
# print(f"{name:^30}")

#   line below is creating two columns 30 wide centering name and age
#  print(f"{name:^30} {age:^30}")

score_1 = 1088
score_2 = 1073
score_3 = 1065


average = (score_1 + score_2 + score_3) / 3

print(average)
print(f"{average: ,.0f}")

distance_to_monroe = 852
distance_to_phoenix = 1712

print(f"Distance_to_Monroe, North Carolina{distance_to_monroe: ,.0f}")
print(f"Distance_to_phoenix, Arizona{distance_to_phoenix: ,.0f}")



current_mort_rate = 0.0675
print(f"Mortgage rate = {current_mort_rate:.2%}")