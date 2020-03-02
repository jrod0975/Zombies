from os import system
from sys import exit

have_blue_key = False
have_red_key = False
have_gold = False



def game_intro():
    print("There are zombies chasing you into a building.")
    next = input("\nHit ENTER to continue...")
    system('clear')

    print("You decide to enter the building. It looks abandoned.")
    next = input("\nHit ENTER to continue...")
    system('clear')

    print("You barricade the door behind you and stop the undead from entering.")
    next = input("\nHit ENTER to continue...")
    system('clear')
def main_lobby(have_blue_key, have_red_key, have_gold):
    print("There are 3 doors: a green door, a red door, and a blue door.")
    print("Which door will you take?")
    door_taken = input("> ")

    system('clear')

    if door_taken.lower().strip() == "green":
        print("You decide to take the green door.")
        green_door()
    elif door_taken.lower().strip() == "blue":
        blue_door(have_red_key, have_blue_key)
    elif door_taken.lower().strip() == "red":
        if have_red_key == False:
            print("This door is locked...")
            next = input("\nHit ENTER to continue...")
            print("Take another door.")
            main_lobby(have_blue_key, have_red_key, have_gold)
        elif have_red_key == True:
            red_door(have_gold)
    else:
        print("Invalid choice. Zombies break in and eat you alive.")
        exit(0)
def green_door():
    system('clear')
    print("You take the green door and go into a narrow hallway.")
    print("It is almost pitch black, but because there is a broken window at the end of \n"
          "the hallway, some moonlight from outside goes in.")
    print("\nHit ENTER to continue...")



    print("There is nothing of interest in this room \n"
          "besides an eerie mannequin with dusty, old clothes.")


    print("Exit through the window?")
    go_outside = input("> ")

    if go_outside.strip().lower() == "yes":
        print("You decided to take a risk and go outside.")
        have_blue_key = False
        outside(have_blue_key)
    elif go_outside.lower().strip() == "no":
        print("You decided to stay.")
        print("You stare at the mannequin and notice something in its hand.")
        next = input()
        print("\nIts a note!")

        print("""It reads:
        Hello, we have delivered your paycheck to your office in the blue
        wing of the building. Please make sure you receive it safely.
        Sincerely,
        
            Your manager""")

        next = input()
        print("Attached behind the note is a blue keycard!")
        print("The zombies are breaking in.")
        print("You better go through the window.")
        next = input()
        system('clear')
        have_blue_key = True
        outside(have_blue_key)
    else:
        print("Invalid choice. Zombies break in and eat your intestines.")
        exit(0)
def outside(have_blue_key):
    print("You climb over the window and go into the side alley.")
    print("Its dark and there are puddles everywhere.")
    next = input()
    print("Well, at least there are no zombies around.")
    next = input()
    print("You make your way around the building and find the front door is empty.")
    print("You push the barricades to the side and enter.")
    next = input()
    main_lobby(have_blue_key, have_red_key, have_gold)
def blue_door(have_red_key, have_blue_key):
    if have_blue_key == False:
        print("It appears you need a blue keycard to access this door.")
        print("Choose another door.")
        next = input()
        main_lobby(have_blue_key, have_red_key, have_gold = False)

    elif have_blue_key == True:
        print("There are empty offices in this room.")
        print("Is there anyone alive left in this city at all?")
        next = input()

        print("You look around the room and see an envelope with money in it.")
        print("It's not worth much, especially during these desperate times.")

        next = input()
        print("Take the money?")
        take_money = input(">")

        if take_money.lower().strip() == "yes":

            print("You take the money...")
            next = input()
            print("...and you find a red keycard!")
            print("You better hurry back to the main lobby...")
            main_lobby(have_blue_key, have_red_key = True, have_gold = True)

        elif take_money.lower().strip() == "no":
            print("You put the envelope aside and find a red keycard!")
            print("You better hurry back to the main lobby...")
            main_lobby(have_blue_key, have_red_key = True, have_gold = False)
def red_door(have_gold):
    print("This is also a narrow hallway.")
    print("At the end of the hallway is a door.")
    next = input()
    print("There is a loud noise coming from outside.")
    next = input()
    print("It is a helicopter!")
    next = input()
    print("You rush towards the door and talk to the pilot.")
    next = input()
    print("The pilot says he will only take you if you give him money.")
    next = input()
    system('clear')

    if have_gold == False:
        print("You don't have money to give to him.")
        print("He flies away and abandons you.")
        next = input()
        print("Zombies catch up to you and eat you alive.")

    elif have_gold == True:
        print("You give him the money and he takes you with him.")
        next = input()
        print("CONGRATULATIONS!!!")
        print("YOU SURVIVED!!!")
game_intro()
main_lobby(have_blue_key, have_red_key, have_gold)