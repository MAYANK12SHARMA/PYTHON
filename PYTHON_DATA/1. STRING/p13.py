# #?    Function in string          
#!                                        topic :- string test methods:

# ? 1.isalpha(): Returns `True` if all characters in the string are alphabetic (letters), otherwise returns `False`.
str1 = "Hello"
res1 = str1.isalpha()
print(res1)

# ? 2. isdigit(): Returns `True` if all characters in the string are digits, otherwise returns `False`.
str2 = "12345"
res2 = str2.isdigit()
print(res2)

# ? 3. isalnum(): Returns `True` if all characters in the string are alphanumeric (either letters or numbers), otherwise returns `False`.
str3 = "Hello123"
res3 = str3.isalnum()
print(res3)

# ? 4. islower(): Returns `True` if all characters in the string are lowercase, otherwise returns `False`.
str4 = "hello"
res4 = str4.islower()
print(res4)

# ? 5. isupper(): Returns `True` if all characters in the string are uppercase, otherwise returns `False`.
str5 = "HELLO"
res5 = str5.isupper()
print(res5)

# ? 6. isspace(): Returns `True` if all characters in the string are whitespaces, otherwise returns `False`.
str6 = "    "
res6 = str6.isspace()
print(res6)

# ? 7. **`startswith(prefix)`**: Returns `True` if the string starts with the specified `prefix`, otherwise returns `False`.
str7 = "Hello, World!"
res7 = str7.startswith("Hello")
print(res7)

# ? 8. **`endswith(suffix)`**: Returns `True` if the string ends with the specified `suffix`, otherwise returns `False`.
str8 = "Hello, World!"
res8 = str8.endswith("World!")
print(res8)
