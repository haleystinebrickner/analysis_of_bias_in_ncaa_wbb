#perform t tests to determine ref with bias foul count call

import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import f_oneway
from scipy.stats import alexandergovern


ref = 'Ref'
fouls = 'TotFouls'
away_fouls= "APf"
home_fouls="HPf"

tot_fouls= 'TotFouls'

#gamedata_file = 'gamedataASUN5sznEDIT.csv'
#reffoulgamecount_file= 'reffoulgamecountASUNall.csv'

gamedata_file= 'gamedataFLORIDA5sznEDIT.csv'
reffoulgamecount_file= 'reffoulgamecountFLORIDAall.csv'

ref_lst=[[] for _ in range(0, 752)]
ref_lst_filt=[[] for _ in range(0, 752)]
tot_lst=[]

ref_add=[[] for _ in range(0, 752)]
ref_gamecount=[[] for _ in range(0, 752)]

tot_gamecount=0
tot_gamefouls=0

df = pd.read_csv(gamedata_file)

for i in range(len(df)):
    # Convert home_fouls to numeric and handle errors
    try:
        df.loc[i, "Ref1"] = int(df.loc[i, "Ref1"])
    except ValueError:
        df.loc[i, "Ref1"] = 0

    try:
        df.loc[i, "Ref2"] = int(df.loc[i, "Ref2"])
    except ValueError:
        df.loc[i, "Ref2"] = 0

    try:
        df.loc[i, "Ref3"] = int(df.loc[i, "Ref3"])
    except ValueError:
        df.loc[i, "Ref3"] = 0
        
    
    

i=0
while i<len(df):
    print(i)

    ref_id1= int(df.loc[i, "Ref1"])
    ref_id2= int(df.loc[i, "Ref2"])
    ref_id3= int(df.loc[i, "Ref3"])

    game_foul1= int(df.loc[i, away_fouls])
    game_foul2= int(df.loc[i, home_fouls])
    game_foul= game_foul1 + game_foul2

    ref_lst[ref_id1].append(game_foul)
    ref_lst[ref_id2].append(game_foul)
    ref_lst[ref_id3].append(game_foul)
    tot_lst.append(game_foul)

    """
    ref_add[ref_id1]+= game_foul
    ref_add[ref_id1]+= game_foul
    ref_add[ref_id1]+= game_foul

    
    ref_gamecount[ref_id1]+=1
    ref_gamecount[ref_id2]+=1
    ref_gamecount[ref_id2]+=1

    tot_gamecount+=1
    tot_gamefouls+= game_foul
    """

    
    i+=1

print(tot_lst)

tot_lst_filter = [x for x in tot_lst if x != 0]

print(tot_lst_filter)
#print(tot_gamefouls/tot_gamecount)

i=1
for i in range(1,752):
    #print(ref_lst[i])
    ref_lst_filt[i]= [x for x in ref_lst[i] if x != 0]
    if len(ref_lst_filt[i])>1:
        print(ref_lst_filt[i])
        t_result= stats.ttest_ind(a=ref_lst_filt[i], b=tot_lst_filter, equal_var=False)
        #alex_result= alexandergovern(ref_lst_filt[i], tot_lst_filter)
        print("REF ", i)
        print(t_result)
        #print(alex_result)
        #print(ref_add[i]/ref_gamecount[i])

    i+=1
