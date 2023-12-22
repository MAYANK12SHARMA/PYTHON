#                                               Topic :- palindrome question 

def is_palindrome(s):
    # Base case: an empty string or a string with one character is a palindrome
    if len(s) <= 1:
        return True
    
    # Compare the first and last characters
    if s[0] == s[-1]:
        # Recursively check the substring without the first and last characters
        return is_palindrome(s[1:-1])
    else:
        return False

# Test the function
print(is_palindrome("radar"))    # True
print(is_palindrome("level"))    # True
print(is_palindrome("python"))   # False
print(is_palindrome(""))          # True (empty string is a palindrome)
