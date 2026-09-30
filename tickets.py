"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""

seats = list(range(1, 21))

print("Available seats:", seats)

while seats:
    try:
        seat = int(input("Enter a seat number (0 to quit): "))
        if seat == 0:
            break
        if seat not in seats:
            print("Invalid seat number or seat already taken.")
            continue
        seats.remove(seat)
        print("Seat", seat, "has been sold.")
        print("Available seats:", seats)
    except ValueError:
        print("Please enter a valid integer.")
    