# list = used to store multiple items in a single variable

food = ["pizza", "Hamburger", "Pav Bhaji", "Garlic Bread"]

food[1] = "Manchurian"
food.append("Softie")
food.remove("Pav Bhaji")
# food.pop()               # removes the last element
food.insert(0, "Cheese Pizza")
food.sort()
# food.clear()

# print(food[1])

for x in food:
    print(x)