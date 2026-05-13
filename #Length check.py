#Length check

def length_check():
    lengthcheck = input("Please enter your name:")
    if len(lengthcheck) < 1 or len(lengthcheck) == " ":
        print("Your name is too short.")
    else:
        print("Hello " + lengthcheck)
length_check()