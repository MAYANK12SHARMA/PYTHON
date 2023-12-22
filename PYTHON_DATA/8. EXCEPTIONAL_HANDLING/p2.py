def square_root(num):
    return num ** 0.5

def power(num, pow):
    return num ** pow

def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

# Take user input for the starting and ending range
start_range = int(input("Enter the starting range: "))
end_range = int(input("Enter the ending range: "))

print(f"Operations on palindrome numbers within the range {start_range} to {end_range}:")

# Iterate through the range and perform operations on palindrome numbers
for num in range(start_range, end_range + 1):
    if is_palindrome(num):
        if num % 2 == 0:
            result = square_root(num)
            print(f"{num} - Square Root: {result:.6f}")
        else:
            result = power(num, 2)
            print(f"{num} - Power of 2: {result}")
