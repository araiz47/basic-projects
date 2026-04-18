#Number guessing project Ver 1

import random #Used random library for the guessing numbers part 


while True:
    print("Welcome to the basic number guessing game")
    print("1. Play")
    print("2. Exit")
    choice = input("Enter a choice: ")

    if choice == '1':
        
        user_number = int(input("Enter a number: "))

        bot = random.randint(0,10)

        if user_number == bot:
            print("Yay u guessed it right")
        else :
            print(f"You're wrong !! The correct number was {bot}")

    elif choice == '2':
        break

    else:
        print("Wrong Choice")



