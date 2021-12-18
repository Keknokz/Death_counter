from colorama import init, Fore

class MainFile:
    
    def main_file_intro():
        """Intro text for death counter"""
        
        init(autoreset=True)

        print(Fore.RED + "Welcome to --DEATH COUNTER--")
        print(Fore.RED + "This program does quite a few things from counting deaths, to showing you how many times you died\n"
            "with time stamps\n"
            "\nSoon this program will ask you to type in what you want to do,\nso here is a list of functions, their commands, with a short description")
        
        
        print(Fore.BLUE  + "\n\n--Counter--\n"
            "Counter is the backbone of this program, so if this is your first time you will need to run it\n"
            "What it does is gets the name of the game you are playing,\n"
            "and the boss you are fighting. Then everytime you hit '/' it adds a death\n"
            "If there is no data in their this program will not work"
            "\n\nIts command is 'count")
        
        
        print(Fore.GREEN + "\n\n--Visualization--\n"
            "Visualization has been the bane of me, it was ment to show your deaths with the time you started fighing the boss,\n"
            "and the time you killed it."
            "\nI tried for a long time and couldn't get it to work so it only shows you a bar chart with names and deaths.\n"
            "You need to have data with --counter-- for this to work."
            "\n\nIts command is 'vis'")
        
        
        print(Fore.MAGENTA + "\n\n--Start and End times--\n"
            "This is almost like the lost feature of --vis-- but it still works.\n"
            "If you have data in --count-- this should work. It will show you the name of the boss,\n"
            "when you started fighing it, and if you killed it when."
            "\n\nIts command is 'sae'")
        
        
        print(Fore.YELLOW + "\n\n--NOTE--\n"
            "If you type 'cls' at any point it will clear the screen\n"
            "If you type 'res' at any point it will restore the screen")
        
        print(Fore.RED + "\nWhat do you want to do?\n")
        
        print(Fore.BLUE + "--count--\n",
            Fore.GREEN + "--vis--\n",
            Fore.MAGENTA + "--sae--\n",
            Fore.YELLOW + "--cls--\n" 
                        "--res--\n"
                        "--close\n"
            )
        

class Counter:

    def death_toll_intro():
        """Intro for counter function"""
        
        init(autoreset=True)
        
        print(Fore.RED + "Welcome to the counter part of this program!"
            "\nThis was really the start of it all, it was only ment to be this, and well"
            "\nI made it into more, so i will, in a moment tell you how this works and what to do.\n")
        
        
        print(Fore.BLUE + "\nSo to start you will be asked to enter the name of the game you are playing."
            "\nNext you will be asked to enter the bosses name, __MAKE SURE YOU ENTER IT RIGHT"
            "AS THIS CAN'T BE CHANGED__"
            "\nNext it will ask if you are starting the boss now, all this does"
            "\nis add the start time. If you put no, the first death you add will add a start time.\n"
                "Next ill show you the controls.")
        
        
        print(Fore.YELLOW+ "\n\n--Controls--\n"
            "\nTo add a death press --/-- this will add the number of the death and the time of it.\n"
            "\nTo stop this program press --1-- this will ask if you have killed the boss."
            "\nAll this does is add a time that you killed the boss")
        
        
    def death_toll_wel_back():
        """Welcome back for counter function"""
        
        init(autoreset=True)
        
        print(Fore.RED + "Welcome back!")
        
        
        print(Fore.YELLOW + "\n--Controls--\n"
            "\n--/-- to add a death"
            "\n\n--1-- to stop")
        

    def death_toll_not_start():
        """Prints if you haven't started the boss"""
        
        print(Fore.YELLOW + "Hit --/-- once you are ready to start.\n"
            "After this inital --/--, all other --/-- will add a death\n")


    def death_toll_control():
        """Controls for counter function"""
        
        print(Fore.YELLOW + "--/-- to add a death")
        
        print(Fore.YELLOW + "\nPress --1-- to stop")
        

class Visualization:
    """Text for the visualization part"""
    
    def vis_intro():
        """Prints when you start vis"""
        
        print(Fore.RED + "Welcome to the Visualization function\n"
              "This is the part that took the fucking longest time to finish.\n"
              "It was ment to have alot more fetures than what it does now, but i can't be bothered reading plotly documentaion.\n"
              "Anyway, first you will be asked which game you want to visualize, then it will show you a visualization\n"
              "After that you can choose to exit this function, or visualize another game.")