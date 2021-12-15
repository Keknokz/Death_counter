import json

import death_toll
# imports the main module of death_counter


while True:
    """The main loop the runs this program"""
    
    death_toll.main_func()
    
    ans = input("\nDo you want to visualize your deaths?\n\n"
                "Or do you want to restart the program?\n\n"
                "Or do you want to close the program?\n\n"
                "(v/r/c): ").lower()
    
    if ans == 'v':
        pass
    elif ans == 'r':
        continue
    elif ans == 'c':
        break
    
    
    