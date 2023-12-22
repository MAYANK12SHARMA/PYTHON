# #?    Function in string          
#!                                        topic :- sorted():

# ? The sorted() function can be used to sort the characters of a string alphabetically. It returns a new list containing all items from the original iterable (in this case, the characters of the string) in ascending order

# ! SYNTAX : - sorted(string_name,reverse)

# ?reverse(optional) = If reverse is set to True, the items are sorted in reverse order; otherwise, they are sorted in ascending order (the default behavior).


str1 = "121"
sort_str = sorted(str1)
print(sort_str)
sort_string = ''.join(sort_str)
print(sort_string)