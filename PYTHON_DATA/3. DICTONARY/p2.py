# #?          Dictonary Methods
# ?                            TOPIC :- clear()

# ?This method removes all items from the dictionary, making it an empty dictionary.
# !Keep in mind that calling clear() modifies the original dictionary in place. If you want to create a new dictionary with the same variable name, you would need to reassign it or create a new dictionary instance

# !   SYNTAX : - dictonary_name.clear()

# Create a dictionary
my_dict = {'name': 'John Doe', 'age': 25, 'city': 'Example City', 'occupation': 'Software Engineer'}

# Display the original dictionary
print("Original Dictionary:", my_dict)

# Clear all key-value pairs from the dictionary
my_dict.clear()

# Display the dictionary after clearing
print("Dictionary after Clearing:", my_dict)
