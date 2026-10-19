"""
passing values with functions

"""

# Globals

SCOPE_DEMO = "Visible!!!"

def passed(variable):
    # notice the name does not matter!!!
    print(variable)


def not_passed():
    # print(local)
    # print(variable)
    print(SCOPE_DEMO)


def count(one, two, three):
    print("\n\ncount")
    print(one)
    print(two)
    print(three)


def control(one, two, three):
    print("\n\nControl")
    print(one)
    print(two)
    print(three)


def order_pizza(toppings):
    for topping in toppings:
        print(topping)


def main():
    print(SCOPE_DEMO)
    local = "Can you see me?"
    print(local)
    passed(local)
    not_passed()
    count(4, 32, 43)
    control(three=3, one=1, two=2)
    my_toppings = ["Pepperoni", "Mushroom", "Green Peppers", "Onions"]
    order_pizza(my_toppings)



    main()
    