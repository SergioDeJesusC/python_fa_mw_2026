# ℹ️ Operators

answer = int(input ("Enter a number between 1 and 100:  "))

if answer == 42:
    print("You found the answer to life, the universe and everything")
else:
    print("Sorry. Talk to the white mice.")

print("Score ")
score = float(input("Please enter your test score:  "))

if score > 90.0:
    print("A")
elif score > 80.0:
    print("B")
elif score > 70.0:
    print("C")
elif score > 60.0:
    print("D")
else:
    print("F")

# 💀⚡ string are CASE SENSITIVE
# convert to upper or lower by using .lower()

current_month = input("what Month is it? (spell out full):")

match current_month.lower():