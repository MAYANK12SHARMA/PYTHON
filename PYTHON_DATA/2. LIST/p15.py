# #?                                LIST FUNCTION
# !     Topic:- sorted()

# ? If you want to sort a list without modifying the original list, you can use the sorted() function:
# ! SYNTAX :-  sorted_list = sorted(orignal_list)
numbers = [5, 2, 8, 1, 3]

# Create a new sorted list without modifying the original
sorted_numbers = sorted(numbers)

print(sorted_numbers)
# Output: [1, 2, 3, 5, 8]

print(numbers)
# Output: [5, 2, 8, 1, 3] (original list is not modified)
