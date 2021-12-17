import os
import time
import json
import keyboard


file1 = 'data/deaths_and_times.json'
file2 = 'data/number_deaths.json'
# Basic files for this program


first_msg = ("\nWelcome to Death counter!\n"
    "\nThis program is ment to help keep track of deaths in games.\n"
    "First you will be asked to type in the name of the game you are playing.\n"
    "Then you will be prompted to type the boss you are fighting against.\n"
    "After this the program has started.\n"
    "\nNow everytime you hit '/' a death will be added.\n"
    "Once you are done, press ] to either choose to:\n"
    "\nrestart the program and add a new game or boss\n"
    "\n"
    "close the program.\n"
    "\nIf you are fighting the same boss from last time, enter the name of the game and boss, and it will add deaths to that.\n"
    "Thank you for using this program!")
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
            

def get_names_plus_make_stuff(empty):
    """
    Gets the name of the game and boss,
    and makes the dict containing them
    """ 
                
    if empty is True:
        
        game = input("\nWhat is the name of the game you are playing?\n ").strip()
        game = game.title()
        
        boss = input("\nWhat is the name of the boss you are fighting against?\n ").strip()
        boss = boss.title()
        
        deaths = {game: {boss: {'deaths': {}}}}
        count = False
        
        return deaths, count, game, boss
        
        
    elif empty is False:
        
        with open(file1, 'r') as f:
            deaths = json.load(f)
            
            print("Here is a list of games you have saved:\n")    
            for x in deaths.keys():
                print(f"-- {x}\n")
            
            game = input("What is the name of the game you are playing?\n ").strip()
            game = game.title()
            
                
        if game in deaths:
            print("\nHere is a list of bosses you have saved:\n")
            for x in deaths[game].keys():
                print(f"-- {x}\n")
            
            boss = input("What is the name of the boss you are fighing against?\n ").strip()
            boss = boss.title()
            
            
            if boss in deaths[game]:
                count = True
                return deaths, count, game, boss
            
            elif boss not in deaths:
                deaths[game][boss] = {'deaths': {}}
                count = False 
                return deaths, count, game, boss
        
        
        elif game not in deaths:
            boss = input("What is the name of the boss you are fighting against?\n ").strip()
            boss = boss.title()
            
            deaths[game] = {boss: {'deaths': {}}}
            count = False
            
            return deaths, count, game, boss
# This checks if the file is empty if it isn't
# it shows what games are saved in the file
# if bosses are in the game it shows the names of the bosses

def main_func():
    """Main loop of the program."""

    def counter():
        """
        This is the counter, if the boss hasnt been started it starts it
        otherwise it adds a death and saves it
        """
        if deaths[game][boss]['deaths']['start date']['time'] == 'n/a':
            deaths[game][boss]['deaths']['start date'] = {'time': time.strftime('%d/%m/%Y - %H:%M')}
            
        elif deaths[game][boss]['deaths']['start date']['time'] != 'n/a':
            number_deaths.append("1")
            deaths[game][boss]['deaths'][str(len(number_deaths))] = {'time': time.strftime('%d/%m/%Y - %H:%M')}
            
        with open(file1, 'w') as f:
            json.dump(deaths, f, indent=6)
        with open(file2, 'w') as f:
            json.dump(number_deaths, f, indent=6)


    while True:
        #Main loop
        empty = check_file()
        
        if empty is True:
            print(first_msg)
        
        elif empty is False:
            print("Welcome back!\n"
                  "\nCONTROLS:\n\n"
                  ":    '/'    adds a death\n\n"
                  ":    '1'    allows user to either restart and add new games or bosses, or close.\n\n")
            
        deaths, count, game, boss = get_names_plus_make_stuff(empty)
    
        #Checks if you want to start the boss now
        start_ans = input(f"\nIs this the start of you fighting: {boss}?\n(y/n)? ").lower()
        if start_ans == 'y':
            deaths[game][boss]['deaths']['start date'] = {'time': time.strftime('%d.%m.%Y: %H:%M')}
        elif start_ans == 'n':
            deaths[game][boss]['deaths']['start date'] = {'time': 'n/a'}
            print("\nHit '/' once you are ready to start, after this inital '/', all other '/' will add a death")
        
        with open(file1, 'w') as f:
            json.dump(deaths, f, indent=6)

        #Checks if the counter needs to be from another boss
        if count is True:
            with open(file1):
                place = json.load(file1)
                number_deaths = []
                for x in place[game][boss]['deaths'].keys():
                    number_deaths.append("1")
        
        elif count is False:
            number_deaths = []
            
        # Adds the hot key
        keyboard.add_hotkey("/", counter)
        ans = input("Type 'cls' to clear the screen\n"
                     "Type 'res' to restore it\n").lower()
        keyboard.wait("1")
        print("\nHave you killed this boss?\n")
        ans = input("(y/n): ").lower()
        
        # Checks if you have killed the boss
        if ans == 'y':
            deaths[game][boss]['deaths']['killed'] = {f"{boss} killed on:": time.strftime('%d.%m.%Y: %H:%M')}
            with open(file1, 'w') as f:
                json.dump(deaths, f, indent=6)
        if ans == 'n':
            pass
        break
