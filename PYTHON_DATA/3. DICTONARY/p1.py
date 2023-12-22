# CREATING A DICTONARY

dict1 = {
    'id':1,
    'name':'Mayank',
    'course':'B.Tech'
}

# Printing a dictonary 
print("Printing a dictonary :  ",end=' ')
print(dict1)

# Modifying a dictonary 
print("\n Modifying  a dictonary :  ",end=' ')

dict1['course']  = 'C.E.O'
print(dict1)

# adding a data to dictonary

print("\nAdding a data to   a dictonary :  ",end=' ')
dict1['lname'] = 'radhe'
print(dict1)


# ? KEY should be unique

# ? In a Python dictionary, each key must be unique. If you try to add a key that already exists, the new value will overwrite the existing one. This behavior allows dictionaries to efficiently map unique keys to their associated values. Here's an example: 

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
 
# Adding a new key-value pair
my_dict['new_key'] = 'New Value'

# Trying to add a key that already exists
my_dict['key1'] = 'Updated Value'

# Displaying the updated dictionary
print(my_dict)
