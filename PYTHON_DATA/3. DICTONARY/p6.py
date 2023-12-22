# #?          Dictonary Methods
# ?                            TOPIC :- dict.items()

#? the items() method is a dictionary method that returns a view of the dictionary's key-value pairs as tuples.

#! SYNTAX :- dict_items = my_dict.items()

# Creating a dictionary
my_dict = {'name': 'John Doe', 'age': 25, 'city': 'Example City'}

# Using items() to get a view of key-value pairs
dict_items = my_dict.items()

# Displaying the view as a list
print(list(dict_items))

print("__________________________________________________________________________________\n")

# Iterating over key-value pairs using items()
for key, value in my_dict.items():
    print(f"{key}: {value}")
