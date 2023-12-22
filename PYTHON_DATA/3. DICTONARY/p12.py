# #  ?                  LIST TO dictonary

# !  using zip function

# Example lists of keys and values
keys_list = ['name', 'age', 'city']
values_list = ['John Doe', 25, 'Example City']

# Using zip to pair keys and values, and dict to convert to a dictionary
my_dict = dict(zip(keys_list, values_list))

# Displaying the created dictionary
print(my_dict)
             