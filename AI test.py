def display_menu(menu):
    print("\n----- Café Menu -----")
    for item, price in menu.items():
        print(f"{item.title()}: ${price:.2f}")
    print("----------------------\n")

def take_order(menu):
    order = {}
    while True:
        item = input("Enter item to order (or 'done' to finish): ").lower()
        if item == 'done':
            break
        if item in menu:
            qty = int(input(f"How many {item}(s)?: "))
            order[item] = order.get(item, 0) + qty
        else:
            print("Item not on menu.")
    return order

def calculate_total(order, menu, tax_rate=0.07, tip_rate=0.15):
    subtotal = sum(menu[item] * qty for item, qty in order.items())
    tax = subtotal * tax_rate
    tip = subtotal * tip_rate
    total = subtotal + tax + tip
    return round(subtotal, 2), round(tax, 2), round(tip, 2), round(total, 2)

def split_bill(total, num_people):
    return round(total / num_people, 2)

def accept_payment(amount_due):
    while True:
        paid = float(input(f"Enter payment amount ($): "))
        if paid >= amount_due:
            change = round(paid - amount_due, 2)
            print(f"Payment accepted. Change: ${change:.2f}")
            break
        else:
            print(f"Insufficient payment. ${amount_due - paid:.2f} more needed.")
    return paid

def main():
    menu = {
        "coffee": 3.50,
        "tea": 2.75,
        "sandwich": 5.25,
        "cake": 4.00,
        "juice": 3.00
    }

    display_menu(menu)
    order = take_order(menu)

    if not order:
        print("No items ordered.")
        return

    subtotal, tax, tip, total = calculate_total(order, menu)

    print("\n----- Bill Summary -----")
    print(f"Subtotal: ${subtotal}")
    print(f"Tax (7%): ${tax}")
    print(f"Tip (15%): ${tip}")
    print(f"Total: ${total}")
    print("------------------------")

    split = input("Would you like to split the bill? (yes/no): ").lower()
    if split == 'yes':
        people = int(input("Enter number of people to split the bill: "))
        amount_per_person = split_bill(total, people)
        print(f"Each person owes: ${amount_per_person}")
    else:
        people = 1
        amount_per_person = total

    for person in range(1, people + 1):
        print(f"\n--- Payment for Person {person} ---")
        accept_payment(amount_per_person)

    print("\nThank you for visiting our café!")

if __name__ == "__main__":
    main()
