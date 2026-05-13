#Login and account creation system
#Author: Dave Muton 

print("===================================")
print("    Basement Government Systems")
print("===================================")
print("")
print("Welcome to the Basement Government Systems")
print("")
print("Please select an option:")
print("1. Login")
print("2. Create an account")
print("3. Exit")

while True:
    option = input("Enter your choice (1-3): ")
    if option == "1":
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        import os
        if os.path.exists("users/" + email + ".txt"):
            with open("users/" + email + ".txt", "r") as f:
                stored_password = f.read().strip()
            if password == stored_password:
                print("Login successful! Welcome back.")
                break
            else:
                print("Incorrect password. Please try again.")   
        else:
            print("Account not found. Please create an account.")
    elif option == "2":
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        if email.strip() == "":
            print("Email cannot be empty. Please try again.")
            continue
        elif "@" not in email or "." not in email:
            print("Invalid email format. Please try again.")
            continue
        phone_number = input("Enter your phone number: ")
        password = input("Create a password: ")
        if password.strip() == "":
            print("Password cannot be empty. Please try again.")
            continue
        elif password.lower() == "password":
            print("Password cannot be 'password'. Please try again.")
            continue
        elif len(password) < 12:
            print("Password must be at least 12 characters long. Please try again.")
            continue
        elif " " in password:
            print("Password cannot contain spaces. Please try again.")
            continue
        elif not any(char.isdigit() for char in password):
            print("Password must contain at least one number. Please try again.")
            continue
        elif not any(char.isupper() for char in password):
            print("Password must contain at least one uppercase letter. Please try again.")
            continue
        elif not any(char.islower() for char in password):
            print("Password must contain at least one lowercase letter. Please try again.")
            continue
        import os
        if not os.path.exists("users"):
            os.makedirs("users")
        if os.path.exists("users/" + email + ".txt"):
            print("An account with this email already exists. Please login.")
        else:
            with open("users/" + email + ".txt", "w") as f:
                f.write(password)
            print("Account created successfully! You can now login.")

    if option == "3":
        print("Exiting the system. Goodbye!")
        break