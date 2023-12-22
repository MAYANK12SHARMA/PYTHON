#                                                Topic :- Compile-Time error

#? "compile-time error" typically refers to syntax errors or other issues that prevent the Python interpreter from successfully parsing and compiling the source code. When you write a Python script, the interpreter goes through a two-step process: parsing (compiling) and execution.

#? Compile-time errors occur during the parsing (compiling) phase before the program is executed. They are caused by violations of the Python language syntax rules. Some common examples of compile-time errors include: 

# Syntax Errors:

#!  Occur when the code violates the rules of the Python language syntax.

print("Hello, World"  # Missing closing parenthesis
      

#? Indentation Errors:

#! Occur when there are issues with the indentation of the code.

if x > 0:
print("Positive")  # IndentationError: expected an indented block


#?  Invalid Variable Names:

#! Occur when using an invalid variable name that does not follow the naming conventions.

123variable = 10  # Invalid variable name starting with a digit


#? Compile-time errors prevent the program from being executed because the Python interpreter is unable to create a valid bytecode representation from the source code. When you attempt to run a Python script with compile-time errors, the interpreter will display an error message indicating the location and nature of the error.

#? It's important to fix compile-time errors before attempting to run the program, as the interpreter will not proceed to the execution phase until the code is syntactically correct. Once the compile-time errors are resolved, the program can be executed, and any runtime errors (exceptions) that may occur during execution can be addressed separately.






