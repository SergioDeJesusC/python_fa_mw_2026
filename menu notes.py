"""
Think CRUD

 Create
🔎 Search
📈 update
🗑️ Delete

  When we got crud, we will present user with a menu of choices. This is a standard interface module. Now that we know Match Case, It makes menu choices  easy. It will get even easir
"""

# Match case for menu
# Display menu
print(f"1.  Create a new contact")
print(f"2.  Search contact")
print(f"3.  Update contact")
print(f"4.  Delete contact")
print(f"5.  ")

# get user choise
choice: 1
while choice > 0 and choice < 4:
    choice = int(input("please enter the number of your selection:  "))
    match choice:

        case 1:
            print("Create")
        case 2:
            print("Seach")  # Read
        #Delete contact
        case 3:
            print("Update")
        case 4:
            print("Delete")
        case 5:
            print("Good bye!")
