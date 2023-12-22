# #?          Dictonary Methods
# ?                            TOPIC :- pop()

# ? the pop() method is used to remove and return the value associated with a specified key from a dictionary.

#! SYNTAX :- value = my_dict.pop(key, default)
#? key: The key whose associated value is to be removed and returned.
# ? default (optional): If the key is not found, the pop() method returns this value. If not provided, a KeyError is raised when the key is not found

# Creating a dictionary
my_dict = {'name': 'John Doe', 'age': 25, 'city': 'Example City'}

# Using pop() to remove and return the value associated with a key
age = my_dict.pop('age', 'key not found')
occupation = my_dict.pop('occupation', 'key not found')

# Displaying the removed value and the updated dictionary
print("Removed Age:", age)
print("Removed occupation:", occupation)
print("Updated Dictionary:", my_dict)
