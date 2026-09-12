
menu = {
    'pizza': 40,
    'pasta': 60,
    'burger': 40,
    'salad': 50,
    'coffee': 80,
    'tea': 30
}

print("================================")
print("   Welcome to Riddhi's Restaurant")
print("================================")

order_number = 1001
table_number = input("Enter table number: ")

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


# Bill
print("\n==============================")
print("          YOUR BILL")
print("==============================")
print(f"Order Number : {order_number}")
print(f"Table Number : {table_number}")
print("------------------------------")

for item, quantity in order.items():
    price = menu[item]
    total = price * quantity
    print(f"{item.title():10} x {quantity} = Rs.{total}")

print("------------------------------")
print(f"Subtotal: Rs.{order_total}")

# GST
gst = order_total * 0.05
final_total = order_total + gst

print(f"GST (5%): Rs.{gst:.2f}")
print(f"Total: Rs.{final_total:.2f}")
print("==============================")
print("Thank you for visiting!")

