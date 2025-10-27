'''
my_list = ["mystring", True, 54, [2.0,3.0,4.0]]
for x in my_list:
    print(f"{x} and {type(x)}")
'''

'''
my_numbers = [ ]
my_numbers.extend([1,-1,2,-3,5,-8])
my_numbers.append(0)
my_numbers.sort()
my_numbers.pop()
my_numbers.reverse()
print(my_numbers)
'''

'''
Total = 0
Book = {"Alice": 123, "Bob": 456, "Eve":789}
for key,value in Book.items():
    Total += value
print(Total)
'''

'''
x_input = input("Enter a string: ")
y_input = input("Enter a letter: ")
for gh in x_input:
    if gh == y_input:
        fl = x_input.index(gh)
print(x_input[:fl+1])
print(x_input[fl+1:])
'''

'''
squares = [ ]
for x in range(1,11):
    squares.append(x**2)
print(squares)
'''

'''
me = {"Name": "Nic", "Age": 23,}
me["Enjoyment"] = 10
print(me)
'''

'''
names = ["Alice", "Bob", "Carlos", "Dave", "Eve"]
lololol = []
for x in names:
    if x[-1] == "e":
        lololol.append(x)
print(lololol)
'''

'''
import itertools
dice_pairs = list(itertools.combinations_with_replacement(range(1,7),2))
print(dice_pairs)
'''

'''
dice_pairs = []
for i in range(1,7):
    for j in range(i,7):
        dice_pairs.append((i,j))
print(dice_pairs)
'''

'''
import itertools
dice_pairs = list(itertools.product(range(1,7),repeat = 2))
print(dice_pairs)
'''

'''
l1 = ['q', 1, 'w', 2]
l2 = [x*2 for x in l1]
print(l2)
'''

'''
listy = ["qwer", "asdf", "zxcv"]
for i in range(len(listy)):
    print(f"{i}, {listy[i][i]}")
'''

'''
user_input = input("Enter a string: ")
china = [char for char in user_input]
removal = input("Enter letters to remove: ")
usa = [char for char in removal]
for x in china:
    for y in usa:
        if x.lower() == y.lower():
            china.remove(x)
            lick = ""
            for d in china:
                lick += d
print(lick)
'''

'''
x = input("Enter a string:")
y = ""
count = 0
for char in x:
    if char.isalpha():
        y += char.upper() if count % 2 else char.lower()
        count += 1
    else:
        y += char
print(y)

x = input("Enter a string: ")
y = ""
'''

'''
x = input("Enter a string:")
y = ""
for index, char in enumerate(x):
    y += char.upper() if index % 2 != 0 else char.lower()

print(y)
'''

'''
import re
from collections import Counter
wayang = "The sun is shining brightly in the clear blue sky. The sun is warm on my skin, and the sun is making everything feel alive. The birds are singing their sweet songs, and the birds are flying high in the sky. The trees are swaying gently in the breeze, and the trees are providing shade from the sun. The world is a beautiful place, and the world is full of wonder. The sun is setting slowly, casting a warm glow over the landscape. The sun is shining down on us, and the sun is making everything feel happy. The birds are singing their sweet melodies, and the birds are chirping loudly. The trees are swaying gently, and the trees are rustling softly."
lol = wayang.lower()
clean_lol = re.sub(r'[^\w\s]','',lol)
clean = clean_lol.split()
keng = Counter(clean)
print(keng)
'''
