# #?    Function in string          
#!                                                   topic :- replace()

#?  The replace() method is used to replace occurrences of a specified substring with another substring

# ! SYNTAX :- new_string = original_string.replace(old_substring, new_substring, count)

#? original_string: The original string where replacements will be made.
#? old_substring: The substring to be replaced.
#? new_substring: The substring that will replace occurrences of old_substring.
#? count (optional): The number of occurrences to replace. If specified, only the first count occurrences of original_substring will be replaced.

# Given string containing multiple occurrences of "hi"
original_string = "hi alice, Hi krishna, hi radha"

# Replace all occurrences of "hi" with "hello" in the entire string
modified_string = original_string.replace("hi", "hello")

# Replace only the first occurrence of "hi" with "hello" in the string
partial_modified_string = original_string.replace("hi", "hello", 1)

print(modified_string)
print(partial_modified_string)