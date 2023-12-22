# with open('a_text_file.txt','w') as file:
#     file.write('mayank sharma is a student')
    
# file.close()

# file = open('a_text_file.txt','w')
# file.write('mayank sharma is a good student')


# file = open('a_text_file.txt','r')
# content = file.read(6)

# print(content)


# with open('a_text_file.txt','w+') as f:
#     str = f"mayank sharma is a good student\njay shree ram \n radhe radhe  "
#     f.write(str)
#     f.seek(0)
#     print(f.read(20))
    
    
    
# with open('a_text_file.txt', 'x') as new_file:
#     new_file.write('This is a new file.')

try:
    with open('a_text_file.txt', 'x') as new_file:
        new_file.write('This is a new file.')
except FileExistsError:
    print('File already exists.')

     