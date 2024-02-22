# Creating an empty list my_list
my_list = []

# Appending values 10, 20, 30, and 40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# Inserting value 15 at the second position in my_list
my_list[1] = 15
print(my_list)

# Extending my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])
print(my_list)

# Deleting the last item in my_list
del my_list[(len(my_list) - 1)]
print(my_list)

# Sorting my_list in ascending order
my_list.sort
print(my_list)

# Finding and printing the index of the value 30
print(my_list.index(30))
