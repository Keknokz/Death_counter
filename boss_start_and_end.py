import json

from functions.clear import clear
from colorama import init, Fore


file = 'data/deaths_and_times.json'

def get_game_name():
    """Gets the name of the bosses"""
    
    init(autoreset=True)
        
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
    
    return deaths, game
            

def get_game_p_boss():
    """Gets the name of the game, and boss they want data for"""

    init(autoreset=True)
    
    with open(file) as f:
        deaths = json.load(f)
        
    while True:
        print(Fore.BLUE + "Here is a list of the games saved")
        
        for x in deaths.keys():
            print(Fore.MAGENTA + F"\n-- {x}")
            
        game = input(Fore.GREEN + "\nWhat game has the boss you want data for?\n ").title().strip()
        
        print(Fore.BLUE + "\nHere is a list of the bosses saved")

        for x in deaths[game].keys():
            print(Fore.MAGENTA + F"\n-- {x}")
            
        boss = input(Fore.GREEN + "\nWhat is the name of the boss you want data for?\n ").title().strip()
        
        if boss in deaths[game].keys():
            ans = input(Fore.GREEN + f"So you want data for {boss}?"
                        "\n(y/n): ").lower()
            
            if ans == 'y':
                break
            elif ans == 'n':
                continue
    
    return deaths, game, boss


def get_all_data():
    """Gets the start and end dates of the bosses"""
    
    init(autoreset=True)
    
    deaths, game = get_game_name()
    
    bosses = []
    start = []
    end = []
    
    for x in deaths[game].keys():
        bosses.append(x)
        start.append(deaths[game][x]['deaths']['start date']['time'])
        if "killed" in deaths[game][x]['deaths'].keys():
            end.append(deaths[game][x]['deaths']['killed'][f'{x} killed on:'])
        elif "killed" not in deaths[game][x]['deaths'].keys():
            end.append(f"{x} has not been killed yet")
            
    start.reverse()
    end.reverse()

    return bosses, start, end


def get_spes_data():
    """Gets specific data about a boss."""

    init(autoreset=True)
    
    deaths, game, boss = get_game_p_boss()
    
    start = (deaths[game][boss]['deaths']['start date']['time'])
    
    if "killed" in deaths[game][boss]['deaths'].keys():
        end = (deaths[game][boss]['deaths']['killed'][f'{boss} killed on:'])
    elif "killed" not in deaths[game][boss]['deaths'].keys():
        end = (f"{boss} has not been killed yet")
            
    return boss, start, end
        
    
def get_all_sae():
    """Gets all the start dates and end dates for a game"""
    bosses, start, end = get_all_data()
    
    print(Fore.GREEN + "----------------------------------------------")
    for x in bosses:
        print(Fore.MAGENTA + f"Boss name: {x.title()}")
        c = start.pop()
        v = end.pop()
        print(Fore.MAGENTA + F"Start date: {c}")
        if v == f"{x} has not been killed yet":
            print(Fore.MAGENTA + v)
        elif v != f"{x} has not been killed yet":
            print(Fore.MAGENTA + f"End date: {v}")
        print(Fore.GREEN + "----------------------------------------------")


def get_spes_sae():
    """Gets a specific bosses data"""
    
    boss, start, end = get_spes_data()
    
    print(Fore.GREEN + "----------------------------------------------")
    print(Fore.MAGENTA + f"Boss name: {boss}")
    print(Fore.MAGENTA + F"Start date: {str(start)}")
    if end == f"{boss} has not been killed yet":
        print(Fore.MAGENTA + str(end))
    elif end != f"{boss} has not been killed yet":
        print(Fore.MAGENTA + f"End date: {str(end)}")
    print(Fore.GREEN + "----------------------------------------------")

    
def main_sae_func():
    """Main function"""
    
    while True:
        ans = input(Fore.GREEN + "Do you want data for one or all?"
                    "\n(o/a): ").lower()
        
        if ans == 'o':
            clear()
            get_spes_sae()
        elif ans == 'a':
            clear()
            get_all_sae()
            
        exit_ans = input(Fore.GREEN + "Are you done?"
                         "\n(y/n): ").lower()
        
        if exit_ans == 'y':
            break
        elif exit_ans == 'n':
            continue
                    
main_sae_func() 