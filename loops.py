"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""


hungry = True

while hungry:
    print("Eating a taco...")
    
    # We MUST change the state to stop the loop!
    answer = input("Are you full? (yes/no): ")
    if answer == "yes":
        hungry = False






def double_penny(days):
    # BASE CASE: Stop when we hit Day 1
    if days == 1:
        return 0.01
    
    # RECURSIVE CASE: Double the previous day's total
    return 2 * double_penny(days - 1)

total = double_penny(30)
print(f"Total after 30 days: ${total:,.2f}")