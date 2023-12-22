# #?    Function in string          
#!                                                   topic :- index()

#?Similar to find(), but raises a ValueError if the substring is not found.
#?Returns the lowest index in the string where the substring is found.
#?Optional parameters start and end can be used to specify the search range within the string.

# !  SYNTAX :- string_name.index("substring",start,end)

# Define a string
input_string = "hii! bro whats up"

# Find the index of the character 'q' in the string
index_of_q = input_string.index("q")               # show error becouse q is not exist in string

# Find the index of the character 'w' in the string
index_of_w = input_string.index("w")

# Print the result
print(index_of_q)

# Print the result
print(index_of_w)
