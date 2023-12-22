 #?                                     Topic :- Nested tuple
 
#?             sotred nested element


# Creating a nested tuple
nested_tuple = ((3, 'z', 5), (1, 'd', 24), (2, 'b', 16))

# Sorting the nested tuple based on the default (first) element of each inner tuple
sorted_tuple = sorted(nested_tuple)

# Sorting the nested tuple based on the second element of each inner tuple
sorted_tuple_1 = sorted(nested_tuple, key=lambda x: x[1])

# Sorting the nested tuple based on the third element of each inner tuple
sorted_tuple_2 = sorted(nested_tuple, key=lambda x: x[2])

# Printing the results
print("Original nested tuple with index 0:", sorted_tuple)
print("\nSorted nested tuple with index 1:", sorted_tuple_1)
print("\nSorted nested tuple with index 2:", sorted_tuple_2)


