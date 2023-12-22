 #?In Python, a function is a block of organized, reusable code that performs a specific task. Functions provide a way to modularize your code, making it more readable, maintainable, and efficient. Here's a basic overview of defining and using functions in Python:

 #! Defining a Function:
 
#?  You can define a function using the def keyword, followed by the function name and a set of parentheses. Any parameters the function takes are specified within the parentheses. The function body is indented


def greet(name):
    """This function prints a greeting."""
    print(f"Hello, {name}!")

# Calling the function
greet("Alice")
# Accessing the docstring
print(greet.__doc__)



#!  dynamic typing in python not in c and java

#? Dynamic typing in Python is a feature that allows you to assign values to variables without explicitly specifying their data types. This is in contrast to statically-typed languages like C and Java, where you must declare the data type of a variable before using it, and the type is typically fixed throughout the program.


#!  function can return multiple value in python not  in java or in c 

#?  In Python, a function can return multiple values as a tuple, and you can easily unpack these values when calling the function. This is a feature commonly used in Python but is not directly supported in languages like Java or C.

def get_coordinates():
    x = 10
    y = 20
    z = 30
    return x, y, z

# Calling the function and unpacking the result
result_x, result_y, result_z = get_coordinates()

# Printing the results
print("X coordinate:", result_x)
print("Y coordinate:", result_y)
print("Z coordinate:", result_z)
