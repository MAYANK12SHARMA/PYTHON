 #?                                     Topic :- Nested tuple
 
#?             accessing nested element

# Creating a nested tuple
nested_tuple = ((1, 2, 3), ('a', 'b', 'c'), (4, 5, 6))

# Accessing elements in the nested tuple
element_1_2 = nested_tuple[0][1]  # Accessing the element at index 1 in the tuple at index 0
element_a = nested_tuple[1][0]    # Accessing the element at index 0 in the tuple at index 1
element_5 = nested_tuple[2][1]    # Accessing the element at index 1 in the tuple at index 2

# Printing the results
print(element_1_2)  # Output: 2
print(element_a)    # Output: 'a'
print(element_5)    # Output: 5
