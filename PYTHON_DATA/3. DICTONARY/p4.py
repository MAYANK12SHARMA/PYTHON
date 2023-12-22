# #?          Dictonary Methods
# ?                            TOPIC :- fromkeys()

# ? the fromkeys() method is a class method that returns a new dictionary with keys from a given iterable (such as a list) and a default value for all keys. 

# ! SYNTAX :- new_dictonary =  dict.fromkeys(iterable, value) 

# ? iterable: The iterable (list, tuple, etc.) whose elements will become the keys of the new dictionary.
# ?value: The default value to be assigned to each key in the new dictionary.

# Using fromkeys() to create a dictionary with default values
keys = ['name', 'age', 'city']
default_value = 'radhe'

my_dict = dict.fromkeys(keys, default_value)

# Displaying the created dictionary
print(my_dict)