import os
import time
import json
import keyboard
# os, for checking files
# time to get time of death
# json to load stuff
# keyboard to set hot keys


file1 = 'data/deaths_and_times.json'
file2 = 'data/number_deaths.json'
# Basic files for this program


first_msg = ("\nWelcome to Death counter!\n"
    "\nThis program is ment to help keep track of deahts in games.\n"
    "First you will be asked to type in the name of the game you are playing.\n"
    "Then you will be prompted to type the boss you are fighting against.\n"
    "After this the program is started\n"
    "\nNow everytime you hit '/' a death will be added\n"
    "Once you are done, press ] to either choose to:\n"
    "\nRestart the program and add a new boss, or new boss and game.\n"
    "\nClose the program.\n"
    "Thank you for using this program!\n")
# Msg to be displayed the first time the program is started
    
def check_file():
    """Checks if a file is empty, or doesn't exist"""
    
    try:
        with open(file1, 'r'):
            if os.path.getsize(file1) == 0:
                return True
            elif os.path.getsize(file1) != 0:
                return False
    except FileNotFoundError:
        with open(file1, 'w') as f:
            f.close()
        with open(file2, 'w') as f:
            f.close()
        return True
    # Checks if a file is empty and looks for a FileNotFoundError
    # if the error happens it makes the files
            

def get_names():
    """Gets the name of the game and boss."""
    
    game = input("What is the name of the game you are playing? ")
    game = game.title()
    
    boss = input("What is the name of the boss you are fighting against? ")
    boss = boss.title()
    
    return game, boss
# This gets the name of the game and the name of the boss


def make_or_load(empty):
    """Makes the dict and list or loads them"""
    
    game, boss = get_names()

    if empty is True:
        deaths = {game: {boss: {'times': {}}}}
        count = False
        return deaths, count, game, boss
        
    elif empty is False:
        with open(file1, 'r') as f:
            deaths = json.load(f)
        if game in deaths:
            if boss in deaths[game]:
                count = True
                return deaths, count, game, boss
            
            elif boss not in deaths:
                deaths[game][boss] = {'times': {}}
                count = False 
                return deaths, count, game, boss
            
        elif game not in deaths:
            deaths[game] = {boss: {'times': {}}}
            count = False
            return deaths, count, game, boss
# This is a bunch of true or false tests, to see what should happen with the data
# as well as to see what needs to happen on the counter function

    
def main():
    """Main loop of the program."""

    def counter():
        number_deaths.append("1")
        deaths[game][boss]['times'][str(len(number_deaths))] = {'time': time.strftime('%d: %m: %Y: %H_%M')}
        
        with open(file1, 'w') as f:
            json.dump(deaths, f, indent=6)
        with open(file2, 'w') as f:
            json.dump(number_deaths, f, indent=6)

    while True:
        empty = check_file()
        if empty is True:
            print(first_msg)
        elif empty is False:
            print("Welcome back!\n")
        deaths, count, game, boss = make_or_load(empty)

        if count is True:
            with open(file1, 'r') as f:
                place = json.load(f)
                number_deaths = []
                for x in place[game][boss]['times'].keys():
                    number_deaths.append("1")
        
        elif count is False:
            number_deaths = []
            
        keyboard.add_hotkey("/", counter)
        keyboard.wait("1")
        break
# This is simply the main loop of the program
# that gets all the data and sends it to the right place


while True:
    main()
    ans = input("Do you want to close or restart? (c/r): ").lower()
    
    if ans == "c":
        break
    elif ans == "r":
        continue     
        
