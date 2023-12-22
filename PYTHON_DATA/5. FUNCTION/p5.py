#                           Topic :- Formal and Actual Argument
#?     Default Argument

#? Default arguments in Python are parameters in a function that have a default value. If the caller of the function doesn't provide a value for these parameters, the default value is used


# Function definition with default parameter values
def greet(name='mayank', greeting='hello'):
    """
    Greets a person with a specified greeting and name.

    Parameters:
    - name (str): The name of the person to greet (default is 'mayank').
    - greeting (str): The greeting message to use (default is 'hello').
    """
    print(f"{greeting} {name}")

# Example 1: Greeting with custom values
greet(name='suraj', greeting='hii')
# Output: hii suraj

# Example 2: Greeting with default values
greet()
# Output: hello mayank
