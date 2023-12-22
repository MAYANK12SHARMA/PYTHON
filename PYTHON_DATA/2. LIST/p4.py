# #?                            Topic : -  cloning of list

#?  Cloning involves creating a new list that is a copy of the original list. Changes made to one list will not affect the other.

original_list = [1, 2, 3]
cloned_list = original_list.copy()                 #  or cloned_list = original_list[:]

# Cloning - a new list is created with the same elements
print(original_list)  
print(cloned_list)    

# Modify the original list
original_list.append(4)

# Only the original list is modified, not the cloned list
print(original_list)  
print(cloned_list)