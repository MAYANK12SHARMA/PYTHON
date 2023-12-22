# #?    Function in string          
#!                                                   topic :- count()

# ? The count() method is used to count the number of occurrences of a specified substring in a given string.

# ! SYNTAX :- string.count(substring, start, end)
#? substring: The substring for which you want to count occurrences.
#? start (optional): The starting index for the search.
#? end (optional): The ending index for the search.

#! If the start and end parameters are provided, count() will count occurrences only within the specified range. If they are omitted, the entire string is searched.

#! Keep in mind that the count() method is case-sensitive, so "hello" and "Hello" would be treated as /different substrings.


text_message = "hii! how are you."

# Define a character to count in the string
character_to_count = 'h'

# Count the occurrences of the specified character 'i' in the string
occurrences_of_character = text_message.count(character_to_count)

# Display the occurrences of the specified character
print(f"Occurrences of '{character_to_count}':", occurrences_of_character)

