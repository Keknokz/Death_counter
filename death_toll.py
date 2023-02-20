import json
import time
import keyboard
import os
# All the imports


deaths_and_times = 'data/deaths_and_times.json'
number_deaths = 'data/number_deaths.json'
# Filenames and paths


boss_name = input("Are you fighting the boss from last time? \n"
                              "Or is this a new boss?\n"
                              "(type boss name for new boss: type 'n' to use last boss) ")
boss_name = boss_name.lower()
boss_ans = boss_name

try:
    with open(deaths_and_times) as f_o:
        with open(number_deaths) as f_t:
            if os.stat(deaths_and_times).st_size == 0:
                deaths = {boss_name: {}}
                death_count = []
                f_o.close(), f_t.close()
            elif boss_ans == 'n':
                death_count = json.load(f_t)
                deaths = json.load(f_o)
                boss_names = []
                for keys in deaths.keys():
                    boss_names.append(keys)
                boss_name = boss_names.pop()
            else:
                deaths = json.load(f_o)
                deaths[boss_name] = {}
                death_count = []
                print(deaths)
except FileNotFoundError:
    deaths = {boss_name: {}}
    death_count = []
# This makes the boss name and checks if they want to use the last boss
# it also makes the dict this uses


def counter():
    death_count.append('1')
    deaths[boss_name][str(len(death_count))] = {'time': time.strftime('%d: %m: %Y: %H_%M')}
    print(f"You have died {str(len(death_count))} times")
# This counter the deaths


while True:
    keyboard.add_hotkey("/", lambda: counter())
    keyboard.wait("1")

    with open(deaths_and_times, 'w') as f:
        json.dump(deaths, f, indent=4)
        f.close()
    with open(number_deaths, 'w') as f:
        json.dump(death_count, f, indent=2)
        f.close()
    print("Are you finished? (press '2' to finish)")
    keyboard.wait("2")
    break
# Main loop
