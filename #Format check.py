#Format check

def format_check():
    formatcheck = input("Please enter your email address:")
    if "@" not in formatcheck or "." not in formatcheck:
        print("This is not a valid email address.")
    else:
        print("Thank you for entering a valid email address.")