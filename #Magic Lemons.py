#Magic Lemons
#Author: Dave Muton

def welcome():
    print("========================")
    print("      Magic Lemons")
    print("========================")
    print("Welcome to the Magic Lemons hotline")
welcome()

print("What would you like to know?")
print("1. What Magic Lemons are")
print("2. What potions can be created with them")
print("3. Wheather you can eat Uncooked Magic Lemons")
print("4. Magic Lemons and Animals")

print("What would you like to know about Magic Lemons. Please enter the number corresponding to the information you would like to know about.")
option = int(input("Option: "))

while True:
    if option == 1:
        print("Magic lemons are a type of magical fruit that is used as an ingredient in potion making and can be eaten cooked or raw. However, if eaten raw, they can turn the consumer into a different form of being. There are a variety of potions that these magical fruits can be used in, and Magic Lemons can also be used for medicinal purposes.")
        feedback = input("Would you like to give feedbck (y/n)? ")
        if feedback == "y":
            reader_feedback = input("Please give us your feedback")
            print("Thank you for your feedback, we will take that on board")
            break
        if feedback == "n":
            print("Thank you for learning about Magic Lemons")
            break 
    if option == 2:
        print("Health revival potions are also valuable, as they can be used to heal internal medical conditions, injuries, and some mental health conditions.")
        feedback = input("Would you like to give feedback (y/n)")
        if feedback == "y":
            reader_feedback = input("Please give us your feedback")
            print("Thank you for your feedback, we will take that on board")
            break
        if feedback == "n":
            print("Thank you for learning about Magic Lemons")
            break 
        if option == 3:
            print("""When eating uncooked/raw magic lemons, the consumer MUST be careful with the amount that they eat; eating too many can be bad for you; various effects can happen if you eat too many (this depends on the consumer, everyone's body is different). How Many Is Too Many?
    This question is asked a lot, especially by new and young sorcerers. With these magical fruits, the term "too many", as a number, is 3 or more Magic Lemons.
    Consuming Raw Magic Lemons
    Eating 1 uncooked magic lemon can help the sorcerer breathe underwater, which is especially useful for retrieving objects that are in a body of deep water. Eating two magic lemons turns the sorcerer into a Merperson. However, if a sorcerer was to eat 3 or more of these magical fruits, there are many effects, such as:
    *Death
    *Sickness
    *Loss of magical ability
    *Memory loss
    *Transformation into a Werewolf
    There are many other effects, but these are the most common effects. The most common effect is the transformation of a Werewolf; however, the antidote to eating too many magic lemons is to eat something called Lemonesca, which is a small part of the magic lemons gene. This should be taken for approximately 10 days to make sure that any toxins are neutralized. You can get Lemonesca from your local Magica Medicina herbs and potions stores.
    """)
            feedback = input("Would you like to give feedback (y/n)? ")
            if feedback == "y":
                reader_feedback = input("Please give us your feedback")
                print("Thank you for your feedback, we will take that on board")
                break
            if feedback == "n":
                print("Thank you for learning about Magic Lemons")
                break 
    if option == 4:
        print("A magic lemon should never be given to an animal of any kind, as the properties of the fruit will cause the animal to explode. This goes against the laws in the Sorcerer's Kingdom, on law 1.2.45 (Magic and Animals). This law also states that anyone found guilty of the crime will be imprisoned in the Barred Globe prison.")
        feedback = input("Would you like to give feedback (y/n)? ")
        if feedback == "y":
            reader_feedback = input("Please give us your feedback")
            print("Thank you for your feedback, we will take that on board")
            break
        if feedback == "n":
            print("Thank you for learning about Magic Lemons")
            break