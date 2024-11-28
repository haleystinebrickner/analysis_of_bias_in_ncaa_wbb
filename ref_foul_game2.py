import csv
import pandas as pd
from collections import defaultdict

gamedata_file = 'gamedataFLORIDA5sznEDIT.csv'
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
print("test")
# Read the CSV file into a DataFrame
df = pd.read_csv(gamedata_file)
print("test")
# Convert fouls columns to numeric, replacing NaN with 0
#df[hfouls] = pd.to_numeric(df[hfouls], errors='coerce').fillna(0)
#df[afouls] = pd.to_numeric(df[afouls], errors='coerce').fillna(0)
print("test")
# Iterate over DataFrame rows and calculate statistics
for index, row in df.iterrows():
    ref_counts = [row[ref1], row[ref2], row[ref3]]
    for team in [row[hteam], row[ateam]]:
        for ref_count in ref_counts:
            tot_foulcount[team][ref_count] += row[hfouls] + row[afouls]
            h_foulcount[team][ref_count] += row[hfouls]
            a_foulcount[team][ref_count] += row[afouls]
            gamecount[team][ref_count] += 1

# Write the results to a CSV file
with open('reffoulgamecountFLORIDAall.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Team", "Ref", "GameCount", "TotFouls", "HFouls", "AFouls"])
    for team in team_list:
        for ref_count in range(1, 745):
            row_data = [team, ref_count, gamecount[team][ref_count], tot_foulcount[team][ref_count], h_foulcount[team][ref_count], a_foulcount[team][ref_count]]
            writer.writerow(row_data)

print("Data written to CSV successfully.")
