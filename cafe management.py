
menu = {
    'pizza': 40,
    'pasta': 60,
    'burger': 40,
    'salad': 50,
    'coffee': 80,
    'tea': 30,
    'Avacado toast':80,
    'icecream':60
}

print("================================")
print("   Welcome to Riddhi's Cafe!")
print("================================")
customer_name=(input("Enter customer's name:"))
order_number = 1001
table_number = input("Enter table number: ")
print(f"Customer Name:{customer_name}")
print(f"\nOrder Number: {order_number}")
print(f"Table Number: {table_number}")

print("\n----- MENU -----")
for item, price in menu.items():
    print(f"{item.title():10} Rs.{price}")

order = {}
order_total = 0

while True:
    item = input("\nEnter the item you want to order: ").lower().strip()

    if item in menu:
        quantity = int(input("Enter quantity: "))

        if item in order:
            order[item] += quantity
        else:
            order[item] = quantity

        item_total = menu[item] * quantity
        order_total += item_total

        print(f"{quantity} {item}(s) added to your order.")

    else:
        print(f"Sorry, {item} is not available.")

    another_order = input("Do you want to add another item? (yes/no): ").lower()

    if another_order != "yes":
        break

print("\n==============================")
print("          YOUR BILL")
print("==============================")
print(f"Customer Name:{customer_name}")
print(f"Order Number : {order_number}")
print(f"Table Number : {table_number}")


for item, quantity in order.items():
    price = menu[item]
    total = price * quantity
    print(f"{item.title():10} x {quantity} = Rs.{total}")

print("------------------------------")
print(f"Subtotal: Rs.{order_total}")
print(input("Enter the mode of payment(Upi/cash/card):"))
print("Payment Successful!")
print("Thanks For Using the Cafe Management system!")
