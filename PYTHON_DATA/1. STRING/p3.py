# #?    Function in string          
#!                                                   topic :- rstrip() 

# ? The rstrip() method removes trailing whitespaces from the right side of a string.
# !    >> string_name.rstrip()

user_input = input("Enter the string: ")

# Display the original string using repr() to show special characters
print("Original String:", repr(user_input))

#!  Remove leading whitespaces from the input string using lstrip()
trimmed_input = user_input.rstrip()

print("Trimmed String:", repr(trimmed_input))
