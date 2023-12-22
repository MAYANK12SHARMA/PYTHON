# #?    Function in string          
#!                                                   topic :- rindex()

#?  Similar to index(), but searches for the last occurrence of the substring.
#? Returns the highest index in the string where the substring is found.
#? Raises a ValueError if the substring is not found.
#? Optional parameters start and end can be used to specify the search range within the string.

# !  SYNTAX :- string_name.rindex("substring",start,end)

# Define a string
input_string = "hii! u bro whats up"

# Find the rindex of the character 'q' in the string
index_of_q = input_string.rindex("q")               # show error becouse q is not exist in string

# Find the rindex of the character 'w' in the string
index_of_w = input_string.rindex("w")

# Print the result
print(index_of_q)

# Print the result
print(index_of_w)