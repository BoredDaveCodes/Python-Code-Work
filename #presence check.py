#presence check

def checky_checky():
    checkthingy = input("Are you there bozo? ")
    if checkthingy == " ":
        print("You didn't answer the question. Please try again.")
    
    else:
        print("Thank you for confirming your presence!")
        print("Exiting the system. Goodbye!")
        checky_checky()

