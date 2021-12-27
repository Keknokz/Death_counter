import json
# main import


from functions.msgs import SaE
from functions.clear import clear
from colorama import init, Fore
# function imports


file = 'data/deaths_and_times.json'
# file to be used


def get_game_name():
    """Gets the name of the bosses"""
    
    init(autoreset=True)
        
    with open(file) as f:
        deaths = json.load(f)
        
    while True:    
        print(Fore.BLUE + "Here is a list of games saved")
    
        for x in deaths.keys():
            print(Fore.MAGENTA + F"\n-- {x}")
    
        game = input(Fore.GREEN + "\nWhat games bosses do you want to get the start and end dates for?\n ").strip()
        game = game.title()
        
        clear()
        print(Fore.BLUE + "Are these the bosses you want to get the start and end dates for?")
        
        for x in deaths[game].keys():
            print(Fore.MAGENTA + F"\n-- {x}")
        
        boss_ans = input(Fore.GREEN + "\n(y/n): ").lower()
        
        if boss_ans == 'y':
            clear()
            break
        if boss_ans == 'n':
            clear()
            continue
    # shows the user what games can be visualized
    
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
            
        game = input(Fore.GREEN + "\nWhat game has the boss you want data for?\n ").strip()
        game = game.title()
        
        print(Fore.BLUE + "\nHere is a list of the bosses saved")

        for x in deaths[game].keys():
            print(Fore.MAGENTA + F"\n-- {x}")
            
        boss = input(Fore.GREEN + "\nWhat is the name of the boss you want data for?\n ").strip()
        boss = boss.title()
        
        clear()
        if boss in deaths[game].keys():
            ans = input(Fore.GREEN + f"So you want data for {boss}?"
                        "\n(y/n): ").lower()
            
            if ans == 'y':
                clear()
                break
            elif ans == 'n':
                clear()
                continue
    
    return deaths, game, boss
# gets the user to say what game and boss they want data for


def get_all_data():
    """Gets the start and end dates of the bosses"""
    
    init(autoreset=True)
    
    deaths, game = get_game_name()
    
    bosses = []
    start = []
    end = []
    number_deaths = []
    num = []
    
    for x in deaths[game].keys():
        bosses.append(x)
        start.append(deaths[game][x]['deaths']['start date']['time'])
        if "killed" in deaths[game][x]['deaths'].keys():
            end.append(deaths[game][x]['deaths']['killed'][f'{x} killed on:'])
            
            for i in deaths[game][x]['deaths'].keys():
                num.append("1")
            num.pop()
            num.pop()
           
            number_deaths.append(len(num))
            
            num.clear()
            
        elif "killed" not in deaths[game][x]['deaths'].keys():
            end.append(f"{x} has not been killed yet")
            
            for i in deaths[game][x]['deaths'].keys():
                num.append("1")
            num.pop()
            
            number_deaths.append(len(num))
            
            num.clear()
            
    start.reverse()
    end.reverse()
    number_deaths.reverse()

    return bosses, start, end, number_deaths
# gets all the data from one game


def get_spes_data():
    """Gets specific data about a boss."""

    init(autoreset=True)
    
    deaths, game, boss = get_game_p_boss()
    
    number_deaths = []
    
    start = (deaths[game][boss]['deaths']['start date']['time'])
    
    if "killed" in deaths[game][boss]['deaths'].keys():
        end = (deaths[game][boss]['deaths']['killed'][f'{boss} killed on:'])
        
        for i in deaths[game][boss]['deaths'].keys():
            number_deaths.append("1")
        number_deaths.pop()
        number_deaths.pop()
        number_deaths = len(number_deaths)
            
        
    elif "killed" not in deaths[game][boss]['deaths'].keys():
        end = (f"{boss} has not been killed yet")
        
        for i in deaths[game][boss]['deaths'].keys():
            number_deaths.append("1")
        number_deaths.pop()
        number_deaths = len(number_deaths)
                    
    return boss, start, end, number_deaths
# gets specific data from a boss
        
    
def get_all_sae():
    """Gets all the start dates and end dates for a game"""
    
    bosses, start, end, number_deaths = get_all_data()
    
    
    print(Fore.GREEN + "----------------------------------------------")
    for x in bosses:
        print(Fore.MAGENTA + f"Boss name: {x}")
        c = start.pop()
        v = end.pop()
        b = number_deaths.pop()
        print(Fore.MAGENTA + f"Number of deaths: {str(b)}")
        print(Fore.MAGENTA + F"Start date: {str(c)}")
        if v == f"{x} has not been killed yet":
            print(Fore.MAGENTA + v)
        elif v != f"{x} has not been killed yet":
            print(Fore.MAGENTA + f"End date: {str(v)}")
        print(Fore.GREEN + "----------------------------------------------")
    # shows all data for a game


def get_spes_sae():
    """Gets a specific bosses data"""
    
    boss, start, end, number_deaths = get_spes_data()
    
    clear()
    
    print(Fore.GREEN + "----------------------------------------------")
    print(Fore.MAGENTA + f"Boss name: {boss}")
    print(Fore.MAGENTA  + f"Number of deaths: {number_deaths}")
    print(Fore.MAGENTA + F"Start date: {str(start)}")
    if end == f"{boss} has not been killed yet":
        print(Fore.MAGENTA + str(end))
    elif end != f"{boss} has not been killed yet":
        print(Fore.MAGENTA + f"End date: {str(end)}")
    print(Fore.GREEN + "----------------------------------------------")
# gets specific data for a boss
    
def main_sae_func():
    """Main function"""
    
    s = SaE
    s.saeintro()
    
    while True:
        ans = input(Fore.GREEN + "Do you want data for one or all?"
                    "\n(o/a): ").lower()
        
        if ans == 'o':
            clear()
            get_spes_sae()
        elif ans == 'a':
            clear()
            get_all_sae()
            
        exit_ans = input(Fore.GREEN + "Do you want to get data for any more or quit?"
                         "\n(r/q): ").lower()
        
        if exit_ans == 'r':
            clear()
            continue
        elif exit_ans == 'q':
            clear()
            break
    # they main loop that asks if they 
    # want to get data for one
    # or all