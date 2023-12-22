# #?    Function in string          
#!                                                   topic :- find()

#? Returns the lowest index in the string where the substring substring is found.
#? If the substring is not found, it returns -1.
#? Optional parameters start and end can be used to specify the search range within the string.

#!  >>  string_name.find(substring, start, end):

# Define a string variable
input_string = "hii! how are you."

# Find the index of the substring "are" in the string
index_of_are = input_string.find("are")

# Print the result
print(index_of_are)

