
def calculator():
    def add(x,y):
       return x+y

    def subtract(x,y):
       return x-y

    def multiply(x,y):
       return x*y

    def divide(x,y):
       return x/y

    print("Choose 1 for addition")
    print("Choose 2 for subtraction")
    print("Choose 3 for multiplication")
    print("Choose 4 for division")

    userinput = input("Which would you like to do?: ")

    if userinput == "1":
       first = float(input("Whats your first value: "))
       second =  float(input("Whats your second value: "))
       print(add(first,second))
       choice = input("Would you like to try again, Y/N: ")
       if choice == "Y":
          calculator()
       elif choice == "N":
          print("Thank you for trying")
        
    elif userinput == "2":
       first = float(input("Whats your first value: "))
       second =  float(input("Whats your second value: "))
       print(subtract(first,second))
       choice = input("Would you like to try again, Y/N: ")
       if choice == "Y":
          calculator()
       elif choice == "N":
          print("Thank you for trying")
       
    elif userinput == "3":
       first = float(input("Whats your first value: "))
       second =  float(input("Whats your second value: "))
       print(multiply(first,second))
       choice = input("Would you like to try again, Y/N: ")
       if choice == "Y":
          calculator()
       elif choice == "N":
          print("Thank you for trying")

    elif userinput == "4":
       first = float(input("Whats your first value: "))
       second =  float(input("Whats your second value: "))
       print(divide(first,second))
       choice = input("Would you like to try again, Y/N: ")
       if choice == "Y":
          calculator()
       elif choice == "N":
          print("Thank you for trying")

    else:
       print("That is not within the choice range")

calculator()