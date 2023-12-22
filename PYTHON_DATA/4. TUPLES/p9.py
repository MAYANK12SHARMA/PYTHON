 #?                           Topic :- Function  on tuples 

#?       sorted() function

#? The sorted() function is used to sort the elements of an iterable (e.g., a tuple) and return a new list containing the sorted elements. 

#! It does not modify the original tuple; instead, it creates a new sorted list.

#! SYNTAX :- new_list = sorted(tuple_name, reverse(optional))

#? The sorted() function in Python has a reverse parameter that allows you to specify whether the sorting should be in ascending order (default) or descending order. If you want to sort a tuple in descending order, you can set the reverse parameter to True


# Creating a tuple
my_tuple = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)

# Using sorted() to sort the elements of the tuple
sorted_tuple = sorted(my_tuple)

# Printing the result
print("Original tuple:", my_tuple)
print("Sorted tuple(list):", sorted_tuple)


# conversion list into tuple 

print("sorted tuple : ",tuple(sorted_tuple))

# sortind in deceding order 

print("decending order : ", sorted(reverse = True))


