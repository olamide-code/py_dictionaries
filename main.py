  #PYTHON CODE FOR A MENU/CART
#..............................

menu = {
    "Rice" : 4.0,
    "Beans" : 6.0,
    "Yam" : 7.0,
    "Spaghetti" : 3.0,
    "Fish" : 4.0,
    "Plantain" : 5.0,
    "Potato" : 4.0
   }

cart = []
total = 0

print("...........MENU............")

for key, value in menu.items():
    print(f"{key:10}: ${value: .2f}")

print("...........................")

while True:
    food = input("Select a food to eat or (q to quit): \n").title()

    if food == "Q":
        break

    elif menu.get(food) is not None:
        cart.append(food)
print("****************YOUR ORDERS*********************")
for food in cart:
        total += menu.get(food)    
        print(food, end=" ")

print()
print(f"Total is: ${total: .2f}")
