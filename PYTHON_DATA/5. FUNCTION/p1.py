#                                       Topic :- Function Parameters:

#?  Functions can take parameters, which are values passed to the function when it is called. Parameters are specified within the parentheses in the function definition.

def power(a, b):
    c = a ** b
    print(f"The {a}^{b} is: {c}")

# Calling the power function and storing the result in a variable
result = power(4, 2)

# Calling the power function again without storing the result
power(4, 2)

# Printing the result obtained from the first function call
print(result)
