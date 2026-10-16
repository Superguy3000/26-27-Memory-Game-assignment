from random import randint
from time import sleep
from os import system
import msvcrt
def generate(lvl,string,arr):
    """generates an uppercase letter string which scales with level, then returns it"""
    for i in range(0,lvl+3):
        rand = randint(0,25)
        string += arr[rand]
    return string
def ask(lvl,string):
    """displays the string for 5 seconds and then clears the console,
      then it asks the user to input the same string"""
    print(f"""Level {lvl}
Remember code: {string}""")
    for i in range(0,5):
        print((5-i))
        sleep(1)
    system("cls")
    clear_keyboard_buffer()
    a = input("Enter code: ")
    return a
def wrong():
    """runs if the string was not entered correctly,
    prints the the user is wrong, the level they made it through, and a text describing how they did,
      after that returns the values to refresh the needed variables"""
    print("WRONG!!!")
    print()
    print(f"You made it through {level-1} levels")
    print()
    if level <3:
        print("HAHA Noob!")
    elif(level <7):
        print("Ehh, you're kinda good")
    else:
        print("wow, you're a mustard")
    return 1,""

def clear_keyboard_buffer(): 
    """Remove any pending keystrokes from the keyboard buffer.""" 

    while msvcrt.kbhit(): 

        msvcrt.getwch()


level = 1
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
string = ""
guess = ""


while True:
    string = generate(level,string,letters)
    guess = ask(level,string)
    if guess.upper() == string:
        level +=1
        string = ""
        print("Good Job!")
        sleep(3)
        while True:
            a = input("Do you want to continue?")
            if a.upper() == "Y" or a.upper() == "N":
                break
            else:
                print("Invalid")
    else:
        level,string = wrong()
        while True:
            a = input("Do you want to play again?")
            if a.upper() == "Y" or a.upper() == "N":
                break
            else:
                print("Invalid")
    if a.upper() == "N":
        break
    else:
        system("cls")
print("GOOODBYE!!!")
