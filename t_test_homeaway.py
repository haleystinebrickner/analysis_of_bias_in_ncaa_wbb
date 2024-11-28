#BvW Coaches Total Fouls 

#per year

#2018-2019

import pandas as pd
import numpy as np
from scipy.stats import f_oneway
from scipy.stats import alexandergovern
from scipy import stats


year="Gamedate"
away_team= "AwayTeam"
home_team= "HomeTeam"
away_fouls= "APf"
home_fouls="HPf"

#gamedata_file = 'gamedataASUN5sznEDIT.csv'
gamedata_file= 'gamedataFLORIDA5sznEDIT.csv'

home_foul=[[] for _ in range(0, 753)]
away_foul=[[] for _ in range(0, 753)]

home_foul_filt=[[] for _ in range(0, 753)]
away_foul_filt=[[] for _ in range(0, 753)]


h_tot_lst=[]
a_tot_lst=[]

ref_add=[[] for _ in range(0, 753)]
ref_gamecount=[[] for _ in range(0, 753)]




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

j=0
while j<753:
    print("REF: ", j)
    i=0
    gamecount=0
    while i<len(df):

        if (((df.loc[i, "Ref1"])==j) or ((df.loc[i, "Ref2"])==j) or ((df.loc[i, "Ref3"])==j)): 

            away=df.loc[i, away_team]
            home= df.loc[i, home_team]

            away_fc=df.loc[i, away_fouls]
            home_fc= df.loc[i, home_fouls]

            home_foul[j].append(home_fc)
            away_foul[j].append(away_fc)
            h_tot_lst.append(home_fc)
            a_tot_lst.append(away_fc)
            gamecount+=1
        
           
        i+=1
    j+=1     

 

h_tot_lst_filter = [x for x in h_tot_lst if x != 0]
a_tot_lst_filter = [x for x in a_tot_lst if x != 0]

#print(h_tot_lst_filter)
#print(a_tot_lst_filter)

#print(tot_lst_filter)
#print(tot_gamefouls/tot_gamecount)

i=0
for i in range(0,753):
    #print(ref_lst[i])
    home_foul_filt[i]= [x for x in home_foul[i] if x != 0]
    away_foul_filt[i]= [x for x in away_foul[i] if x != 0]

    if len(home_foul_filt[i])>1:
        #print(home_foul_filt[i])
        t_result= stats.ttest_ind(a=home_foul_filt[i], b=h_tot_lst_filter, equal_var=False)
        #alex_result= alexandergovern(ref_lst_filt[i], tot_lst_filter)
        print("REF ", i, ":Home")
        print(t_result)
        #print(alex_result)
        #print(ref_add[i]/ref_gamecount[i])
    
    if len(away_foul_filt[i])>1:
        #print(away_foul_filt[i])
        t_result= stats.ttest_ind(a=away_foul_filt[i], b=a_tot_lst_filter, equal_var=False)
        #alex_result= alexandergovern(ref_lst_filt[i], tot_lst_filter)
        print("REF ", i, ":Away")
        print(t_result)
        #print(alex_result)
        #print(ref_add[i]/ref_gamecount[i])

    i+=1

        


         
