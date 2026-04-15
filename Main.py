while True:
    print("Adventure Game")
    print("--------------")
    print("To play, enter the number corresponding to your chosen path")
    print("-----------------------------------------------------------")
    print("You find yourself in a dark dark forrest, You see a mountain off in the distance.\n Do You:\n 1: Walk down the dark path to go deeper into the forrest?\n 2: Walk towards the mountains")
    choice = input("> ")
    if choice == "1":
        print("You walk deeper into the woods and come across a big tree, looks like it has a door, maybe someone lives there?\n Do you:\n 1: Keep walking\n 2: Knock on the door")
        choice = input("> ")
        if choice == "1":
            print("You keep walking and fall into a hole and die")
            win = False
            break
        elif choice == "2":
            print("The door opens and little creature greets you")
            win = True
            break
    elif choice == "2":
        print("After days of hiking you reach the mountain when suddenly a thunderstorm breaks out. \n Do you:\n 1: Take shelter inside a nearby cave \n 2: Walk back into the forrest")
        choice = input("> ")
        if choice == "1":
            print("The cave was already home to a bear, the bear eats you")
            win = False
            break
        if choice == "2":
            print("You take shelter underneath some trees to hide from the rain and wait for the storm to pass")
            win = True
            break
if win == False:
   print("GAME OVER")
elif win == True:
    print("You win!")
