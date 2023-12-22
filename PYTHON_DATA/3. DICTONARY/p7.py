# #?          Dictonary Methods
# ?                            TOPIC :- keys()

# ? there is a keys() method that returns a view of the dictionary's keys.

#! SYNTAX :-  dict_keys = my_dict.keys()


# Creating a dictionary
my_dict = {'name': 'John Doe', 'age': 25, 'city': 'Example City'}

# Using keys() to get a view of keys
dict_keys = my_dict.keys()

# Displaying the view as a list
print(list(dict_keys))

print("___________________________________________________________________________________\n")

# Iterating over keys using keys()
for key in my_dict.keys():
    print(key)
