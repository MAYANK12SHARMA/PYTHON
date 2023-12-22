#                           Topic :- FILE OPENING

#? The open() function is used to open a file in Python. It takes two arguments primarily: the file path and the mode. 

#!  SYNTAX :-     1.   with open('file_path', 'mode') as file_variable:

#!  SYNTAX :-     2.   file_variable = open('file_path', 'mode',buffering) 

# Here's a breakdown of the syntax:

#? 1. 'file_path': This is the path to the file you want to open. It can be either a relative or an absolute path

#? 2. 'mode': This is a string that specifies the mode in which the file should be opened. It is a combination of characters indicating the purpose of opening the file (e.g., read, write, append, etc.).

#? a:  'w' - Write Mode:

#! Opens the file for writing. If the file already exists, it truncates the file to zero length. If the file  does not exist, it creates a new file.
#! Use with caution, as it overwrites the entire file content.

with open('example.txt', 'w') as file:
    file.write('Hello, World!')

#____________________________________________________________________________________________________________

#? b:  'r' - Read Mode:

#! Opens the file for reading. The file pointer is placed at the beginning of the file.
#! Raises FileNotFoundError if the file does not exist.

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)        # display the data
    
#____________________________________________________________________________________________________________
    
#? c:  'a' - Append Mode:

#! Opens the file for writing. If the file already exists, it appends new data to the end of the file. If the file does not exist, it creates a new file.
#! The file pointer is at the end of the file.

with open('example.txt', 'a') as file:
    file.write('\nAppended text.')

#____________________________________________________________________________________________________________
    
#? d: 'w+' - Write and Read Mode:

#! Opens the file for both reading and writing.
#!  If the file exists, it truncates the file to zero length (erases existing content).
#!  If the file does not exist, it creates a new file.


with open('example.txt', 'w+') as file:
    file.write('Hello, World!')  # Writes data to the file
    file.seek(0)  # Moves the file pointer to the beginning
    content = file.read()  # Reads the data

#____________________________________________________________________________________________________________



#? e:  'r+' - Read and Write Mode:

#! Opens the file for both reading and writing.
#! The file pointer is at the beginning of the file.
#! If the file does not exist, it raises a FileNotFoundError.

with open('example.txt', 'r+') as file:
    content = file.read()  # Reads existing content
    file.write('New data')  # Overwrites existing content or adds new data

#____________________________________________________________________________________________________________

#? f: 'a+' - Append and Read Mode:

#! Opens the file for both reading and writing.
#! If the file exists, the file pointer is at the end of the file.
#! If the file does not exist, it is created.
#! New data written to the file is added at the end.

with open('example.txt', 'a+') as file:
    content = file.read()  # Reads existing content
    file.write('New data')  # Appends new data at the end


#____________________________________________________________________________________________________________


#? 'x' - Exclusive Creation:

#! Creates a new file. If the file already exists, the operation fails and raises a FileExistsError.

with open('new_file.txt', 'x') as new_file:
    new_file.write('This is a new file.')

try:
    with open('new_file.txt', 'x') as new_file:
        new_file.write('This is a new file.')
except FileExistsError:
    print('File already exists.')
