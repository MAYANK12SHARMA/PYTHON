# #?          Dictonary Methods
# ?                            TOPIC :- fromkeys()

# ?  the get() method is used to retrieve the value of a specified key from a dictionary.

# ! SYNTAX :- value = my_dict.get(key, default)

#? key: The key whose value you want to retrieve.
#? default (optional): The value to return if the key is not found. If not provided, None is returned.

# Creating a dictionary
my_dict = {'name': 'John Doe', 'age': 25, 'city': 'Example City'}

# Using get() to retrieve values
name = my_dict.get('name', 'Not Found')
occupation = my_dict.get('occupation', 'Not Found')

# Displaying the retrieved values
print("Name:", name)
print("Occupation:", occupation)
