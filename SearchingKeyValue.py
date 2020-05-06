MLB_team = {'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins',
'Milwaukee': 'Brewers', 'Seattle': 'Seahawks', 'Kansas City': 'Royals'}
Team = str(input("Input a new key : "))
for x in MLB_team:
    if Team == x:
        print('yeah')
