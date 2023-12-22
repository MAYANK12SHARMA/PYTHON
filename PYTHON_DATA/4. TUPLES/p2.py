# #?                            Topic : -  Accessing the tuple elements 

#? Define a tuple named 'tup1' with integer elements
tup1 = (10, 20, 30, 40, 50, 60, 70, 80)

#? Print the first element of the tuple
print("First element:", tup1[0])

#? Print the sixth element of the tuple
print("Sixth element:", tup1[5])

#? Print the last element of the tuple using negative index
print("Last element:", tup1[-1])

#? Print the entire tuple using slicing
print("All elements:", tup1[:])

#? Print elements from index 1 to 3 using slicing
print("Elements from index 1 to 3:", tup1[1:4])

#? Print every second element using step size 2
print("Every second element:", tup1[::2])

#? Print every second element in reverse order using negative step size
print("Every second element in reverse:", tup1[::-2])

#? Print elements from index -4 to -2 using negative slicing
print("Elements from index -4 to -2:", tup1[-4:-1])

#? Unpack the first two elements of the tuple into variables 'num1' and 'num2'
num1, num2 = tup1[0:2]

#? Print the unpacked variables
print("num1:", num1, "\nnum2:", num2)

