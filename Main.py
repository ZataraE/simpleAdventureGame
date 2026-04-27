# Dictionary that stores the players inventory
Inventory = {"Bandaid":0, "Bow":False, "Arrows":0, "Sword":False}

# The first scene of the game
def firstScene():
    print("You find yourself in a dark dark forrest, You see a mountain off in the distance.\n Do You:\n 1: Walk down the dark path to go deeper into the forrest?\n 2: Walk towards the mountains")
    choice = input("> ")
    if choice == "1":
        print("You walk deeper into the woods and come across a big tree, looks like it has a door, maybe someone lives there?\n Do you:\n 1: Keep walking\n 2: Knock on the door")
        choice = input("> ")
        if choice == "1":
            print("You keep walking and fall into a hole and die")
        elif choice == "2":
            inTheTreehouse()
    elif choice == "2":
        print("""\
          /\\
         /**\\
        /****\   /\\
       /      \ /**\\
      /  /\    /    \        /\    /\  /\      /\            /\/\/\  /\\
     /  /  \  /      \      /  \/\/  \/  \  /\/  \/\  /\  /\/ / /  \/  \\
    /  /    \/ /\     \    /    \ \  /    \/ /   /  \/  \/  \  /    \   \\
   /  /      \/  \/\   \  /      \    /   /    \\
__/__/_______/___/__\___\__________________________________________________

              """)
        print("After some walking you reach the mountain when suddenly a thunderstorm breaks out. \n Do you:\n 1: Take shelter inside a nearby cave \n 2: Walk back into the forrest")
        choice = input("> ")
        if choice == "1":
            print("The cave was already home to a bear, the bear eats you")
        if choice == "2":
            print("You take shelter underneath some trees to hide from the rain and wait for the storm to pass. Off in the distance you notice a massive tree that sort of looks like a house. You walk up and knock on the door")
            inTheTreehouse()
# The second scene of the game
def inTheTreehouse():
    print("""\
                          
     .{{}}}}}}.
    {{{{{{(`)}}}.
   {{{(`)}}}}}}}}}
  }}}}}}}}}{{(`){{{
  }}}}{{{{(`)}}{{{{
 {{{(`)}}}}}}}{}}}}}
{{{{{{{{(`)}}}}}}}}}}
{{{{{{{}{{{{(`)}}}}}}
 {{{{{(`)   {{{{(`)}'
  `""'" |   | "'"'`
  (`)  /     \\
 ~~~~~~~~~~~~~~~~~~~       
                """)
    print("The door opens and little creature greets you")
    print("You ask if it would be okay for you to stay the night and the little creature nods in agreement")
    print("You quickly fall asleep")
    print("The next morning the forrest now looks alot friendlier in the soft glow of the sunrise")
    print("""\
           |
     \     |     /
       \       /
         ,d8b,           .,
 (')-")_ 88888 ---   ;';'  ';'.
('-  (. ')98P'      ';.,;    ,;
 '-.(PjP)'     \       '.';.'
           |     \\
           |

          """)
    print("Will you:")
    print("1: Thank the creature for the night and venture out into the woods again")
    print("2: Ask if it would be okay for you to stay another day")
    choice = input("> ")
    if choice == "1":
        print("You head out and the sun shines brightly")
    elif choice == "2":
        print("The creature says you can stay aslong as you help him with some chores")
        print("After a day of chopping wood and gathering berries and mushrooms, your very tired")
        print("The creature thanks you for your hard work and gives you a gift to aid you in your journey")
        print("Inside the package you find a bow and two arrows")
        print("+ 1 Bow")
        # Update the Inventory Dict so that the player has a bow
        Inventory.update({"Bow":True})
        print("+ 2 Arrows")
        # Update the inventory by fetching the amount of arrows the player already has and adding the additional arrows
        Inventory.update({"Arrows":Inventory["Arrows"] + 2})

# Intro to the game                      
print("Adventure Game")
print("--------------")
print("To play, enter the number corresponding to your chosen path")
print("-----------------------------------------------------------")

firstScene()
