# #?          Dictonary Methods
# ?                            TOPIC :- update()

# ?  the update() method is used to update a dictionary with elements from another dictionary or from an iterable of key-value pairs.

#! SYNTAX :-  dict1.update(dict2)

# ? dict1 = dictonary in which data is going to be add.
# ? dict2 = dictonary which idsgoing to be add. 

# ? iterable_or_dict: An iterable of key-value pairs or another dictionary whose elements will be added to the calling dictionary.

# Creating an initial dictionary
my_dict = {'name': 'John Doe', 'age': 25, 'city': 'Example City'}

# Creating another dictionary with additional data
additional_data = {'occupation': 'Software Engineer', 'salary': 50000}

# Using update() to add elements from another dictionary
my_dict.update(additional_data)

# Displaying the updated dictionary
print(my_dict)
