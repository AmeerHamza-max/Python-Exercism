# dictionary = a collection of {key:value} pairs ordered and
#               changeable. No duplicates


capitals = {"USA":"Washington D.C.",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow",
            }

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("India"))
# print(capitals.get("Japan"))

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")


# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()
# keys=capitals.keys()
# print(keys)

# for key in capitals.keys():
#     print(key)

values=capitals.values()
print(values)

for value in capitals.values():
    print(value)

items=capitals.items()
print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")




menu={
    "pizza":3.00,
    "nachos":4.50,
    "popcorn":6.00,
    "fries":2.5,
    "chips":1.00,
    "pretzel":3.50,
    "soda":3.00,
    "lemonade":4.25
      }

cart= []
total=0

print("------------- Menu -----------------")
for key,value in menu.items():
    print(f"{key}: {value:.2f}")

print("------------- Menu ---------------")
print()
while True:
    food=input("Select an item (q to quit): ").lower()
    if food== "q":
        break
    elif (menu.get(food)) is not None:
        cart.append(food) 

print("-------- Your Order ----------")   

for food in cart:
    total+= menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")