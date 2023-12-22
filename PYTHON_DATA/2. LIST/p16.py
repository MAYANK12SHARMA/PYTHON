# #?                                LIST FUNCTION
# !     Topic:- reverse()

# ? The reverse() method in Python is a list method used to reverse the elements of a list in place. It modifies the original list by reversing the order of its elements

# ! SYNTAX :- list.reverse()

numbers = [1, 2, 3, 4, 5]

# Reverse the order of elements in the list
numbers.reverse()

print(numbers)
# Output: [5, 4, 3, 2, 1]


# ? If you want to create a new list with reversed elements without modifying the original list, you can use slicing:

num1 = [1, 2, 3, 4, 5]

# Create a new list with reversed elements without modifying the original
reversed_numbers = num1[::-1]

print(reversed_numbers)
# Output: [5, 4, 3, 2, 1]

print(num1)
# Output: [1, 2, 3, 4, 5] (original list is not modified)
