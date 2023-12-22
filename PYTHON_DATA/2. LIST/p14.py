# #?                                LIST FUNCTION
# !     Topic:- sort()

# ? The sort() method is used to sort the elements of a list in ascending order.

# ! SYNTAX : - list.sort(key=None, reverse=False)

# ? key (optional): A function to execute to decide the order. Default is None.
# ? reverse (optional): A Boolean. If True, the list is sorted in descending order. Default is False.

numbers = [5, 2, 8, 1, 3]

# Sort the list in ascending order
numbers.sort()

print(numbers)

# ? You can also use the reverse parameter to sort the list in descending order:

num1= [5, 2, 8, 1, 3]

# Sort the list in descending order
num1.sort(reverse=True)

print(num1)
