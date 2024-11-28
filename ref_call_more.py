#3- DOES ONE REF CALL MORE FOULS?
"""
for r1
aup=[fc1, fc2, ...fcn]
fgcu=[fc1, fc2, .. fcn]
foneway[aup, fgcu,...]

repeat^^ for all r
"""

#compare list of all of r1 fouls per game per team to list for each team
#repeat for all refs

#if ref'n' is in column ref1/ref2/ref3, pull APf+HPf
#add to list for correct team
#perform foneway on list of teams (teams are list of fc games)
#752 752

import pandas as pd
import numpy as np
from scipy.stats import f_oneway

gamedata_file = 'gamedata24-2-edit3.csv'
#gamedata_file='gamedata24fla-2-edit.csv'
ref1 = 'Ref1'
ref2 = 'Ref2'
ref3 = 'Ref3'
hfouls = 'HPf'
afouls = 'APf'
hteam = 'HomeTeam'
ateam = 'AwayTeam'

ref_list = [[] for _ in range(752)]
for i in range(752):
    ref_list[i] = [[] for _ in range(13)]

teams = [
    'Austin Peay', 'Eastern Ky.', 'Jacksonville St.', 'Kennesaw St.',
    'Lipscomb', 'Central Ark.', 'North Ala.', 'North Florida',
    'Bellarmine', 'Jacksonville', 'Queens (NC)', 'Stetson', 'FGCU'
]

#teams=['Florida', 'Florida A&M', 'Florida St.','Bethune-Cookman', 'UCF', 'North Florida', 'USF', 'FIU', 'Jacksonville', 'FAU', 'FGCU', 'Stetson', 'Miami']

teams_id=[0,1,2,3,4,5,6,7,8,9,10,11,12]

df = pd.read_csv(gamedata_file)

refcount = 1
while refcount < 753: #one more than ref count ie.342->343
    i = 0
    while i < len(df):
        refc1 = df.loc[i, ref1]
        refc2 = df.loc[i, ref2]
        refc3 = df.loc[i, ref3]
        if refc1 == refcount or refc2 == refcount or refc3 == refcount:
            hometeam = df.loc[i, hteam]
            awayteam = df.loc[i, ateam]

            homefouls = df.loc[i, hfouls]
            awayfouls = df.loc[i, afouls]

            if hometeam in teams:
                hteamposition = teams.index(hometeam)
                teamidhome = teams_id[hteamposition]
                ref_list[refcount - 1][teamidhome].append(homefouls)

            if awayteam in teams:
                ateamposition = teams.index(awayteam)
                teamidaway = teams_id[ateamposition]
                ref_list[refcount - 1][teamidaway].append(awayfouls)

        i += 1
    refcount += 1

# Print the fouls data for each ref
for j in range(752):
    for i in range(13):
        print(f"Ref {j + 1}, Team {teams[i]}: {ref_list[j][i]}")

j = 0
while j < 752:
    lists_to_compare = [ref_list[j][i] for i in range(13) if len(ref_list[j][i]) > 0]

    # Check if there are at least two lists to compare
    if len(lists_to_compare) >= 2:
        result = f_oneway(*lists_to_compare)
        print(f"Result Ref {j + 1}: {result}")
    else:
        print(f"Not enough data to compare for Ref {j + 1}")

    j += 1

