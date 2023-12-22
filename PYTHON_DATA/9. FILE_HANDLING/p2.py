#                                       Topic :- FILE CLOSE

#?In Python, it's important to explicitly close files after you've finished working with them to free up system resources. The close() method is used to close a file. If you're using the with statement, the file is automatically closed when the block is exited.

#?  Using with Statement:


# Using with statement
with open('example.txt', 'r') as file:
    content = file.read()
    # Perform operations on the file as needed

# File is automatically closed when the block is exited

#!___________________________________________________________________________________________________________

#? Using close() Method:

# Opening the file
file = open('example.txt', 'r')

# Reading content from the file
content = file.read()

# Perform operations on the file as needed

# Closing the file explicitly
file.close()



#? **********************************************************************************************************
#! When using the with statement, the file is automatically closed when the block is exited, even if an exception occurs within the block. This is a preferred and more Pythonic way of handling file operations because it ensures that resources are released properly.

#! If you open a file without using with, it's your responsibility to explicitly call the close() method when you're done with the file to release system resources. Failure to close files properly can lead to resource leaks.

#! Always make sure to close files after reading or writing to them to ensure proper resource management.


#? **********************************************************************************************************   