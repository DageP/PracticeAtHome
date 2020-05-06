MLB_team = {'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins',
'Milwaukee': 'Brewers', 'Seattle': 'Mariners', 'Kansas City': 'Royals'}
Numbers = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
d = MLB_team.copy() # Copies all the items in MLB_team
d.update(Numbers) # Adds all the items in numbers into MLB_team
print(d)
