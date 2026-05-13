#Function 2 out of 3
#Author: Dave Muton

password = input("Please Create a password: ")

def password_check():
    if len(password) < 12:
        print("Your password is too short, please create a password with at least 12 characters.")
    else:
        print("Your password has been created successfully.")
        print("Make sure to remember your password!")
password_check()