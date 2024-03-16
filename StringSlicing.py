# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Het Kothari"

# first_name = name[:3]   # prints the same
first_name = name[0:3]

# last_name = name[4:]    # prints the same
last_name = name[4:11]

# funky_name = name[::2]  #  prints the same
funky_name = name[0:11:2]

reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)
print()

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7, -4)   # removes the url portions

print(website1[slice])
print(website2[slice])
