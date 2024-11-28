import csv
import pandas as pd
from collections import defaultdict

gamedata_file= 'gamedataFLORIDA5sznEDIT.csv'
ref1 = 'Ref1'
ref2 = 'Ref2'
ref3 = 'Ref3'
hfouls = 'HPf'
afouls = 'APf'
hteam = 'HomeTeam'
ateam = 'AwayTeam'

#team_list = ['Austin Peay', 'Eastern Ky.', 'Jacksonville St.', 'Kennesaw St.', 'Lipscomb', 'Central Ark.', 'North Ala.', 'North Florida', 'Bellarmine', 'Jacksonville', 'Queens (NC)', 'Stetson', 'FGCU']
team_list=['Florida', 'Florida A&M', 'Florida St.','Bethune-Cookman', 'UCF', 'North Florida', 'USF', 'FIU', 'Jacksonville', 'FAU', 'FGCU', 'Stetson', 'Miami']

# Create dictionaries to store statistics
tot_foulcount = defaultdict(lambda: defaultdict(int))
h_foulcount = defaultdict(lambda: defaultdict(int))
a_foulcount = defaultdict(lambda: defaultdict(int))
gamecount = defaultdict(lambda: defaultdict(int))
print("test1")
df = pd.read_csv(gamedata_file)
print("test2")

# Check for missing values in the hfouls and afouls columns and replace with 0
df[hfouls] = pd.to_numeric(df[hfouls], errors='coerce')
df[afouls] = pd.to_numeric(df[afouls], errors='coerce')
print("test3a")
# Handle missing values by replacing NaN with 0
df[hfouls].fillna(0, inplace=True)
df[afouls].fillna(0, inplace=True)
print("test3")
for team in team_list:
    for refcount in range(1, 745):
        for i in range(len(df)):
            ref_c1 = df.loc[i, ref1]
            ref_c2 = df.loc[i, ref2]
            ref_c3 = df.loc[i, ref3]
            
            if team == df.loc[i, hteam]:
                if ref_c1 == refcount or ref_c2 == refcount or ref_c3 == refcount:
                    tot_foulcount[team][refcount] += df.loc[i, hfouls] + df.loc[i, afouls]
                    h_foulcount[team][refcount] += df.loc[i, hfouls]
                    gamecount[team][refcount] += 1

            elif team == df.loc[i, ateam]:
                if ref_c1 == refcount or ref_c2 == refcount or ref_c3 == refcount:
                    tot_foulcount[team][refcount] += df.loc[i, hfouls] + df.loc[i, afouls]
                    a_foulcount[team][refcount] += df.loc[i, afouls]
                    gamecount[team][refcount] += 1

# Print the results
print("test4")                    
for team in team_list:
    for refcount in range(1, 745):
        print(team, refcount, gamecount[team][refcount], tot_foulcount[team][refcount], h_foulcount[team][refcount], a_foulcount[team][refcount])
print("test5")
with open('reffoulgamecountFLORIDAall.csv', mode='w', newline='') as csv_file:
        writer= csv.writer(csv_file)
        writer.writerow(["Team","Ref","GameCount","TotFouls", "HFouls", "AFouls"])
        for team in team_list:
            for refcount in range(1, 745):
                row_data = [team, refcount, gamecount[team][refcount], tot_foulcount[team][refcount], h_foulcount[team][refcount], a_foulcount[team][refcount]]
                writer.writerow(row_data)