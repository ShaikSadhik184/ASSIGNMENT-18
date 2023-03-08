# create two lists
keys = ["name", "age", "gender"]
values = ["John Smith", 30, "male"]

# create an empty dictionary
my_dict = {}

# use a loop to add items to the dictionary
for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

# print the resulting dictionary
print(my_dict)
