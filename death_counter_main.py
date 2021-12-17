from functions.msgs import main_file_intro
from functions.clear import clear

import death_toll


flag = True


def main_function(flag):
    """Main function for this whole program"""
    
    while flag is True:
        """Main loop"""
        
        main_file_intro()
        
        while True:
            fun_ans = input("--> ").lower()
            
            if fun_ans == 'close':
                break
            
            elif fun_ans == 'cls':
                clear()
                
            elif fun_ans == 'res':
                main_file_intro()
            
        break
                
        
main_function(flag)