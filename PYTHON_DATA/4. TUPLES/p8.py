 #?                           Topic :- Function  on tuples 

#?       count() function

#? In Python, the index() method is used to find the index of the first occurrence of a specified element in a tuple.

#! SYNTAX :- tuple.index(element, start, end)

#? tuple: The tuple in which you want to find the index.
#? element: The element whose index you want to find.
#? start (optional): The index in the tuple from where the search starts (default is 0).
#? end (optional): The index in the tuple where the search ends (default is the end of the tuple) 

# Creating a tuple
my_tuple = (1, 2, 3, 1, 4, 1, 4, 5)

# Finding the index of the first occurrence of the element 4 in the tuple
index_of_4 = my_tuple.index(4)

index_of_4_from_end= my_tuple.index(4,5,7)

# Printing the result
print("Index of 4 in the tuple:", index_of_4)  # Output: 4

print("Index of 4 in the tuple:", index_of_4_from_end)  # Output: 4

