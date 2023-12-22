# #?    Function in string          
#!                                                   topic :- strip()

#?  The strip() method removes leading and trailing whitespaces from a string.
# !     >> new_string  =  string_name.strip()


# Prompt the user to input a string
user_input = input("Enter the string: ")

# Display the original string using repr() to show special characters
print("Original String:", repr(user_input))

#!  Remove leading and trailing whitespaces from the input string using strip()
trimmed_input = user_input.strip()

# Display the trimmed string using repr()
print("Trimmed String:", repr(trimmed_input))
