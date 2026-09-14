"""
Error cheching data entry with while statements
"""

# Name check

# Rule - can't be empty
# less than 30 characters
# should have first letter capitalized (we handle)

try:
    fname = ""
    while not fname:
            fname = input("Please enter your first name:")       
            fname = fname.strip()


    age = -1
    while age >= 0:
        age = int(input("please enter your child's age: (whole years, round down)") )

except ValueError:
    print("I'm sorry, that is not a valid value")
except Exception as e:
    print(f"Error: {e}")