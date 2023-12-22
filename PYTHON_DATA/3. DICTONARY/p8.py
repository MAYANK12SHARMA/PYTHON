# #?          Dictonary Methods
# ?                            TOPIC :- values()

# ? the values() method is used to get a view of the dictionary's values. 

#! SYNTAX :-  dict_values = my_dict.values()

# Creating a dictionary
my_dict = {'name': 'John Doe', 'age': 25, 'city': 'Example City'}

# Using values() to get a view of values
dict_values = my_dict.values()

# Displaying the view as a list
print(list(dict_values))

print("__________________________________________________________________________________\n")

# Iterating over values using values()
for value in my_dict.values():
    print(value)

