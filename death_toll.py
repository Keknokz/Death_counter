import os
import time
import json
import keyboard
from colorama import init, Fore
# main imports


from functions.clear import clear
from functions.msgs import Counter 
# function imports


file1 = 'data/deaths_and_times.json'
file2 = 'data/number_deaths.json'
# file paths


c = Counter
# the functions imports

    
def check_file():
    """Checks if a file is empty, or doesn't exist"""
    
    if not os.path.exists('data'):
        os.mkdir('data')
        
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
    # Checks if the file is empty
    # If it gets a file not found error it makes the files
            

def get_names_plus_make_stuff(empty):
    """
    Gets the name of the game and boss,
    and makes the dict containing them
    """ 
    
    init(autoreset=True)
          
    if empty is True:
    
        game = input(Fore.GREEN + "\nWhat is the name of the game you are playing?\n ").strip()
        game = game.title()
        
        boss = input(Fore.GREEN + "\nWhat is the name of the boss you are fighting?\n ").strip()
        boss = boss.title()
        
        deaths = {game: {boss: {'deaths': {}}}}
        count = False
        clear()
        
        return deaths, count, game, boss
        # if the file is empty then it only
        # has to get the name of the game and boss
        
        
    elif empty is False:
        
        with open(file1, 'r') as f:
            deaths = json.load(f)
            
            print(Fore.BLUE + "\n\nHere is a list of games you have saved:")    
            for x in deaths.keys():
                print(Fore.MAGENTA + f"\n-- {x}")
            
            game = input(Fore.GREEN +"\nWhat is the name of the game you are playing?\n ").strip()
            game = game.title()
            # if the it isnt empty then
            # it shows what games are saved
                        
                
        if game in deaths:
            print(Fore.BLUE + "\n\nHere is a list of bosses you have saved:")
            for x in deaths[game].keys():
                print(Fore.MAGENTA + f"\n-- {x}")
            
            boss = input(Fore.GREEN + "\nWhat is the name of the boss you are fighting?\n ").strip()
            boss = boss.title()
            # it shows what bosses are saved so you 
            # can fight a boss saved or a new one
            
            
            if boss in deaths[game]:
                count = True
                clear()
                return deaths, count, game, boss
                # if the boss is in the game 
                # it needs to start from the last death
            
            elif boss not in deaths:
                deaths[game][boss] = {'deaths': {}}
                count = False 
                clear()
                return deaths, count, game, boss
                # if the boss isnt in the game it adds it
        
        
        elif game not in deaths:
            boss = input(Fore.GREEN + "\nWhat is the name of the boss you are fighting?\n ").strip()
            boss = boss.title()
            
            deaths[game] = {boss: {'deaths': {}}}
            clear()
            count = False
            
            return deaths, count, game, boss
            # if the game isnt saved it adds
            # the game
            
            
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
            # if there is no start date it adds one
            
        elif deaths[game][boss]['deaths']['start date']['time'] != 'n/a':
            number_deaths.append("1")
            deaths[game][boss]['deaths'][str(len(number_deaths))] = {'time': time.strftime('%d/%m/%Y - %H:%M')}
            # if there is a start date it adds a death
            
        with open(file1, 'w') as f:
            json.dump(deaths, f, indent=6)
        with open(file2, 'w') as f:
            json.dump(number_deaths, f, indent=6)
            # saves it


    while True:
        #Main loop
        empty = check_file()
        
        if empty is True:
            c.death_toll_intro()
        
        elif empty is False:
            c.death_toll_wel_back()
        # checks what intro it has to print
            
            
        deaths, count, game, boss = get_names_plus_make_stuff(empty)
        # makes the var
    
    
        start_ans = input(Fore.GREEN + f"Are you away to fight {boss} for the first time."
                          "\nThis adds a start date."
                          "\nIf this is the start of this boss, put --y--\n"
                          "\nIf you have already started fighing this boss put --n--"
                          "(y/n): ").lower()
        # checks if you have just started the boss
        # if you have yet to start 
        # or if you are continuing 
        
        if start_ans == 'y':
            try:
                if start_ans == 'y':
                    if deaths[game][boss]['deaths']['start date'] != 'n/a':
                        clear()
                        print(Fore.BLUE + f"{boss}: has already been started\n")
                        continue
                        # checks if the boss has already been started
                    
                    elif deaths[game][boss]['deaths']['start date'] == 'n/a':
                        deaths[game][boss]['deaths']['start date'] = {'time': time.strftime('%d/%m/%Y: %H:%M')}
                        clear()
                        c.death_toll_control()
                        # adds a start date if their isnt one
                        
            except KeyError:
                clear()
                c.death_toll_control()
                deaths[game][boss]['deaths']['start date'] = {'time': time.strftime('%d/%m/%Y - %H:%M')}
                # if there is a key error make the start date
                
        elif start_ans == 'n':
            try:
                if "n/a" in deaths[game][boss]['deaths']['start date']['time']:
                    clear()
                    c.death_toll_not_start()
                    deaths[game][boss]['deaths']['start date'] = {'time': 'n/a'}
                
                elif "n/a" not in deaths[game][boss]['deaths']['start date']['time']:
                    clear()
                    c.death_toll_control()
                # checks if this is a continuation or not
                
            except KeyError:
                clear()
                c.death_toll_not_start()
                deaths[game][boss]['deaths']['start date'] = {'time': 'n/a'}
            # if their is a key error it makes the right dict
        

        with open(file1, 'w') as f:
            json.dump(deaths, f, indent=6)
            # saves

        if count is True:
            number_deaths = []
            
            if "killed" in deaths[game][boss]['deaths'].keys():
                clear()
                print(Fore.BLUE + f"{boss} has already been killed.\n")
                continue
            # checks if the boss has already been killed
            
            elif "killed" not in deaths[game][boss]['deaths'].keys():
            
                if "start date" in deaths[game][boss]['deaths'].keys():
            
                    for i in deaths[game][boss]['deaths'].keys():
                        number_deaths.append("1")
                    number_deaths.pop()
            # if not it gets the right number of deaths
            
        elif count is False:
            number_deaths = []

        # Adds the hot key
        keyboard.add_hotkey("/", counter)
        keyboard.wait("1")
        # adds the hot key
        # the wait is to stop input lag
        
        clear()
        print(Fore.BLUE + f"Have you killed {boss}\n")
        ans = input(Fore.GREEN + "(y/n): ").lower()
        
        # Checks if you have killed the boss
        if ans == 'y':
            deaths[game][boss]['deaths']['killed'] = {f"{boss} killed on:": time.strftime('%d.%m.%Y: %H:%M')}
            with open(file1, 'w') as f:
                json.dump(deaths, f, indent=6)
        if ans == 'n':
            pass
        # checks if you have killed the boss
        break
        