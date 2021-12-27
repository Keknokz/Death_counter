from colorama import init, Fore
# main import


import death_toll
import death_c_visualization
import boss_start_and_end
# imports for main functions


from functions.msgs import MainFile
from functions.clear import clear
# side imports

def main_function():
    """Main function for this whole program"""
    
    init(autoreset=True)
    
    mf = MainFile
    
    mf.main_file_intro()
    
    d = death_c_visualization
    dcv = d.DeathCounterVisualization()
    
    
    while True:
        """Main loop for choosing a function"""
        
        ans = input(Fore.GREEN + "--> ").lower().strip()
        
        if ans == 'cnt':
            while True:
                clear()
                death_toll.main_func()
                
                res_ans = input(Fore.GREEN + "\nDo you want to track another game/boss?\n"
                                "Or do you want to quit?\n"
                                "(r/q): ").lower()
                
                if res_ans == 'r':
                    continue
                elif res_ans == 'q':
                    break
                # starts death toll 
                # and asks if the user wants to start it again
                # or quit
        
        elif ans == 'vis':
            while True:
                clear()
                
                dcv.main_vis()
                break
            
        elif ans == 'sae':
            while True:
                clear()
                boss_start_and_end.main_sae_func()
                
                clear()
                res_ans = input(Fore.GREEN + "\nAre you sure you want to quit this function?\n"
                                "(y/n)").lower()
                
                if res_ans == 'y':
                    break
                elif res_ans == 'n':
                    continue
            
        elif ans == 'cls':
            clear()
            continue
        
        elif ans == 'res':
            mf.main_file_intro()
        
        elif ans == 'quit':
            break
        
main_function()