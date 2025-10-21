'''
my_float =  3.00
my_str = "Name"
my_int = 5

print(type(my_int))
'''

'''
my_quote = '"Programs are meant to be read by humans and only incidentally for \n' \
'computers to execute." - Donald E. Knuth'
print(my_quote)
'''
'''
x = input("Enter a value for x: ")
x = int(x)
print(f"x*x is {x*x}")
print(f"3*x is {3*x}")
print(f"(x+2)^2 is {(x+2)^2}")
'''

'''
user_age = input("Enter your age: ")
user_age = int(user_age)

print(f"Five years ago, your age was {user_age-5}")
print(f"In three years, your age will be user_age {user_age+3}")
'''

'''
temp = 35.0
wind_speed = 11.0
wcf = 35.7 + 0.6*temp - 35.7*wind_speed**0.16 + 0.43*temp*wind_speed**0.16
print(f"The temperature is {temp} and the wind speed is {wind_speed}")
print(f"The wind chill factor is {wcf}")
'''

length_input = input("Enter length of rectangle: ")
width_input = input("Enter width of rectangle: ")

try:
    length = float(length_input)
    width = float(width_input)
    perimeter = 2*length + 2*width
    area = length*width
    print(f"The perimeter is {perimeter} and the area is {area}.")

except ValueError:
    print("Not an integer or float")
