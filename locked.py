"""
ASSIGNMENT 6B: THE DEPARTMENT SECURITY TERMINAL
This program implements a secure terminal system for department access
with username/password authentication and error handling.
"""

# Department constant
DEPARTMENT = "SECURITY_TERMINAL"

# Username tuple (immutable)
usernames = ("user1", "user2")

# Password list
passwords = ["secure77", "secure77"]

# Interactive loop
while True:
    try:
        print("\n" + "=" * 50)
        print(f"  {DEPARTMENT}")
        print("=" * 50)
        
        # Get user input
        username = input("\nEnter username: ").strip()
        password = input("Enter password: ").strip()
        
        # Validate credentials
        if username in usernames and password in passwords:
            print(f"Access granted for {username}")
            print(f"Welcome to {DEPARTMENT}!")
            
            # Ask if user wants to continue
            again = input("\nAccess another account? (yes/no): ").lower()
            if again != "yes":
                print("Exiting the terminal. Goodbye!")
                break
        else:
            print("Access denied. Invalid username or password.")
            print("Please try again.")
            
    except TypeError:
        print("ERROR: Invalid input type.")
        print("Please contact the help desk at support@department.com")
        
    except KeyboardInterrupt:
        print("Exiting the terminal. Goodbye!")
        break
