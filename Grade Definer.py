#Function thingy
#Author: Dave Muton

def name():
    print("=================================")
    print("         Grade Definer")
    print("=================================")

def checkychecky():
    print("Welcome to the Grade Definer!")
    continue_ = input("Are you ready to continue? (Y/N): ")
    if continue_ == "Y" or continue_ == "y":
        grade_calculator()
    else:
        goodbye()
 

        def grade_calculator():
            paper1 = int(input("Enter your score for Paper 1: "))
            paper2 = int(input("Enter your score for Paper 2: "))
            paper3 = int(input("Enter your score for Paper 3: "))
            final_grade = paper1 + paper2 + paper3
            if final_grade >= 801:
                print("Your final grade is A")
            elif final_grade >= 701:
                print("Your final grade is B")
            elif final_grade >= 601:
                print("Your final grade is C")
            elif final_grade >= 501:
                print("Your final grade is D")
            elif final_grade >= 401:
                print("Your final grade is E")
            else:
                print("Your final grade is F")
        grade_calculator()

        def totalscore():
            print("Thank you for using the Grade Definer!")
        totalscore()

        def goodbye():
            print("Goodbye!")
        goodbye()

