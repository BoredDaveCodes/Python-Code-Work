#My basement Cafe V2
#By Dave Muton

print("===============================")
print("         Basement Cafe         ")
print("===============================")
print("Welcome to the Basement Cafe!")
print("Here is our menu:")
print("1. Coffee - £2.00")
print("2. Tea - £1.50")
print("3. milk - £1.00")
print("4. Juice - £2.50")
print("5. Water - £1.00")
print("6. cake - £3.00")
print("7. sandwich - £5.00")
print("8. salad - £4.00")

print("9. create your own killer sandwich - $7.00")
print("A killer sandwich includes a drink and a side")
print("ingredients available: ")
print ("A choice of bread: white, wheat, rye, sourdough")
print ("A choice of protein: turkey, ham, roast beef, chicken, tofu")
print ("A choice of cheese: cheddar, swiss, provolone, american")
print ("A choice of toppings: lettuce, tomato, onion, pickles, mustard, mayo")
print("A choice of sides: crisps, fruit, cookie, salad")

print("10. 2 Cookies - £1.99")
print("11. 1 cookie - £1.00")
print("12. 1 piece of fruit - £1.67")
print("13. Done ordering")
print("14. Exit")

order = []
total = 0.0
while True:
    choice = int(input("Please enter the number that corresponds to your choice (1-18): "))
    if choice == 1:
        order.append("Coffee - £2.00")
        total += 2.00
        print("Coffee added to your order.")
    elif choice == 2:
        order.append("Tea - £1.50")
        total += 1.50
        print("Tea added to your order.")
    elif choice == 3:
        order.append("milk - £1.00")
        total += 1.00
        print("milk added to your order.")
    elif choice == 4:
        order.append("Juice - £2.50")
        total += 2.50
        print("Juice added to your order.")
    elif choice == 5:
        order.append("Water - £1.00")
        total += 1.00
        print("Water added to your order.")
    elif choice == 6:
        order.append("cake - £3.00")
        total += 3.00
        print("cake added to your order.")
    elif choice == 7:
        order.append("sandwich - £5.00")
        total += 5.00
        print("sandwich added to your order.")
    elif choice == 8:
        order.append("salad - £4.00")
        total += 4.00
        print("salad added to your order.")
    elif choice == 9:
        order.append("create your own killer sandwich - £7.00")
        total += 7.00
        print("create your own killer sandwich added to your order.")
        print("Please choose your bread:")
        bread = input("Bread (white, wheat, rye, sourdough): ")
        print("Please choose your protein:")
        protein = input("Protein (turkey, ham, roast beef, chicken, tofu): ")
        print("Please choose your cheese:")
        cheese = input("Cheese (cheddar, swiss, provolone, american): ")
        print("Please choose your toppings (you can choose multiple, separated by commas):")
        toppings = input("Toppings (lettuce, tomato, onion, pickles, mustard, mayo): ")
        print("Please choose your side:")
        side = input("Side (crisps, fruit, cookie, or a salad): ")
        print("Your killer sandwich with", bread, "bread", protein, cheese, "cheese, toppings: ",toppings, "and a side of", side, "has been added to your order.")
    elif choice == 10:
        order.append("2 Cookies - £1.99")
        total += 1.99
        print("2 Cookies added to your order.")
    elif choice == 11:
        order.append("1 cookie - £1.00")
        total += 1.00
        print("1 cookie added to your order.")
    elif choice == 12:
        order.append("1 piece of fruit - £1.67")
        total += 1.67
        print("1 piece of fruit added to your order.")
    elif choice == 13:
        print("You have finished ordering.")
        print("Here is your order summary:")
        for item in order:
            print("-", item)
        print("Total amount due: £{total:.2f}")
        print("How many people are splitting the bill?")
        num_people = int(input("Number of people: "))
        if num_people > 1:
            split_total = total / num_people
            print("Each person owes: £{split_total:.2f}")
            print("Please choose a payment method:")
            print("1. Cash")
            print("2. Card")
            payment_method = int(input("Payment method (1 or 2): "))
            if payment_method == 1:
                print("Please pay the cashier.")
            elif payment_method == 2:
                print("Please proceed to the card machine.")
            else:
                print("Invalid payment method selected.")
        else:
            print("Please choose a payment method:")
            print("1. Cash")
            print("2. Card")
            payment_method = int(input("Payment method (1 or 2): "))
            if payment_method == 1:
                print("Please pay the cashier.")
            elif payment_method == 2:
                print("Please proceed to the card machine.")
            else:
                print("Invalid payment method selected.")
    if choice == 14:
        print("Thank you for visiting the Basement Cafe. You cannot escape!")
        print("(-_-)(o_o)(^_^)(>_<)(T_T)(^_~)(-_-)(^_^)(^o^)(^o^)(^o^)(£_£)")
        break