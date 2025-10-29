'''
import math

def f(x,y,z):
    total = x*y + math.sin(y*z) + math.pi*x*z
    print(total)

f(1,2,3)
f(4,5,6)
f(7,8,9)
'''

'''
def is_odd(x):
    if x % 2 != 0:
        print(True)
    else:
        print(False)

y = input("Please choose an interger: ")
is_odd(int(y))
'''

'''
def cap_and_rev(x):
    x = x.upper()
    print(x[::-1])

y = input("Please enter a string: ")
cap_and_rev(y)
'''

'''
def sum_to(x):
    er = 0
    for y in range(1,x+1):
        er += y
    print(er)

sum_to(20)
'''

'''
def is_equal_length(x,y):
    if len(x) == len(y):
        print(True)
    else:
        print(False)

t = "Hello"
w = "Strig"
is_equal_length(t,w)
'''

'''
def remove_number(x):
    y = list(x)
    for t in y:
        if t.isdigit():
            y.remove(t)
    print("".join(y))

z = "we1are2one4big5house"
remove_number(z)
'''

'''
def find_max(x):
    print(max(x))

y = [1,4,54,23,100,43,55,67]
find_max(y)

def find_min(x):
    print(min(x))

y = [-100,12,34,-120,43]
find_min(y)
'''

'''
def combine_strings(x,y):
    x_list = list(x)
    y_list = list(y)
    tu = ""
    for q in x_list:
        for z in y_list:
           if x_list.index(q) == y_list.index(z):
                tu += q
                tu += z
    print(tu)

combine_strings("abc123", "edf456")
'''

'''
def caesar_cipher(text,shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char)-base+shift)%26+base)
        else:
            result += char
    return result

encrypted = caesar_cipher("Hell", 3)
decrypted = caesar_cipher(encrypted,-3)

print(encrypted)
print(decrypted)
'''

'''
def occurrences(x,y):
    x_list = list(x)
    t = []
    count = 0
    for i, char in enumerate(x_list):
       if char == y:
           t.append(i)
           count +=1
    total = (count,t)
    print(total)

occurrences("Hellolololo", "l")
'''

'''
def occurrences(x,y):
    t = [i for i, char in enumerate(x) if char == y]
    count = len(t)
    total = (count,t)
    print(total)
occurrences("Hellolololo", "l")
'''