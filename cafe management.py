menu= {
     'pizza': 40,
     'pasta':60,
     'burger':40,
     'salad':50,
     'coffee':80,
     'tea':30,   
}
print("welcome to Riddhi's Restraurant")
print("pizza:rs40\npasta:rs60\nburger:rs40\ncoffee:rs80\nsalad:rs50\ntea:30")
order_total=0
item_1=input("enter the name of item you want to order=")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"yout item {item_1} has been added to your order ")
else:
    print(f"ordered item {item_1} is not available yet.")
another_order= input("Do you want to add another item?(yes/no)")
if another_order=="yes":
    item_2=input("enter the name of second item=")
    if item_2 in menu:
     order_total+=menu[item_2]
     print(f"Item{item_2}has been added to order")
    else:
      print(f"ordered item{item_2}is not available!") 
print(f"The total amount of items to pay is {order_total}")


