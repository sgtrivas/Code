players = 8
teams = list()
bool = True

for i in range(players):
    if bool:
        teams.insert(i, "Even")
        print(f'{i}+{teams}')
    else:
        teams.insert(i, "Odd")
        print(f'{i}+{teams}')
    bool = not bool
#print(f'{i}teams')