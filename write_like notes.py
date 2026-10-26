"""
write to file

"""


# create and writ to file
def write_header():
    # file = open("menu.txt", "m")
    # file.writen("--------ice cream menu--------")
    # file.close()

    # new - self closing way
    with open("menu.txt", "w") as f:
        f.write("--------ice cream menu--------\n")


def append_line():
    with open("menu.txt", "a") as f:
        ice_cream = {
        "monday": "",
        "tuesday": ""
        }


def main():
    write_header()


    main()