 #?                           Topic :- Function  on tuples 

#?     min() and max() function in tuples

#? The min() and max() functions in Python are used to find the minimum and maximum values, respectively, from a collection of values

# ! SYNTAX :-  max(tuple_name) and min(tuple_name)

# Creating a tuple of integers
integer_tuple = (5, 12, 3, 8, 20)

# Using min() to find the minimum value in the integer tuple
minimum_value_integer = min(integer_tuple)

# Using max() to find the maximum value in the integer tuple
maximum_value_integer = max(integer_tuple)

# Printing the results for the integer tuple
print("Integer Tuple - Minimum value:", minimum_value_integer)  # Output: 3
print("Integer Tuple - Maximum value:", maximum_value_integer)  # Output: 20


# *************************************************************************************************

# Creating a tuple with mixed types
mixed_tuple = (10, 'apple', 5.5, 'orange', -3)

# Note: Using min() and max() with mixed types can raise TypeError

# Uncomment the lines below to see the TypeError in action
# min_value_mixed = min(mixed_tuple)  
# max_value_mixed = max(mixed_tuple)

# Explanation for the TypeError:
# When a tuple contains different types, the comparison between them is not well-defined
# and can result in a TypeError when using min() and max() functions.

# To avoid TypeError, make sure the elements in the tuple are of the same comparable type.

# If you still want to find the minimum and maximum values for specific types within the mixed tuple,
# you can create a new tuple with only elements of that type, and then apply min() and max() on it.


# ********************************************************************************************************

# Example:
# Extracting only numeric values from the mixed tuple
numeric_values = tuple(item for item in mixed_tuple if isinstance(item, (int, float)))

# Using min() and max() on the numeric tuple
min_value_numeric = min(numeric_values)
max_value_numeric = max(numeric_values)

# Printing the results for the numeric tuple
print("Numeric Tuple - Minimum value:", min_value_numeric)  # Output: -3
print("Numeric Tuple - Maximum value:", max_value_numeric)  # Output: 10



