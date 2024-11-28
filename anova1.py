import pandas as pd
import numpy as np
from scipy.stats import f_oneway
from statistics import fmean, variance

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

df = pd.read_csv(ref_foul_team)

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
"""
ftst = {}
ref_count = 1
while ref_count < 343:
    team_values = [team_data[team][ref_count - 1] for team in teams if team_data[team]]
    
    if team_values:
        # Check if any team has an empty array (zero-dimensional array)
        zero_dimensional = any(np.size(arr) == 0 for arr in team_values)

        if not zero_dimensional:
            team_data_filtered = [arr for arr in team_values if arr is not None]
            ftst[ref_count] = f_oneway(*team_data_filtered)

    ref_count += 1

for ref_count, value in ftst.items():
    print(f"Referee {ref_count}: {value}")
"""

ftst = {}
ref_count = 1
while ref_count < 343:
    team_values = [team_data[team][ref_count - 1] for team in teams if team_data[team]]
    
    if team_values:
        mean = fmean(team_values)
        var = variance(team_values)
        ftst[ref_count] = var / mean

    ref_count += 1

for ref_count, value in ftst.items():
    print(f"Referee {ref_count}: {value}")