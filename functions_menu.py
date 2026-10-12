"""


using functions to create a menu
"""
def display_menu():
    # display menu
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")


try:
    selection = int(input("Please enter"))


    value = display_menu()
    print(value)
    match value:
            case 1:
                create()
            case 2:
                read()
            case 3:
                update()
            case 4:
                delete()
            case _:
                print("Sorry, that is not a valid choice")
                valute = display_menu()

def create():
    # create a record
    pass


def read():
    # read a record
    pass


def update():
    # update a record
    pass


def delete():
    # delete a record
    pass


def main():
    # main a record
    