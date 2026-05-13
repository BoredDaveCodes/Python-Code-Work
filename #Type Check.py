#Type Check

def type_check():
    typecheck = input("Please enter a number:")
    try:
        val = int(typecheck)
        print("Thank you for entering a number.")
    except ValueError:
        print("This is not a number. Please enter a number.")