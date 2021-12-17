from logging import Handler
import time
import json

import plotly.graph_objects as go

class DeathCounterVisualization:
    """A class to visualize deaths in games"""

    def __init__(self):
        """Initialize"""
        
        self.file = 'data/deaths_and_times.json'
        
        self._get_game_name
        #self._get_data
        
        self.game_name = []
        
    def _get_game_name(self):
        """returns the name of the game and the boss"""
        
        games = []
        
        with open(self.file, 'r') as f:
            deaths = json.load(f)
        
        for game in deaths.keys():
            games.append(game)
        print(games)
        game_name = input("What is the name of the game you want to visualize? ").title().strip()
        
        return game_name
    
    
    def get_data(self):
        """Gets the data that plotly needs"""
        
    def main_vis_fun(self):
        """Main function"""
            
    