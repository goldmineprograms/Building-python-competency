import math

'''
x = (math.pi**3)-(5.6**2)+1
y = (1.2**(math.pi/2))-math.log(465**math.e)
z = (14.8/math.e)**(math.pi-1.8)

print(x/y + z)
'''

'''
x = input("Enter a number: ")
try:
    number = int(x)
    if number % 2 == 0:
        print(f"{number} is an even number.")
    elif number % 2 != 0:
        print(f"{number} is an odd number")

except ValueError:
    print("That is not a number")
'''

'''
hello = input("Enter pH of solution: ")

try:
    solpH = float(hello)
    if solpH>=0 and solpH<7.0:
        print("The solution is acidic") 
    elif solpH == 7.0:
        print("The solution is neutral")
    elif solpH>7.0  and solpH<=14.0:
        print("The solution is basic")
    else:
        print("Invalid pH. pH should be between 0 and 14.")
except ValueError:
    print("Please input a valid number.")
'''

'''
x = 12345
x_years = math.floor(x/(365*24))
x_remain1 = x-x_years*365*24
x_days = math.floor(x_remain1/24)
x_hours = x_remain1-x_days*24

print (f"{x} hours is equal to {x_years} years, {x_days} days and {x_hours} hours.")
'''

'''
travelling = input("Enter distance in kilometers: ")
try: 
    distance = float(travelling)
    if distance >= 0 and distance <= 20:
        print("Walkable, its FREE!")
        print(f"Cost of travel by motorcycle: {distance*0.22}")
        print(f"Cost of travel by car: {distance*0.26}")
    elif distance > 20 and distance <100:
        print("Too far to walk!")
        print(f"Cost of travel by motorcycle: {distance*0.22}")
        print(f"Cost of travel by car: {distance*0.26}")
    elif distance >= 100 and distance <= 200:
        print("Too far to walk!")
        print(f"Cost of travel by motorcycle: {distance*0.22}")
        print(f"Cost of travel by car: {distance*0.26}")
        print(f"Cost of travel by plane: {distance*0.76}")
    elif distance>200 and distance <=800:
        print("Too far to walk!")
        print("Too far to travel by motorcycle!")
        print(f"Cost of travel by car: {distance*0.26}")
        print(f"Cost of travel by plane: {distance*0.76}")
    elif distance>800:
        print("Too far to walk!")
        print("Too far to travel by motorcycle!")
        print("Too far to travel by car!")
        print(f"Cost of travel by plane: {distance*0.76}")
except ValueError:
    print("Please input a number")
'''

'''
x = (math.e**1.4 + 2*math.log(465)) / (math.sqrt(2) + 14)
y = 12 / math.sqrt(math.e + 4)
print(x + y)

x1 = 2.6**0.2 + 17**(-1/7)
y1 = math.e**(-math.sqrt(43.3))/math.tan(176)
print(x1 + y1)
'''

'''
item_price = 100
if item_price > 0 and item_price <= 10:
    discount = item_price * 0.1
elif item_price > 10 and item_price < 20:
    discount = item_price * 0.15
elif item_price >= 20 and item_price < 50:
    discount = item_price * 0.2
else:
    discount = item_price * 0.25
print(f"The final price of the item is ${item_price-discount}")
'''

'''
def Cylinder():
    x = input("Radius of Cylinder:")
    y = input("Height of Cylinder: ")
    z = 2*math.pi*(float(x)**2) + 2*math.pi*float(x)*float(y)
    print(f"The area of the cylinder is {z}")

def Circle():
    r = input("Radius of circle: ")
    q = math.pi*(float(r)**2)
    print(f"The area of the circle is {q}")

def Rectangle():
    g = input("Length of rectangle: ")
    w = input("Breadth of rectangle: ")
    t = float(g)*float(w)
    print(f"The area of the rectangle is {t}")

print("Area Calculator")
print("----------------")
print("Shapes available:")
print("1. Cylinder")
print("2. Circle")
print("3. Rectangle")
user_input = input("Choose one of the number above: ")
if int(user_input) == 1:
    Cylinder()
elif int(user_input) == 2:
    Circle()
elif int(user_input) == 3:
    Rectangle()
'''

'''
x = input("Enter amount in SGD: ")
y = input("Conver into Euros (E), U.S. Dollar (U) or Japanese Yen (J)?: ")
if y == "E":
    converted = float(x) * 0.712
    print(f"{float(x)} SGD = {round(converted, 2)} EUR")
elif y == "U":
    converted = float(x) * 0.743
    print(f"{float(x)} SGD = {round(converted, 2)} USD")
elif y == "J":
    converted = float(x) * 111.3
    print(f"{float(x)} SGD = {round(converted, 2)} JPY")
'''

'''
print("Quadratic solver: ax^2 + bx + c = 0")
print("Enter values for a, b and c:")
a = input("a: ")
b = input("b: ")
c = input("c: ")
a = float(a)
b = float(b)
c = float(c)
x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
if x1 == x2:
    print(f"The roots of the equation is x = {x1}")
elif x1 != x2:
    print(f"The roots of the equation is x = {x1} and x = {x2}")
'''

x = input("length of base: ")
x1 = input("inches(i) or centimeters (c)?: ")
if x1 == "i":
    y = input("width of base: ")
    y1 = input("inches(i) or centimeters (c)?: ")
    if y1 == "i":
        y2 = float(y)
    elif y1 == "c":
        y2 = float(y) / 2.54
    z = input("height of pyramid: ")
    z1 = input("inches(i) or centimeters (c)?: ")
    if z1 == "i":
        z2 = float(z)
    elif y1 == "c":
        z2 = float(z) / 2.54
    volume = (float(x)*y2*z2)/3
    print(f"The volume of the pyramid is {volume} cubic inches")
elif x1 == "c":
    y = input("width of base: ")
    y1 = input("inches(i) or centimeters (c)?: ")
    if y1 == "i":
        y2 = float(y) 
    elif y1 == "c":
        y2 = float(y) / 2.54
    z = input("height of pyramid: ")
    z1 = input("inches(i) or centimeters (c)?: ")
    if z1 == "i":
        z2 = float(z)
    elif y1 == "c":
        z2 = float(z) / 2.54
    volume = ((float(x)/2.54)*y2*z2)/3
    print(f"The volume of the pyramid is {volume} cubic inches")