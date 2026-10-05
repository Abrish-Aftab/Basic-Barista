import time
print("Hey, welcome to our coffee shop!!!!")
time.sleep(1.5)
print("Here is the menu for you.\n")
time.sleep(1)
menu = """Black Coffee : 6$
Latte : 10$
Cappuccino : 8$
Espresso : 6$
Frappuccino : 13$"""
print(menu)
time.sleep(3)


item = input("\nWhat would u like?  ")
time.sleep(1)
if (item == "Latte"):
  cream = input("Would you like whipped cream?  ")
  if (cream == "Yes"):
    price = 12
    time.sleep(1)
    print("Okay!")
  elif (cream == "yes"):
    price = 12
    time.sleep(1)
    print("Okay!")
  else:
    time.sleep(1)
    print("Okay")
    price = 10
elif (item == "Frappuccino"):
  price = 13
elif (item == "Cappuccino"):
  price = 8
else:
  price = 6

name = input("Can I get a name for your order?  ")
time.sleep(1)

quantity = int(input("How many coffees do you want?  "))
total = price*quantity


if(quantity == 1):
  time.sleep(1)
  print(f"\nOkay {name}, your {item} will be ready in a moment.\n")
  time.sleep(6)
  print(f"\n{name}, your {item} is ready! Your total will be {total}$")
elif (quantity == 0) :
  print("okay? bye")
  exit()
else:
  if (quantity > 10):
    time.sleep(0.5)
    print("Thats a big order! Wait a while please")
    time.sleep(12)
    print(f"\n{name}, your {item}s are ready! Your total will be {total}$")
  else:
    time.sleep(1)
    print(f"\nOkay {name}, your {item}s will be ready in a moment.\n")
    time.sleep(6)
    print(f"\n{name}, your {item}s are ready! Your total will be {total}$")

