#                                     Topic :- Recursive Function 

#? A recursive function is a function that calls itself either directly or indirectly in order to solve a problem. Recursive functions are often used when a problem can be broken down into smaller subproblems that are similar to the original problem. Each recursive call processes a smaller instance of the problem until a base case is reached, at which point the function returns a result without making further recursive calls.


def factorial(n):
    if n ==1 or n ==0:
        return 1
    else:
        return n*factorial(n-1)

n = factorial(5)

print(n)