# #?          Dictonary Methods
# ?                            TOPIC :- setdefault()

# ? the setdefault() method is used to retrieve the value of a specified key from a dictionary. If the key is present, it returns the corresponding value. If the key is not present, it inserts the key with a specified default value and returns that value.


#! SYNTAX :- value = my_dict.setdefault(key, default)

#! key: The key whose value you want to retrieve or set.
#! default (optional): The value to be set for the key if the key is not present. If not provided, None is used as the default value.

# Creating a dictionary
my_dict = {'name': 'John Doe', 'age': 25, 'city': 'Example City'}

# Using setdefault() to retrieve a value
age = my_dict.setdefault('age', 30)

# Using setdefault() to set a default value for a new key
occupation = my_dict.setdefault('occupation', 'Software Engineer')

# Displaying the retrieved values and the updated dictionary
print("Retrieved Age:", age)
print("Set Default Occupation:", occupation)
print("Updated Dictionary:", my_dict)
