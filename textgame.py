print("Welcome to a text based adventure game") #just making a basic text based adventure game gonna add more features later 
print("You have woken up in a destroyed city ....")

choice = input("Choose a path (Left/Right): ").lower()

if choice =="left": #left route
    print("You have reached a small camp")
    village = input("Be polite or hostile: ").lower()
    if village == "pol":
        print("You talked politely to the campers and they decided to let you live there")
        print("You win !!")
    elif village == "hos":
        print("You were hostile to the campers and they killed you !!")
        print("Game over")
    

elif choice == "right": #right route
    print("You have reached a river")
    river_choice = input("Enter a choice (Swim or boat): ").lower()
    if river_choice == "swim":
        print("Oh no you drowned !!")
        print("Game over !!")
    elif river_choice == "boat":
        print("You reached back side of camp !!")
        river_choice2 = input("Enter a choice: ")
        if river_choice2 == "pol":
         print("You talked politely to the campers and they decided to let you live there")
         print("You win !!")
        elif river_choice2 == "hos":
            print("You were hostile to the campers and they killed you !!")
            print("Game over")


