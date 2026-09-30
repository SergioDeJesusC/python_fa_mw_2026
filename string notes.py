"""
    all about string!
"""

name = "sergio"

new_name = "luis"

names = names + new_name # replaces content of names - concatenating

print(names)

print("*" * 50)

print(len(names))

print(names(5))
print(f"\n\n - 2 blank lines \n \ttad")

my_name = "     sergio      luis    "
print(my_name.strip().title)

greeting = "Hello World"

words = greeting.split(" ")
print(words)
for word in words:
    print(word)


print("It Digit?"())
print("123".isalpha())
print("123.4".isalpha())

print("Is Alpha"())
print("Python".isalpha())



name_string = "BINGO"
dog_letters = list(name_string)
count = 0

for char in name_string:
    current_name = " ".join(dog_letters)

    print("There was a farmer who had a dog and Bingo was his Name-o")
    print(f"((current_name)) \n" * 3)
    print("and Bingo was")