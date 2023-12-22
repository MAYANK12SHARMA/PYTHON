#                                               Topic :- Lambda Function

#? A lambda function in Python is a way to create anonymous functions, which are functions without a name. They are also referred to as lambda expressions.

#!   SYNTAX : - lambda arguments: expression

#? lambda: Keyword used to define a lambda function.
#? arguments: Comma-separated list of input parameters.
#? expression: Single expression that is evaluated and returned.

add = lambda x, y: x + y
result = add(3, 5)
print(result)  


print("\n*******************************************************************\n")


# Lambda function to calculate the square of a number
square = lambda x: x**2

# Using the lambda function to calculate the square of 5
number = square(5)

# Printing the result
print(number)  # Output: 25


print("\n*******************************************************************\n")


bigger = lambda x,y : x if (x>y) else y

bigger_number = bigger(45,65)

print(bigger_number)