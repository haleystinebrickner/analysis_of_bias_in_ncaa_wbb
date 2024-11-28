import pandas as pd
import numpy as np
from scipy.stats import f_oneway

ref_foul = 'reffoulcount.csv'
ref_foul_team = 'reffoulgamecount2.csv'
ref = 'Ref'
fouls = 'TotFouls'
games = 'GameCount'
team = 'Team'

teams = [
    'Austin Peay', 'Eastern Ky.', 'Jacksonville St.', 'Kennesaw St.',
    'Lipscomb', 'Central Ark.', 'North Ala.', 'North Florida',
    'Bellarmine', 'Jacksonville', 'Queens (NC)', 'Stetson', 'FGCU'
]

team_data = {team: [] for team in teams}
team_data2 = {team: [] for team in teams}


df = pd.read_csv(ref_foul_team)

#statisitically significant results between each refs teams 
#but only 0/1 value for each team/ref combo 
#should this be a list of all of refs teams, compared to each other refs teams?

ref_count = 1
while ref_count < 343:
    i = 0
    while i < len(df):
        ref_num = df.loc[i, ref]
        if ref_num == ref_count:
            ref_foul = df.loc[i, fouls]
            game_count = df.loc[i, games]
            if game_count != 0:
                reffoul_pgame = ref_foul / game_count
                team_name = df.loc[i, team]
                team_data[team_name].append(reffoul_pgame)
        i += 1
    ref_count += 1

ftst = {}
ref_count = 1


while ref_count < 343:
    team_values = []

    for team in teams:
        if len(team_data[team]) >= ref_count:
            team_values.append(team_data[team][ref_count - 1])
    
    # Filter out zero-dimensional arrays (scalars)
    team_values = [arr for arr in team_values if arr.ndim > 0]

    if len(team_values) >= 1:
        ftst[ref_count] = f_oneway(*team_values)

    ref_count += 1

print("Before print")
print(ftst[1])

for ref_count, value in ftst.items():
    print(f"Referee {ref_count}: {value}")


