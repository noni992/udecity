import time
import random


enemies = ['Beast', 'Warewolf', 'Dragon', 'Ork', 'Vampire', 'Devil']
weapons = ['Shotgun', 'Magic Wond', 'sword']
enemy = random.choice(enemies)
weapon = random.choice(weapons)


def print_pause(message, puase=2):
    print(message)
    time.sleep(puase)


def game():
    intro()
    choices()


def intro():

    print_pause("Welcome to Adventure Game.", 2)
    print_pause("Lets begin!", 2)
    print_pause("One day you traveled to a village in your summer holiday.", 4)
    print_pause("You arrive to the house that you will stay in.", 3)
    print_pause("You entered the house with your lougage.",2)
    print_pause("You notice that the house was beautiful from outside "
                "but have eerie vipe inside.", 3)
    print_pause("The house was divided to 3 floors.", 2)
    print_pause("1st floor has: Kitchen,living room,and basement door.", 3)
    print_pause("2nd floor has: bedroom, office room,bath room.", 3)
    print_pause("3rd floor was the basement.", 2)
    print_pause("You went to the 2nd floor to sleep.", 2)
    print_pause("At mid night, you was waken by "
                "a weird noise coming from 1st floor.", 3)
    print_pause("You went down and walk slowly "
                "to check where the noise come from.", 3)
    print_pause(f"you saw {enemy} entering the basement!.", 2)
    print_pause("The shiver came all the way throw your spine.", 2)


def choices():
    print_pause("Here you tought of 2 choices:\n"
                f"1- Fight the {enemy}.\n"
                "2- Run away.")

    select = input("choose carefuly:1 or 2\n")
    if select == '1':
        print_pause("Ooh, i see. You're brave budy.")
        fight_mood()
    elif select == '2':
        run_mood()
        play_again()
    else:
        print_pause("Sorry i don't understand, try again.")
        choices()


def fight_mood():

    search = input("lets see. Do you want to:\n"
                   "1-fight directly.\n"
                   "2-prepare first.\n")
    if search == '1':
        death()
        fight_mood()
    elif search == '2':
        survive()
        play_again()
    else:
        print_pause("Sorry i don't understand, try again")
        fight_mood()


def run_mood():

    print_pause("You glup and walk slowly toward "
                "the front door and run away.", 3)
    print_pause("How brave you are!!", 2)


def death():

    print_pause(f"You went after the {enemy}."
                "He saw you and becouse you didn't prepared.", 4)
    print_pause("'CONGRATES YOU DIED'", 2)
    print_pause("Come on budy!, try again but try not to die.", 3)


def survive():

    print_pause('You choosed to prepare, how clever.', 2)
    print_pause('You search around the house for a weapon '
                f'to fight the {enemy}.', 3)
    print_pause(f'you found a {weapon} in the office room.', 2)
    print_pause(f'You chased after the {enemy}.'
                'He saw you and tried to fight.', 3)
    print_pause(f'You fight him back with the {weapon}.'
                'He got affriad and run away.', 3)
    print_pause('Congrates! You survived.')


def play_again():
    print_pause("Do you want to play again?")

    again = input("Enter Y for Yes or N for No:\n").lower()
    if again == 'y':
        print_pause("Cool! have fun.")
        global enemy, weapon
        enemy = random.choice(enemies)
        weapon = random.choice(weapons)
        game()
    elif again == 'n':
        print_pause("To bad, thanks for playing.")
        print_pause("Bye bye.")
    else:
        print_pause("Sorry i don't understand, try again")
        play_again()


game()
