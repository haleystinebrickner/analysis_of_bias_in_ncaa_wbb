import csv
import pandas as pd

#for each team, for each ref, each game
#for team, if ref is in that game add to fouls
#increment game count

gamedata_file= 'gamedataASUN5sznEDIT.csv'
ref1= 'Ref1'
ref2= 'Ref2'
ref3= 'Ref3'
hfouls='HPf'
afouls='APf'
hteam='HomeTeam'
ateam='AwayTeam'

team_list=['Austin Peay', 'Eastern Ky.', 'Jacksonville St.','Kennesaw St.','Lipscomb','Central Ark.', 'North Ala.','North Florida', 'Bellarmine', 'Jacksonville','Queens (NC)','Stetson', 'FGCU']
"""
tot_foulcount = [0] * 752
h_foulcount = [0] * 752
a_foulcount = [0] * 752
gamecount = [0] * 752
"""
tot_foulcount = [[]*13]*752
h_foulcount = [[]*13]*752
a_foulcount = [[]*13]*752
gamecount = [[]*13]*752

team_count = len(team_list)
ref_count = 752
tot_foulcount = [[0] * ref_count for _ in range(team_count)]
h_foulcount = [[0] * ref_count for _ in range(team_count)]
a_foulcount = [[0] * ref_count for _ in range(team_count)]
gamecount = [[0] * ref_count for _ in range(team_count)]


df = pd.read_csv(gamedata_file)

# Check for missing values in the hfouls and afouls columns and replace with 0
df[hfouls] = pd.to_numeric(df[hfouls], errors='coerce')
df[afouls] = pd.to_numeric(df[afouls], errors='coerce')

# Handle missing values by replacing NaN with 0
df[hfouls].fillna(0, inplace=True)
df[afouls].fillna(0, inplace=True)
"""
tot_foulcount = [0] * 752
h_foulcount = [0] * 752
a_foulcount = [0] * 752
gamecount = [0] * 752
"""

team_count=0
for team in team_list:
    print(team)
    refcount=1
    tot_foulcount[team_count] = [0] * 752
    h_foulcount[team_count] = [0] * 752
    a_foulcount[team_count] = [0] * 752
    gamecount[team_count] = [0] * 752
    while refcount <= 752:
        i = 0
        while i < len(df):
            ref_c1 = df.loc[i, ref1]
            ref_c2 = df.loc[i, ref2]
            ref_c3 = df.loc[i, ref3]
            if team== df.loc[i,hteam]:
                if ref_c1 == refcount:
                    tot_foulcount[team_count][refcount] += df.loc[i, hfouls] + df.loc[i, afouls]
                    h_foulcount[team_count][refcount] += df.loc[i, hfouls]
                    gamecount[team_count][refcount] += 1
                elif ref_c2 == refcount:
                    tot_foulcount[team_count][refcount] += df.loc[i, hfouls] + df.loc[i, afouls]
                    h_foulcount[team_count][refcount] += df.loc[i, hfouls]
                    gamecount[team_count][refcount] += 1
                elif ref_c3 == refcount:
                    tot_foulcount[team_count][refcount] += df.loc[i, hfouls] + df.loc[i, afouls]
                    h_foulcount[team_count][refcount] += df.loc[i, hfouls]
                    gamecount[team_count][refcount] += 1
            elif team==df.loc[i, ateam]:
                    #same as above code
                if ref_c1 == refcount:
                    tot_foulcount[team_count][refcount] += df.loc[i, hfouls] + df.loc[i, afouls]
                    a_foulcount[team_count][refcount] += df.loc[i, afouls]
                    gamecount[team_count][refcount] += 1
                elif ref_c2 == refcount:
                    tot_foulcount[team_count][refcount] += df.loc[i, hfouls] + df.loc[i, afouls]
                    a_foulcount[team_count][refcount] += df.loc[i, afouls]
                    gamecount[team_count][refcount] += 1
                elif ref_c3 == refcount:
                    tot_foulcount[team_count][refcount] += df.loc[i, hfouls] + df.loc[i, afouls]
                    a_foulcount[team_count][refcount] += df.loc[i, afouls]
                    gamecount[team_count][refcount] += 1
            i += 1
        refcount += 1
        team_count+=1

team_count=-1
for team in team_list:
    i=0
    team_count+=1
    while i<=752:
        print(team, i, tot_foulcount[team_count][i], h_foulcount[team_count][i], a_foulcount[team_count][i])
        i+=1
    
   # for ref, game_count, tot_fouls, h_fouls, a_fouls in zip(range(752), gamecount, tot_foulcount, h_foulcount, a_foulcount):
      #  print([team,ref, game_count, tot_fouls, h_fouls, a_fouls])
"""
with open('reffoulgamecount2.csv', mode='w', newline='') as csv_file:
        writer= csv.writer(csv_file)
        writer.writerow(["Team","Ref","GameCount","TotFouls", "HFouls", "AFouls"])
        for team in team_list:
            for ref, game_count, tot_fouls, h_fouls, a_fouls in zip(range(752), gamecount, tot_foulcount, h_foulcount, a_foulcount):
                writer.writerow([team,ref, game_count, tot_fouls, h_fouls, a_fouls])

#delete rows with no data

completed_file='reffoulgamecount2.csv'
game_count='GameCount'

df= pd.read_csv(completed_file)

# Delete rows with a GameCount of 0
df = df[df[game_count] > 0]

# Write the updated DataFrame back to the CSV file
df.to_csv(completed_file, index=False)

while i<len(df):
    if df.loc[i,game_count]==0:
        df = df.drop(df.loc(i))
    i+=1
df.to_csv(csv_file, index=False)
"""