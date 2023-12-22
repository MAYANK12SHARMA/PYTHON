#                           Topic :- Formal and Actual Argument
#?      Variable Length Argument

#? Variable-length arguments in a Python function allow you to pass a variable number of arguments to the function. 
# There are two types of variable-length arguments: *args for positional arguments and **kwargs for keyword arguments.

#! *args (Variable-Length Positional Arguments):

#? The *args syntax in a function definition allows you to pass any number of positional arguments. Inside the function, args becomes a **tuple** containing all the passed values.

def sum_all(*args):
    """A function that sums all the passed numbers."""
    total = sum(args)
    # OR 
    # sum = 0
    # for i in args:
        # sum = sum+i
    # return sum 
    return total

# Using variable-length positional arguments
result = sum_all(1, 2, 3, 4, 5)
print("Sum:", result)

#! kwargs (Variable-Length Keyword Arguments):
#? The **kwargs syntax in a function definition allows you to pass any number of keyword arguments. Inside the function, kwargs becomes a **dictionary** containing all the passed key-value pairs.

def display_info(**kwargs):
    
    """A function that displays information based on keyword arguments."""
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Using variable-length keyword arguments
display_info(name="Alice", age=25, country="USA")


#! Combining *args and **kwargs:
#? You can also combine both variable-length positional and keyword arguments in a single function definition.

def display_info_combined(*args, **kwargs):
    """A function that displays information based on both positional and keyword arguments."""
    for arg in args:
        print("Positional argument:", arg)
    for key, value in kwargs.items():
        print(f"Keyword argument - {key}: {value}")

# Using both variable-length positional and keyword arguments
display_info_combined("Alice", 25, country="USA", occupation="Engineer")
