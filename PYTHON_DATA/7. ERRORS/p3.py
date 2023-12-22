#                                           Topic :-  Exception

#? Exception handling in Python involves using try, except, else, and finally blocks to manage and respond to exceptions (runtime errors) that may occur during the execution of a program. The basic structure of exception handling in Python is as follows:



#! SYNTAX :- 

#! try: 
#!     ........code.....................
#! except Exception 1
#!     ........code.....................
#! except Exception n
#!     ........code.....................
#! else:
#!      .....code without error.........
#! finally:
#!      ........code....................



try:
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))
    result = num1 / num2
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"Result: {result}")
finally:
    print("Cleanup and finalization code.")




# try:
#     num1 = int(input("enter the 1st number : "))
#     num2 = int(input("enter the 2nd number : "))
#     num3 = num1/num2
# except ZeroDivisionError:
#     print("indefinate form")
# except ValueError:
#     print("an value error occured")
# else:
#     print(num3)
# finally:
#     print("your file closed finally")