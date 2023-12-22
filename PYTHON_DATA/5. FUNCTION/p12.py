#                                               Topic :- Map function

#? The map() function in Python is used to apply a specified function to all items in an iterable (e.g., a list) and return an iterator that produces the results.

#!    SYNTAX :-     map(function, iterable, ...)

#? function: The function to apply to each item in the iterable.
#? iterable: The iterable (e.g., list, tuple, etc.) whose elements will be processed by the function.   

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use the map() function to square each number in the list
squared_numbers = map(lambda x: x**2, numbers)

# Convert the result to a list (for demonstration purposes, as map() returns an iterator)
squared_numbers_list = list(squared_numbers)

# Print the original and squared lists
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers_list)
