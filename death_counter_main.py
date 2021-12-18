from colorama import init, Fore

from functions.msgs import MainFile
from functions.clear import clear

import death_toll


def main_function():
    """Main function for this whole program"""
    
    init(autoreset=True)
    
    mf = MainFile
    
    mf.main_file_intro()
    
    while True:
        """Main loop for choosing a function"""
        
        ans = input(Fore.GREEN + "--> ").lower().strip()
        
        if ans == 'count':
            while True:
                clear()
                death_toll.main_func()
                res_ans = input(Fore.GREEN + "\nDo you want to track another game/boss?\n"
                                "Or do you want to quit?\n"
                                "('r'/'q'): ").lower()
                
                if res_ans == 'r':
                    continue
                elif res_ans == 'q':
                    break
                    
            
        #elif ans == 'vis':
            
        
        elif ans == 'cls':
            clear()
            continue
        
        elif ans == 'res':
            mf.main_file_intro()
        
        elif ans == 'close':
            break
        
main_function()