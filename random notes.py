"""
Advanced strings, import statements, random
"""
import random

# The fortune
#list of possible fortune




selected = random.randint(0,24)
print(selected)

topic = input("Please enter a sigle word that you want to use to look for fortune.")

printed = False
for item in fortunes:
    if topic in item:
        printed = True
        print(item)

if printed == False:
    selected = random.randint(0,19)
    print(fortunes[selected])