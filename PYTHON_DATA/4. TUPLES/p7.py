# #?                           Topic :- Function  on tuples 

#?    count() function

#? In Python, the count() method is used to count the number of occurrences of a specific element in a tuple

#! SYNTAX :- tuple_name.count(element)

#? tuple_name: The tuple in which you want to count occurrences.
#? element: The element whose occurrences you want to count 

#! Keep in mind that if the specified element is not present in the tuple, the count() method will return 0.

# Creating a tuple
my_tuple = (1, 2, 3, 1, 4, 1, 5)

# Counting occurrences of the element 1 in the tuple
count_of_1 = my_tuple.count(1)

# Printing the result

print(my_tuple)
print("Count of 1 in the tuple:", count_of_1)  # Output: 3
