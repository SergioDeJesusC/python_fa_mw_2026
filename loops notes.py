<<<<<<< HEAD
# while loop demo
#calculating average test score

entering = True  # flag
total = 0
count = 0




while entering >= 0:
    print("Enter each test score, enter -1 when done.")
    score = float(input("Enter the test score"))
    if score > 0:
        total += score # short cut total = total + score
        count += 1
    else:
        print("Entry completed")

average = total / count

print(f"The average test score was: {average:,.1f}")

for x in range(1, 11):
    print(x)

for y in range(10, 0, -1):
    print(y)

for day in (
    "Sunday", 
    "Monday", 
    "Tuesday", 
    "Wensday", 
    "Thursday",
    "Friday", 
    "Saturday",
):
    print(day)

eat = True

while not eat:
    feed = input("Can we eat now???  (yes/no)  ").lower()
    if feed == "yes":
        eat = True
=======
# while loop demo
#calculating average test score

entering = True  # flag
total = 0
count = 0




while entering >= 0:
    print("Enter each test score, enter -1 when done.")
    score = float(input("Enter the test score"))
    if score > 0:
        total += score # short cut total = total + score
        count += 1
    else:
        print("Entry completed")

average = total / count

print(f"The average test score was: {average:,.1f}")

for x in range(1, 11):
    print(x)

for y in range(10, 0, -1):
    print(y)

for day in (
    "Sunday", 
    "Monday", 
    "Tuesday", 
    "Wensday", 
    "Thursday",
    "Friday", 
    "Saturday",
):
    print(day)

eat = True

while not eat:
    feed = input("Can we eat now???  (yes/no)  ").lower()
    if feed == "yes":
        eat = True
>>>>>>> 88cea1dfdcc244c0327fe035cf02228b5b9db499
