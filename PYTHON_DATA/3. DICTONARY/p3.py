# #?          Dictonary Methods
# ?                            TOPIC :- copy()

# ? you can create a copy of a dictionary using the copy() method or by using the dict() constructor.

# !Both copy_dict_method1 and copy_dict_method2 are independent copies of the original dictionary original_dict. Changes to one dictionary will not affect the others.

# ! SYNTAX : - new_dictonary = original_dictonary.copy()

# ! SYNTAX : - new_dictonary = dict(original_dictonary)

# Original dictionary
original_dict = {'name': 'John Doe', 'age': 25, 'city': 'Example City', 'occupation': 'Software Engineer'}

# Method 1: Using the copy() method
copy_dict_method1 = original_dict.copy()

# Method 2: Using the dict() constructor
copy_dict_method2 = dict(original_dict)

# Displaying the original and copied dictionaries
print("Original Dictionary:", original_dict)
print("Copy using copy() method:", copy_dict_method1)
print("Copy using dict() constructor:", copy_dict_method2)

