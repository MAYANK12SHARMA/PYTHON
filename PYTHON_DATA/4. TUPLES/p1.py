# #?                            Topic : -  Creating the tuple

#! Creating empty tuples

tup1 = ()  # An empty tuple
print("Empty Tuple:", tup1)


#! Creating tuple with a single element (Note the comma)

x = (5)  # Without comma, it's not considered a tuple
print("\n",type(x), ":", x)


tup2 = (5,)  # With comma, it's a tuple with a single element
print("\n",type(tup2), ":", tup2)

#! Creating tuple without braces

tup3 = 1, 2, 3, 4, 5, 6  # Tuple without using parentheses
print("\n","Tuple without braces:", tup3)


#! Creating tuple with different datatypes

tup4 = ('mayank', 5, 5.8, " ", True)  # Tuple with elements of different datatypes
print("\n","Tuple with different datatypes:", tup4)


# Topic: Creating a Tuple using tuple()

# Given list
original_list = [1, 2, 4, 5, 8]

# Creating a tuple from the given list using tuple()
created_tuple = tuple(original_list)

# Printing the created tuple
print("\n","Created Tuple by list :", created_tuple)
