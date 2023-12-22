# #?    Function in string          

#!                                                   topic :- lstrip()

# ? The lstrip() method removes leading whitespaces from the left side of a string.
# !   >> string_name.lstrip()

user_input = input("Enter the string: ")

# Display the original string using repr() to show special characters
print("Original String:", repr(user_input))

#!  Remove leading whitespaces from the input string using lstrip()
trimmed_input = user_input.lstrip()

print("Trimmed String:", repr(trimmed_input))
