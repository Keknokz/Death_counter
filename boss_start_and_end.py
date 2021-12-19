import json

from functions.clear import clear
from colorama import init, Fore


init(autoreset=True)

file = 'data/deaths_and_times.json'

def get_boss_name():
    """Gets the name of the bosses"""
    
    with open(file) as f:
        deaths = json.load(f)
        
    while True:    
        print(Fore.BLUE + "Here is a list of games saved")
    
        for x in deaths.keys():
            print(Fore.MAGENTA + F"\n-- {x}")
    
        game = input(Fore.GREEN + "\nWhat games bosses do you want to get the start and end dates for?\n ").title().strip()
        
        print(Fore.BLUE + "\nAre these the games you watn to get the start and end dates for?")
        
        for x in deaths[game].keys():
            print(Fore.MAGENTA + F"\n-- {x}")
            
        boss_ans = input(Fore.GREEN + "\n(y/n): ").lower()
        
        if boss_ans == 'y':
            break
        if boss_ans == 'n':
            clear()
            continue
            
            
get_boss_name()