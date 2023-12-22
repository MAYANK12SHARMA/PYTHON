#                           Topic :- Formal and Actual Argument
#?      Positional Argument

#? A positional argument is a type of argument in a function that is passed based on its position or order in the function call. The values passed to the function are assigned to the parameters in the order they appear.



def greet_person(greeting, person_name):
    """
    A function to greet a person.

    Parameters:
    - greeting (str): The greeting message.
    - person_name (str): The name of the person to be greeted.
    """
    print(f"{greeting} {person_name}")

greet_person("hello", "mayank")

# The order of arguments matters in positional arguments.
greet_person("mayank", "hello")
