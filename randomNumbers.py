import random

# will print random number between 1 and 6
x=random.randint(1, 6)

# will print random number between 0 and 1
y=random.random()

mylist=['Rock', 'Paper', 'Scissor']
z=random.choice(mylist)

# will shuffle the sequence of the elements in the list
cards=[1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
random.shuffle(cards)

print(x)
print(y)
print(z)
print(cards)
