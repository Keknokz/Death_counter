import json
from colorama import init, Fore
import plotly.graph_objects as go
# main imports


from functions.msgs import Visualization
from functions.clear import clear
# function imports


class DeathCounterVisualization:
    """A class to visualize deaths in games"""

    def __init__(self):
        """Initialize"""
        
        self.file = 'data/deaths_and_times.json'
        
        # this is for the msgs
        
        self._get_game_name
        self._get_data
        # helper functions
        
        init(autoreset=True)
        
    
    def _get_game_name(self):
        """Gets the names of the games that can be visualized"""
        
        with open(self.file) as f:
            deaths = json.load(f)
            
            print(Fore.BLUE + "\nHere is a list of games that can be visualized:")
            for x in deaths.keys():
               print(Fore.MAGENTA + f"\n-- {x}")
            
            ans = input(Fore.GREEN + "\nWhat is the name of the game you want to visualize?\n ").strip().lower()
            game = ans.title()
            # gets the game name
            
        return deaths, game
    
    
    def _get_data(self):
        """Gets the right data"""
        
        deaths, game = self._get_game_name()
        
        boss_names = []
        num_deaths = []
        
        for x in deaths[game].keys():
            boss_names.append(x)
            
        for x in boss_names:
            if "killed" in deaths[game][x]['deaths'].keys():
                num_deaths.append(int(list(deaths[game][x]['deaths'].keys())[-2]))
            
            elif "killed" not in deaths[game][x]['deaths'].keys():
                num_deaths.append(int(list(deaths[game][x]['deaths'].keys())[-1]))
            # makes sure it gets the right key
            
        return game, boss_names, num_deaths
    
    
    def main_vis(self):
        """Main functions of the visual part"""
        
        v = Visualization
        
        v.vis_intro()
        
        while True:
                
            game, boss_names, num_deaths = self._get_data()
            
            title = (f"Deaths in {game}")
            
            fig = go.Figure(data=[go.Bar(
                x=boss_names, y=num_deaths,
                text=num_deaths,
                textposition='auto',
                hoverinfo="x",
            )])
            
            fig.update_traces(
                marker_line_color='rgb(15, 145, 240)', marker_color='rgb(125, 84, 250)',
                marker_line_width=1.5, opacity=0.5
            )
            
            fig.update_layout(
                title=title,
                )
            
            fig.show()
            
            clear()
            
            ans = input(Fore.GREEN + "Do you want to get another visualization?\n"
                        "Or do you want to quti?\n"
                        "(r/q): ").lower()
            
            if ans == 'r':
                continue
            
            elif ans == 'q':
                break
        # main visualization loop