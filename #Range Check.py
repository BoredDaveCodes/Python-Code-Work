#Range Check

def range_check():
    rangecheck = int(input("Please enter a number between 1 and 10:"))
    if rangecheck < 1 or rangecheck > 10:
        print("The number is out of range.")
    else:
        print("Thank you for entering a valid number.")