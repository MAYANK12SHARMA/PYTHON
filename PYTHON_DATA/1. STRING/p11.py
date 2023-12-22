# #?    Function in string          
#!                                                   topic :- join()

# ? The join() method  combines the elements of an iterable (e.g., a list) into a single string.

#! SYNTAX :- separator.join(iterable)
#? separator: The string that will be used to concatenate the elements of the iterable.
#? iterable: The iterable (e.g.,list, tuple, or string) whose elements will be joined into a single string

# Define a list of words
word_list = ['this', 'is', 'the', 'earth']

# Define a separator
sep = ' '

# Join the words using the separator
result_str = sep.join(word_list)  # Alternatively, can be written as: result_str = ' '.join(word_list)

# Print the result
print(result_str,'\n')
print("_________________________________________________________________________________")

numbers = ("One", "Two", "Three")
result = "-".join(numbers)

print(result)
# Output: "One-Two-Three"
