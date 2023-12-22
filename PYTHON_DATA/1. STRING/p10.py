# #?    Function in string          
#!                                                   topic :- split()

# ? The split() method is used to split a string into a list of substrings based on a specified delimiter.

# ! SYNTAX :- string.split(separator, maxsplit)
#? separator (optional): The delimiter character or substring. If not specified, any whitespace (spaces, tabs, and newlines) is used as the default separator.
#? maxsplit (optional): The maximum number of splits to perform. If specified, the string is split at most maxsplit times.

# Define a string containing comma-separated values
string_1 = 'hii, how, are, you'

# Define another string containing space-separated values
string_2 = '1 2 3 4 5 6 7 8 9 10'

# Use the split method to create a list by splitting the string at commas
list_1 = string_1.split(',')

# Print the resulting list
print(list_1)

# Use the split method to create a list by splitting the string at spaces
list_2 = string_2.split(' ',maxsplit = 6)

# Print the resulting list
print(list_2)
