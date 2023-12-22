# #?                            Topic : -  Aliasing of list

#?  Aliasing occurs when two or more variables refer to the same object. In the context of lists, if you assign one list to another, both variables refer to the same list object. Changes made to the list through one variable will affect all variables that reference the same list object.

original_list = [1, 2, 3]
alias_list = original_list

# Aliasing - both variables reference the same list object
print(original_list)  
print(alias_list)     

# Modify the list using one variable
original_list.append(4)

# Both variables reflect the change
print(original_list)  
print(alias_list)     
