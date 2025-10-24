import random

def guessing_game():
    x = random.randint(1,100)
    y = input("Choose a number between 1-100: ")
    if int(y) == x:
        print(x)
        print("You did it, you chose the same number as the computer!")
    elif int(y)<1 or int(y)>100:
        print("Please choose a range between 1 and 100 for the game to work")                  
    else:
        print(x)
        print("You did not get the same number as the computer")
                
def play_again():
    que = input("Would you like to play again (Y/N): ")
    while que == "Y":
        guessing_game()
    else:
        print("Its okay, see you next time!")


user_choice = input("Would you like to play a game (Y/N): ")

if user_choice == "Y":
    guessing_game()
    play_again()
    
elif user_choice == "N":
    print("Its okay, see you again!")