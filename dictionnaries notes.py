# Dictionaries
# I used AI to fill this dictionary with the French names for numerals 1 through 10.

# Created with AI assistance.
import random


french_number = {
    1: "un",
    2: "deux",
    3: "trois",
    4: "quatre",
    5: "cinq",
    6: "six",
    7: "sept",
    8: "huit",
    9: "neuf",
    10: "dix",
}
quiz = list(french_number.items())
random.shuffle(quiz)

# if 6 in french_number:
#     print("Found!")
# else:
#     print("Not Found")

# #I give it key, it gives me the value
# print(french_number[3])

# # create or Update, if it exists we replace it
# french_number[11]: "onze"

# # delete an item
# french_number[0]

# # errors - key error
# try:
#     print(french_number[14])
# except KeyError:
#     print("That is not in our dictionary")

# # better
# answer = french_number.get(12)
# print(answer)


# Quiz
correct = 0
incorrect = 0
for key, value in french_number.items():
    answer = int(input(f"Please enter the numeric value for {value}"))
    if answer == key:
        print("correct")
        correct += 1
    else:
        print("incorrect")
        incorrect += 1
score = correct / 10
print(f"Score:  {score:,.1f}")
