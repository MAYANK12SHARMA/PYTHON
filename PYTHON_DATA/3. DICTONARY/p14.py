# #  ?                  LIST TO dictonary

# ! without zip function

# Example lists of keys and values
keys_list = ['name', 'age', 'city']
values_list = ['John Doe', 25, 'Example City']

# Creating an empty dictionary
my_dict = {}

# Iterating over the indices of one list
for i in range(len(keys_list)):
    # Assigning key-value pairs to the dictionary
    my_dict[keys_list[i]] = values_list[i]

# Displaying the created dictionary
print(my_dict)
