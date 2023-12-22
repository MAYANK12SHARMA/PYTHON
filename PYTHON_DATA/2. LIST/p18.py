# #?                                LIST FUNCTION
# !     Topic:- del()

# ? The del statement in Python is used to delete elements from a list or delete an entire list itself. It is not a list method like clear() or remove(); instead, it is a general-purpose statement that can be used to delete various objects, including list elements.
# ! SYNTAX :- del list_name ---> for complete list
# ! SYNTAX :- del list_name[i] --->  i means index.


numbers = [1, 2, 3, 4, 5]

# Delete the entire list
del numbers

# Attempting to print the list after deletion will raise a NameError
# print(numbers)
# Output: NameError: name 'numbers' is not defined
