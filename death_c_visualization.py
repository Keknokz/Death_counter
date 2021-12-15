import time
import json

import plotly.io as pio

class DeathCounterVisualization:
    """A class to visualize deaths in games"""

    def __init__(self, file):
        """Initialize"""
        
        self.file = file
        
        self._get_game_boss_name
        self._get_data
        
        self.game_name = []
        
    def _get_game_boss_name(self):
        """returns the name of the game and the boss"""
        
        games = []
        
        with open(self.file, 'r') as f:
            deaths = json.load(f)
        
        for game in deaths.keys():
            games.append(game)
        print(games)
        game_name = input("What is the name of the game you want to visualize? ").title().strip()
        
        return game_name
        
        
    def _get_data(self):
        """gets the correct data from the game"""
        
        game = self._get_game_boss_name()
        self.game_name.append(game)
        
        boss_deaths_times = {}

        with open(self.file) as f:
            death_data = json.load(f)    
        
        for boss in death_data[game].keys():
            if "killed" in death_data[game][boss]['deaths'].keys():
                
                start_date = list(death_data[game][boss]['deaths']["1"].values())[0]
                
                num_deaths = list(death_data[game][boss]['deaths'].keys())[-2]

                end_date = list(death_data[game][boss]['deaths']["killed"].values())[0]
                
                boss_deaths_times[boss] = {'total deaths': num_deaths, 'start date': start_date, 'end date': end_date}
            
            elif "killed" not in death_data[game][boss]['deaths'].keys():
                
                start_date = list(death_data[game][boss]['deaths']["1"].values())[0]
                
                num_deaths = list(death_data[game][boss]['deaths'].keys())[-1]
                
                end_date = 'not killed'
                
                boss_deaths_times[boss] = {'total deaths': num_deaths, 'start date': start_date, 'end date': end_date}
        
        return boss_deaths_times          


    def visualize(self):
        """Visualizes the deaths in a game."""
        
        
        data = self._get_data()
        
        
        
        boss_names = list(data.keys())
        
        num_deaths = []
        start_date = []
        end_date = []
        
        game = self.game_name[0]
        
        for boss in boss_names:
            num_deaths.append(int(data[boss]['total deaths']))
            start_date.append(data[boss]['start date'])
            end_date.append(data[boss]['end date'])
        
        title = f"Your deaths in the game: {game.title()}"
        
        fig = dict({
            "data": [{"type": "bar",
                      "x": boss_names,
                      "y": num_deaths}],
            "layout": {"title": {"text": title}}
        })       
        pio.show(fig)


file = 'data/deaths_and_times.json'
    
te = DeathCounterVisualization(file)
te.visualize()