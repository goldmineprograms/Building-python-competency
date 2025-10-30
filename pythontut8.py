'''
def my_add(n):
    summer = 0
    for num in range(0,n+1):
        summer += num
    print(summer)

my_add(12)
'''

'''
def my_factorial(n):
    multiple = 1
    if n == 0:
        print(multiple)
    elif n > 0:
        for num in range(1,n+1):
            multiple *= num
        print(multiple)

my_factorial(1)
'''

'''
import math

print(math.gcd(120,500))
'''

'''
def gcd(x,y):
    while y != 0:
        x,y = y, x%y
    print(x)
gcd(34,60)
'''

'''
def fibonacci_index(x):
    if x <= 1:
        return x
    else:
        return fibonacci_index(x-1) + fibonacci_index(x-2)
    
for i in range(10):
    print(fibonacci_index(i))
'''

'''
n = 100
x, y = 0, 1
fib_list = [0,1]
for i in range(2, n):
    new = x + y
    fib_list.append(new)
    x,y = y, new
print(fib_list)
'''

'''
def palindrome(x):
    x = x.lower()
    for i in range(len(x)//2):
        if x[i] != x[-(i+1)]:
            return(False)
    print(True)
palindrome("hElleh")
'''