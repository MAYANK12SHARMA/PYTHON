#                               Topic :- Runtime - error

#?  A runtime error, also known as an exception, occurs during the execution of a program. Unlike compile-time errors, runtime errors are not detected until the program is running. These errors can happen due to a variety of reasons, such as invalid input, division by zero, or attempting to access an index that does not exist.


#? ZeroDivisionError:

#! Occurs when dividing a number by zero.

result = 10 / 0

#? TypeError:

#! Occurs when an operation is performed on an object of an inappropriate type.

result = "Hello" + 42  # Attempting to concatenate a string and an integer


#? IndexError:

#!  Occurs when trying to access an index that is outside the bounds of a sequence (e.g., a list).

my_list = [1, 2, 3]
value = my_list[10]  # Attempting to access an index beyond the length of the list


#? KeyError:

#!  Occurs when trying to access a dictionary key that does not exist.

my_dict = {'name': 'Alice', 'age': 30}
value = my_dict['gender']  # Attempting to access a key that does not exist

