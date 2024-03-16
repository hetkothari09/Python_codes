# set = collection which is unordered, unindexed. No duplicate values

utensils = {"forks", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("Napkin")
# utensils.remove("forks")
# utensils.clear()
# utensils.update(dishes)    # adds all elements of dishes to utensils
dinner_table = utensils.union(dishes)

for x in dinner_table:
    print(x)

print(dishes.difference(utensils))
print(utensils.intersection(dishes))
