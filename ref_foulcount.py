import csv
import pandas as pd

# read line of gamedata file 
#for all refs (i-342)
# read column of that line/row if that ref is in ref1,2,3 column *
# find tot fouls for that row, add to tot fouls 
# increment gamecount +1
#read next line of ref 1, 2,3 
# return to *
#increment ref count

gamedata_file= 'gamedataFLORIDA5sznEDIT.csv'
ref1= 'Ref1'
ref2= 'Ref2'
ref3= 'Ref3'
hfouls='HPf'
afouls='APf'

tot_foulcount = [0] * 745
h_foulcount = [0] * 745
a_foulcount = [0] * 745
gamecount = [0] * 745

df = pd.read_csv(gamedata_file)

# Check for missing values in the hfouls and afouls columns and replace with 0
df[hfouls] = pd.to_numeric(df[hfouls], errors='coerce')
df[afouls] = pd.to_numeric(df[afouls], errors='coerce')

# Handle missing values by replacing NaN with 0
df[hfouls].fillna(0, inplace=True)
df[afouls].fillna(0, inplace=True)

tot_foulcount = [0] * 745
h_foulcount = [0] * 745
a_foulcount = [0] * 745
gamecount = [0] * 745

refcount = 1
while refcount <= 745:
    i = 0
    while i < len(df):
        ref_c1 = df.loc[i, ref1]
        ref_c2 = df.loc[i, ref2]
        ref_c3 = df.loc[i, ref3]
        if ref_c1 == refcount:
            tot_foulcount[refcount] += df.loc[i, hfouls] + df.loc[i, afouls]
            h_foulcount[refcount] += df.loc[i, hfouls]
            a_foulcount[refcount] += df.loc[i, afouls]
            gamecount[refcount] += 1
        elif ref_c2 == refcount:
            tot_foulcount[refcount] += df.loc[i, hfouls] + df.loc[i, afouls]
            h_foulcount[refcount] += df.loc[i, hfouls]
            a_foulcount[refcount] += df.loc[i, afouls]
            gamecount[refcount] += 1
        elif ref_c3 == refcount:
            tot_foulcount[refcount] += df.loc[i, hfouls] + df.loc[i, afouls]
            h_foulcount[refcount] += df.loc[i, hfouls]
            a_foulcount[refcount] += df.loc[i, afouls]
            gamecount[refcount] += 1
        i += 1
    refcount += 1

with open('reffoulcountFLORIDAall.csv', mode='w', newline='') as csv_file:
        writer= csv.writer(csv_file)
        writer.writerow(["Ref","GameCount","TotFouls", "HFouls", "AFouls"])
        for ref, game_count, tot_fouls, h_fouls, a_fouls in zip(range(745), gamecount, tot_foulcount, h_foulcount, a_foulcount):
            writer.writerow([ref, game_count, tot_fouls, h_fouls, a_fouls])
      


