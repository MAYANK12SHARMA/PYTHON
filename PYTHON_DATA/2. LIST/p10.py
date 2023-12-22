# #?                                LIST FUNCTION
# !     Topic:- extend()

# ? The extend() method in Python is a list method used to extend a list by appending elements from an iterable. The iterable could be another list, tuple, string, or any other iterable. 

#! SYNTAX :- list_in_which_you_append.list(list_that_to_be_append)

fruits = ['apple', 'banana', 'orange']
additional_fruits = ['kiwi', 'grape', 'watermelon']

fruits.extend(additional_fruits)

print(fruits)
