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
    
def check_file():
    """Checks if a file is empty, or dosnt exist"""
    
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
    """Gets the name of the game and boss."""
    
    game = input("What is the name of the game you are playing? ")
    game = game.title()
    
    boss = input("What is the name of the boss you are fighting against? ")
    boss = boss.title()
    
    return game, boss
# This gets the name of the game and the name of the boss


def make_or_load(empty):
    """Makes the dict and list or loads them"""
    
    game, boss = get_names()
    
    if empty is True:
        deaths = {game: {boss: {'deaths': {'times': {}}}}}
        count = []
        
        
        gbdp = True # gdpb means game, boss, death, brackets
        gbdteb = False # means game, boss, death, times equals brackets
        gbedb = False # means game, boss, equals deaths brackets
        gebbdb = False # means game, equals boss, brackets, death, brackets
        
        
        return deaths, count, gbdp, gbdteb, gbedb, gebbdb
    
    
    elif empty is False:
        with open (file1, 'r' ) as f:
            deaths = json.load(f)
        with open(file2, 'r') as f:
            count = json.load(f)
        if game in deaths:
            if boss in deaths[game]:
                deaths[game][boss]['deaths']['times'] = {}
                count = [] # place holder
                
                
                gbdp = False
                gbdteb = True
                gbedb = False
                gebbdb = False
                
                
                return deaths, count, gbdp, gbdteb, gbedb, gebbdb
            
            
            elif boss not in deaths:
                deaths[game][boss] = {'deaths': {'times': {}}}
                count = [] # place holder 
                
                
                gbdp = False
                gbdteb = False
                gbedb = True
                gebbdb = False
                
                
                return deaths, count, gbdp, gbdteb, gbedb, gebbdb
            
            
        elif game not in deaths:
            with open(file1, 'w') as f:
                deaths[game] = {boss: {'deaths': {'times': {}}}}
                count = [] #place holder
                
                
                gbdp = False
                gbdteb = False
                gbedb = False
                gebbdb = True
                
                
                return deaths, count, gbdp, gbdteb, gbedb, gebbdb
# This is a bunch of true or false tests, to see what should happen with the data
# aswell as to see what needs to happen on the counter function
            
            
def main():
    """Main loop of the program."""
    
    while True:
        empty = check_file()
        deaths, count, o1, o2, o3, o4 = make_or_load(empty)
        # o1, o2, o3, o4 are all basically a true or false test for
        # the counter part
        print(deaths, count)
        print(f"\n{o1}:{o2}:{o3}:{o4}")
        with open(file1, 'w') as f:
            json.dump(deaths, f, indent=6)
        with open(file2 , 'w') as f:
            json.dump(count, f, indent=6)
        break
# This is simply the main loop of the program
# that gets all the data and sends it to the right place

main()        
        
