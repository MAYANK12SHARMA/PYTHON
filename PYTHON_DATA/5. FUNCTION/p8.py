#                           Topic :- Local and Global Variable

#!  Global Variables:

#?  Definition: A variable declared outside any function or block of code.

#? Scope: Accessible throughout the entire code, both inside and outside functions.

# Global variable
global_variable = 10

def simple_access():
    # Function to demonstrate simple access to the global variable
    print("Inside simple_access function:", global_variable)

def modify_global_with_global_keyword():
    # Function to modify the global variable using the global keyword
    global global_variable  # Declare that we are using the global variable
    global_variable = 20    # Modify the global variable within the function

def modify_global_without_global_keyword():
    # Function to modify the global variable without using the global keyword
    # This actually creates a new local variable with the same name
    global_variable = 30
    print("Inside modify_global_without_global_keyword function (local variable):", global_variable)

# Demonstrate simple access to the global variable
simple_access()

# Use the function with the global keyword to modify the global variable
modify_global_with_global_keyword()
print("Global variable after modification with global keyword:", global_variable)

# Use the function without the global keyword (creates a new local variable)
modify_global_without_global_keyword()
print("Global variable after modification without global keyword:", global_variable)

