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
    "After this the program is on.\n"
    "\nNow everytime you hit '/' a death will be added.\n"
    "Once you are done, press ] to either choose to:\n"
    "\nrestart the program and add a new game or boss\n"
    "Or\n"
    "close the program.\n"
    "\nIf you are fighting the same boss from last time, enter the name of the game and boss, and it will add to that.\n"
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
    """\nGets the name of the game and boss."""
    
    game = input("\nWhat is the name of the game you are playing?\n ").strip()
    game = game.title()
    
    boss = input("\nWhat is the name of the boss you are fighting against?\n ").strip()
    boss = boss.title()
    
    return game, boss
# This gets the name of the game and the name of the boss


def make_or_load(empty):
    """Makes the dict and list or loads them"""
    
    game, boss = get_names()

    if empty is True:
        deaths = {game: {boss: {'deaths': {}}}}
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
                deaths[game][boss] = {'deaths': {}}
                count = False 
                return deaths, count, game, boss
            
        elif game not in deaths:
            deaths[game] = {boss: {'deaths': {}}}
            count = False
            return deaths, count, game, boss
# This is a bunch of true or false tests, to see what should happen with the data
# as well as to see what needs to happen on the counter function

    
def main_func():
    """Main loop of the program."""

    def counter():
        number_deaths.append("1")
        deaths[game][boss]['deaths'][str(len(number_deaths))] = {'time': time.strftime('%d.%m.%Y - %H:%M')}
        
        
        with open(file1, 'w') as f:
            json.dump(deaths, f, indent=6)
        with open(file2, 'w') as f:
            json.dump(number_deaths, f, indent=6)

    while True:
        empty = check_file()
        if empty is True:
            print(first_msg)
        elif empty is False:
            print("Welcome back!\n"
                  "\nCONTROLS:\n"
                  ":    '/'    adds a death\n"
                  ":    '1'    allows user to either restart and add new games or bosses, or close.")
        deaths, count, game, boss = make_or_load(empty)
        with open(file1, 'w') as f:
            json.dump(deaths, f, indent=6)

        if count is True:
            with open(file1, 'r') as f:
                place = json.load(f)
                number_deaths = []
                for x in place[game][boss]['deaths'].keys():
                    number_deaths.append("1")
        
        elif count is False:
            number_deaths = []
            
        keyboard.add_hotkey("/", counter)
        keyboard.wait("1")
        print("Have you killed this boss?\n")
        ans = input("(y/n): ").lower()
        
        if ans == 'y':
            deaths[game][boss]['deaths']['killed'] = {f"{boss} was killed on:": time.strftime('%d.%m.%Y: %H:%M')}
            with open(file1, 'w') as f:
                json.dump(deaths, f, indent=6)
        if ans == 'n':
            pass
        break
# This is simply the main loop of the program
# that gets all the data and sends it to the right place