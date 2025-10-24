'''
sums = 0
i = 0
while i < 10:
    sums +=i
    i+= 1
print(sums)
'''
'''
for i in range(100):
    print(f"{i}")
    i +=7
'''

'''
out = ""
for c in "ABCDEFG":
    if c == "C": 
        continue
    out += c
    if c == "E": 
        break
else:
    print("else")
print(out)
'''

'''
y = ""
x = input("enter a string: ")
for r in x:
    if r == " ":
        continue
    else:
        y += f"{r} "
print(y)
'''

'''
t = 1
x = input("Enter a number: ")
x_num = int(x)

for y in range(1,x_num,1):
    if y % 2 != 0:
        t *= y

print(f"the product of all odd numbers up to and including {x} is {t}")
'''

'''
t = 0
x = input("Enter a string (':q' to exit): ")
if x != ":q":
    for y in x:
        if y == "a" or y == "e" or y == "i" or y == "o" or y == "u":
            t += 1
        else:
            continue
    print(f"There are {t} vowel(s).")
elif x == ":q":
    print("exiting...")
'''

'''
import random
x = random.randint(1,100)
y = None
while y != x:
    y = input("Enter a number between 1 and 100: ")
    if int(y) < x:
        print("The computer chose a higher number.")
    elif int(y) > x:
        print("The computer chose a lower number")
    else:
        print("Congratulations, you won")
'''

'''
import math
n = 1
ex = (1 + 1/n)**n
while math.e - ex > 10**-6:
    n += 1
    ex = (1 + 1/n)**n
print(n)
'''

'''
import random
print("Arithmetic Exercise Generator")
print("Random arithmetic questions will be generated.")
print("Enter 'e' at any time to exit the program.")

while True:
    x = random.randint(1,100)
    y = random.randint(1,100)
    ops = random.choice(["+", "-", "*"])
    if ops == "+":
        ans = x + y
    elif ops == "-":
        ans = x - y
    elif ops == "*":
        ans = x*y
    while True:
        user_input = input(f"What is {x} {ops} {y}: ")
        if user_input.lower() == "e":
            print("exiting...")
            quit()
        elif int(user_input) == ans:
            print("Correct!")
            break
        elif int(user_input) != ans:
            print("Wrong. Try again!")
'''

