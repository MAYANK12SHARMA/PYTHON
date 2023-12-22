# #?    Function in string          
#!                                                   topic :- rfind()

#? Similar to find(), but searches for the last occurrence of the substring.
#? Returns the highest index in the string where the substring is found.
#? If the substring is not found, it returns -1.
#? Optional parameters start and end can be used to specify the search range within the string.

# !  SYNTAX :- string_name.rfind("substring",start,stop)
# Given string
text = "hello! good morning all of you"

# Find the last occurrence of "g" in the string
last_occurrence = text.rfind("g")

# Find the last occurrence of "g" within the specified substring (0 to 9)
occurrence_in_substring = text.rfind("g", 0, 9)

# Display the results
print("Last occurrence of 'g' in the string:", last_occurrence)
print("Last occurrence of 'g' in the substring (0 to 9):", occurrence_in_substring)
