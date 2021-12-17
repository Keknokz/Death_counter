import os
import time
import json
import keyboard
from colorama import init, Fore

from functions.clear import clear
from functions.msgs import death_toll_intro, death_toll_wel_back, death_toll_not_start, death_toll_control

file1 = 'data/deaths_and_times.json'
file2 = 'data/number_deaths.json'
# Basic files for this program

    
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
    
    init(autoreset=True)
          
    if empty is True:
    
        game = input(Fore.GREEN + "\nWhat is the name of the game you are playing?\n ").strip()
        game = game.title()
        
        boss = input(Fore.GREEN + "\nWhat is the name of the boss you are fighting against?\n ").strip()
        boss = boss.title()
        
        deaths = {game: {boss: {'deaths': {}}}}
        count = False
        clear()
        
        return deaths, count, game, boss
        
        
    elif empty is False:
        
        with open(file1, 'r') as f:
            deaths = json.load(f)
            
            print(Fore.BLUE + "\n\nHere is a list of games you have saved:")    
            for x in deaths.keys():
                print(Fore.MAGENTA + f"\n-- {x}")
            
            game = input(Fore.GREEN +"\nWhat is the name of the game you are playing?\n ").strip()
            game = game.title()
            
                
        if game in deaths:
            print(Fore.BLUE + "\nHere is a list of bosses you have saved:\n")
            for x in deaths[game].keys():
                print(Fore.MAGENTA + f"-- {x}\n")
            
            boss = input(Fore.GREEN + "What is the name of the boss you are fighing against?\n ").strip()
            boss = boss.title()
            
            
            if boss in deaths[game]:
                count = True
                clear()
                return deaths, count, game, boss
            
            elif boss not in deaths:
                deaths[game][boss] = {'deaths': {}}
                count = False 
                clear()
                return deaths, count, game, boss
        
        
        elif game not in deaths:
            boss = input(Fore.GREEN + "\nWhat is the name of the boss you are fighting against?\n ").strip()
            boss = boss.title()
            
            deaths[game] = {boss: {'deaths': {}}}
            clear()
            count = False
            
            return deaths, count, game, boss
# This checks if the file is empty if it isn't
# it shows what games are saved in the file
# if bosses are in the game it shows the names of the bosses

def main_func():
    """Main loop of the program."""
    
    init(autoreset=True)

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
            death_toll_intro()
        
        elif empty is False:
            death_toll_wel_back()
            
            
        deaths, count, game, boss = get_names_plus_make_stuff(empty)
    
    
        #Checks if you want to start the boss now
        start_ans = input(Fore.GREEN + f"Are you away to fight {boss} for the first time."
                          "\nThis adds a start date. If you have already started fighing this boss put --n--"
                          "\nIf this is the start of this boss, put --y--\n"
                          "(y/n): ").lower()
        
        if start_ans == 'y':
            try:
                if start_ans == 'y':
                    if deaths[game][boss]['deaths']['start date'] != 'n/a':
                        clear()
                        print(Fore.BLUE + f"{boss}: has already been started\n")
                        continue
                    
                    elif deaths[game][boss]['deaths']['start date'] == 'n/a':
                        deaths[game][boss]['deaths']['start date'] = {'time': time.strftime('%d.%m.%Y: %H:%M')}
            except KeyError:
                deaths[game][boss]['deaths']['start date'] = {'time': time.strftime('%d/%m/%Y - %H:%M')}
            
        elif start_ans == 'n':
            try:
                if "n/a" in deaths[game][boss]['deaths']['start date']['time']:
                    clear()
                    death_toll_not_start()
                    deaths[game][boss]['deaths']['start date'] = {'time': 'n/a'}
                    
            except KeyError:
                clear()
                death_toll_not_start()
                deaths[game][boss]['deaths']['start date'] = {'time': 'n/a'}
        

        with open(file1, 'w') as f:
            json.dump(deaths, f, indent=6)

        #Checks if the counter needs to be from another boss
        if count is True:
            number_deaths = []
            
            if "killed" in deaths[game][boss]['deaths'].keys():
                clear()
                print(Fore.BLUE + f"{boss} has already been killed.\n")
                continue
            
            elif "killed" not in deaths[game][boss]['deaths'].keys():
            
                if "start date" in deaths[game][boss]['deaths'].keys():
            
                    for i in deaths[game][boss]['deaths'].keys():
                        number_deaths.append("1")
                    number_deaths.pop()
            
        elif count is False:
            number_deaths = []

        # Adds the hot key
        keyboard.add_hotkey("/", counter)
        death_toll_control()
        keyboard.wait("1")
        clear()
        print(Fore.GREEN + "\nHave you killed this boss?\n")
        ans = input(Fore.GREEN + "(y/n): ").lower()
        
        # Checks if you have killed the boss
        if ans == 'y':
            deaths[game][boss]['deaths']['killed'] = {f"{boss} killed on:": time.strftime('%d.%m.%Y: %H:%M')}
            with open(file1, 'w') as f:
                json.dump(deaths, f, indent=6)
        if ans == 'n':
            pass
        break
