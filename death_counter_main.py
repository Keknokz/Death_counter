from re import M
from colorama import init, Fore

from functions.msgs import main_file_intro
from functions.clear import clear

import death_toll


def main_function():
    """Main function for this whole program"""
    
    init(autoreset=True)
    
    main_file_intro()
    
    while True:
        """Main loop for choosing a function"""
        
        ans = input(Fore.GREEN + "--> ").lower()
        
        if ans == 'count':
            clear()
            death_toll.main_func()
        
        if ans == 'cls':
            clear()
            continue
        
        elif ans == 'res':
            main_file_intro()
        
        elif ans == 'close':
            break
        
main_function()