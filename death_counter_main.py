import death_toll

while True:
    death_toll.main_func()
    ans = input("\nDo you want to close or restart? (c/r):\n ").lower()
    
    if ans == "c":
        break
    elif ans == "r":
        continue     