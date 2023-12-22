#                                        Topic :- Return Statement:

 #?  The return statement is used to exit a function and return a value. If no return statement is present, the function returns None by default.
 
def square(x):
    """This function returns the square of a number."""
    return x ** 2

# Calling the function and using the returned value
result = square(4)
print("Square:", result)
