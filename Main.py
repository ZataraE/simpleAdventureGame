Inventory = {"Bandaid":0, "Bow":False, "Arrows":0, "Sword":False}

def firstScene():
    print("You find yourself in a dark dark forrest, You see a mountain off in the distance.\n Do You:\n 1: Walk down the dark path to go deeper into the forrest?\n 2: Walk towards the mountains")
    choice = input("> ")
    if choice == "1":
        print("You walk deeper into the woods and come across a big tree, looks like it has a door, maybe someone lives there?\n Do you:\n 1: Keep walking\n 2: Knock on the door")
        choice = input("> ")
        if choice == "1":
            print("You keep walking and fall into a hole and die")
    elif choice == "2":
        print("After some walking you reach the mountain when suddenly a thunderstorm breaks out. \n Do you:\n 1: Take shelter inside a nearby cave \n 2: Walk back into the forrest")
        choice = input("> ")
        if choice == "1":
            print("The cave was already home to a bear, the bear eats you")
        if choice == "2":
            print("You take shelter underneath some trees to hide from the rain and wait for the storm to pass. Off in the distance you notice a massive tree that sort of looks like a house. You walk up and knock on the door")

print("Adventure Game")
print("--------------")
print("To play, enter the number corresponding to your chosen path")
print("-----------------------------------------------------------")

firstScene()