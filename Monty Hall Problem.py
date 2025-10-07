import random

def stick_or_switch(int_choice, doors_array):
    #Variables
    other_goat_door = 0

    #If the user chooses a door with a goat in it
    if doors_array[int(int_choice)] == "goat":
        #Finds the other door with the goat in it
        for i in range(len(doors_array)):
            if i != int_choice and doors_array[i] == "goat":
                other_goat_door = i + 1

        #Lets the user know which of the unchosen doors has a goat in it
        print(f"""\nI have decided to let you know that Door {other_goat_door} does not have a car.
Would you like to stick with Door {int_choice + 1} or switch to Door {doors_array.index('car') + 1}?""")

        #User input
        final_choice = int(input("\nInput choice: ")) - 1

        door_outcome(final_choice, doors_array)

    #If the user chooses the door with the car in it
    elif doors_array[int(int_choice)] == "car":
        #Randomly picks any of the two doors with the goat in it
        revealed_goat_door = random.randint(0, len(doors_array)-1)
        while doors_array[revealed_goat_door] == "car":
            revealed_goat_door = random.randint(0, len(doors_array)-1)

        #Finds the other door with a goat in it
        for i in range(len(doors_array)):
            if i != revealed_goat_door and doors_array[i] == "goat":
                other_goat_door = i

        #Lets the user know which of the unchosen doors has a goat in it
        print(f"""\nI have decided to let you know that Door {revealed_goat_door + 1} does not have a car.
Would you like to stick with Door {int_choice + 1} or switch to Door {other_goat_door + 1}?""")

        #User input
        final_choice = int(input("\nInput choice: ")) - 1

        door_outcome(final_choice, doors_array)


def door_outcome(int_choice, doors_array):
    if doors_array[int(int_choice)] == "goat":
        print('\nUnfortunately, you did not win a car.') #Print statement for choosing the door with a goat in it
    elif doors_array[int(int_choice)] == "car":
        print('\nCongratulations! You won a car.') #Print statement for choosing the door with a car in it


#An array of the three doors
doors = ["", "", ""]

#Assigns a goat to a random door
car = random.randint(0, len(doors)-1)
doors[car] = "car"

#Assigns another goat to a random door
goat1 = random.randint(0, len(doors)-1)
while goat1 == car:
    goat1 = random.randint(0, len(doors)-1)
doors[goat1] = "goat"

#Assigns the car to a random door
goat2 = random.randint(0, len(doors)-1)
while goat2 == car or goat2 == goat1:
    goat2 = random.randint(0, len(doors)-1)
doors[goat2] = "goat"

#print(doors)


#Menu
print("""There are three doors: Door 1, Door 2, and Door 3.  
Behind one of the doors is a brand new car of your choice. Behind the other two doors are goats.
Which door would you like to choose (1, 2, or 3)?""")

#User input
choice = int(input("\nInput choice: ")) - 1

#Call the function to stick with the original door or switch doors
stick_or_switch(choice, doors)

