#                                                Topic :- __main__

#? In Python, the special variable __name__ is used to determine whether a Python script is being run as the main program or if it is being imported as a module into another script. This is particularly useful for creating reusable modules that can be either standalone programs or components of larger applications.

#? When a Python script is executed, the __name__ variable is set to '__main__' if the script is the main program being run. If the script is being imported as a module into another script, the __name__ variable is set to the name of the module. 

# module_example.py

def some_function():
    print("Hello from some_function!")

# If this script is being run as the main program
if __name__ == "__main__":
    print("This script is being run directly.")
    some_function()
else:
    print("This script is being imported as a module.")
