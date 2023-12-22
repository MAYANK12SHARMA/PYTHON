def square_root(num):
    num = num**(1/2)
    print(num)

def power(num,pow):
    num = num**pow
    print(num)

def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]
    
       
start = int(input("Enter the starting range : "))
end = int(input("Enter the ending range : "))

for i in range(start,end,1):
    if is_palindrome(i):
        if i%2 ==0:
            print(f"{i} - Power of 2 : {power(i,2)}")
        else:
            print(f"{i} - Square root : {square_root(i)}")
            
    
 