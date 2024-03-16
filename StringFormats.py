# str.format() = optional method that gives users
#                more control when displaying output

# animal = "cow"
# item = "moon"

# print("The " +animal+ " jumped over the "+item)
# print("The {} jumped over the {}".format("cow", "moon"))
# print("The {1} jumped over the {0}".format(animal, item))    # positional argument
# print("The {animal} jumped over the {animal}".format(animal="cow", item="moon"))   # keyword argument

# text = "The {} jumped over the {}"
# print(text.format(animal, item))



name = "Het"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))   # generates panning that is spacing
print("Hello, my name is {:<10}. Nice to meet you".format(name))  # using '<' left aligns the panning i.e default
print("Hello, my name is {:>10}. Nice to meet you".format(name))  # using '>' right aligns the panning
print("Hello, my name is {:^10}. Nice to meet you".format(name))  # using '^' center aligns the panning


