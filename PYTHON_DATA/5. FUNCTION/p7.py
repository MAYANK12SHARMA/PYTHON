#                           Topic :- Local and Global Variable


#! Local Variables:

#? Definition: A variable declared inside a function or a block of code.
#? Scope: Limited to the function or block where it is declared.

def example_function():
    # x is a local variable
    x = 10
    print("Inside function:", x)

example_function()
# Trying to access x outside the function would result in an error

#! print("Outside function:", x)  # This would raise an error(i.e., Name error)
