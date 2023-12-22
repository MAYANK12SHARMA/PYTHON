#                           Topic :- Formal and Actual Argument
#?     keyword Argument

#? A keyword argument is a type of argument in a function call that is passed by explicitly naming the parameter to which the argument corresponds. Unlike positional arguments, where the values are matched based on their order, keyword arguments are matched based on the parameter names.


# Define a function named 'groceries' that takes two parameters: 'item' and 'price'
def groceries(item, price):
    # Print a formatted string with the name of the item and its price
    print(f"The item {item} is priced at {price:.2f} rupees.")

# Call the function without providing any arguments (will result in an error)
# grocerries()

# Call the function with positional arguments for 'item' and 'price'
groceries('apples', 100)

# Call the function with keyword arguments for 'item' and 'price'
groceries(price=120,item='banana')
