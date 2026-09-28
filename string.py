"""
-----------------------------------------------------------------------
ASSIGNMENT 7A: STRING MASTERY LAB
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: String Basics (Length, Indexing, ASCII) completed.
[ ] 3. Task 2: The Cleanup Crew (Strip, Case, Replace) completed.
[ ] 4. Task 3: Validation (isdigit check) completed.
[ ] 5. Task 4: The Duck Loop (.join and direct iteration) completed.
-----------------------------------------------------------------------
"""

names = "Meri"
new_name = "Louise"
instrument = "Electric Guitar"

print(instrument)

print("*" * 140)

max()
min()

print(new_name.strip())

serial_number = "90210"



# We are going to sing about a Duck!
# We can't change strings (immutable), so we convert to a list

name_string = "DUCKY"
duck_letters = list(name_string)
count = 0

final_name = " ".join(duck_letters)
print(f"({final_name}) \n" * 3)
print("and Ducky was his name-o!")
