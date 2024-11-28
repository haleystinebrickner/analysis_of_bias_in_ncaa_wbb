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

gamedata_file = 'gamedataASUN5sznEDIT.csv'
#gamedata_file= 'gamedataFLORIDA5sznEDIT.csv'

home_foul=[[] for _ in range(0, 753)]
away_foul=[[] for _ in range(0, 753)]

home_foul_filt=[[] for _ in range(0, 753)]
away_foul_filt=[[] for _ in range(0, 753)]


h_tot_lst=[]
a_tot_lst=[]

ref_add=[[] for _ in range(0, 753)]
ref_gamecount=[[] for _ in range(0, 753)]

coaches_dict = {
    "Austin Peay": ["", "", "", "F/B", "F/B"],
    "Eastern Ky.": ["", "", "", "M/W", "M/W"],
    "Jacksonville St.": ["", "", "M/W", "M/W", "M/W"],
    "Kennesaw St.": ["F/W", "F/W", "F/W", "F/B", "F/B"],
    "Lipscomb": ["M/W", "F/B", "F/B", "F/B", "F/B"],
    "Central Ark.": ["", "", "F/W", "F/W", "F/W"],
    "North Ala.": ["F/W", "F/W", "F/W", "F/W", "F/W"],
    "North Florida": ["M/B", "M/B", "M/B", "M/B", "M/B"],
    "Bellarmine": ["F/W", "F/W", "F/W", "F/W", "F/W"],
    "Jacksonville": ["M/B", "M/B", "M/B", "M/B", "M/B"],
    "Queens (NC)": ["", "", "", "", "F/B"],
    "Stetson": ["F/W", "F/W", "F/W", "F/W", "F/W"],
    "FGCU": ["M/W", "M/W", "M/W", "M/W", "M/W"],
    "NJIT": ["M/W", "M/W", "", "", ""],
    "Miami": ["F/W", "F/W", "F/W", "F/W", "F/W"],
    "Florida St.": ["F/W", "F/W", "F/W", "F/W", "F/W"],
    "Florida": ["M/W", "M/W", "M/W", "F/W", "F/W"],
    "UCF": ["F/W", "F/W", "F/W", "F/W", "F/B"],
    "USF": ["M/O", "M/O", "M/O", "M/O", "M/O"],
    "Florida A&M": ["M/B", "M/B", "F/B", "F/B", "F/B"],
    "FIU": ["F/B", "F/B", "F/B", "F/B", "F/B"],
    "FAU": ["F/B", "F/B", "F/B", "F/B", "F/B"],
    "Bethune-Cookman": ["F/B", "F/B", "F/B", "F/B", "F/B"]
}



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


        pre_split= df.loc[i,year].split("-")
        
        #print(pre_split)
        pre_split= ''.join(pre_split)

        if pre_split.startswith('20'):
            ##print(pre_split)
            
            pre_split= pre_split[2:] 
            
            split_1= [pre_split[i:i+2] for i in range(0, len(pre_split), 2)]
        else:
        
            split_1 = pre_split
            split_1 = pre_split.split('/')

        #print(split_1) 
        #print(split_1[0], type(split_1[0])) 
        #print(split_1[1], type(split_1[1])) 
        #print(split_1[2], type(split_1[2])) 
        
        #print("YEAR 18/19")
            away=df.loc[i, away_team]
            home= df.loc[i, home_team]
            #print(away)
            #print(home)

            away_fc=df.loc[i, away_fouls]
            home_fc= df.loc[i, home_fouls]
            #print(away_fc)
            #print(home_fc)

            home_foul[j].append(home_fc)
            away_foul[j].append(away_fc)
            h_tot_lst.append(home_fc)
            a_tot_lst.append(away_fc)
            gamecount+=1
        

        
    

        if ((split_1[2]== "18") or ((split_1[2]== "19") and (int(split_1[0]) <=4))):
            #print("YEAR 18/19")
            away=df.loc[i, away_team]
            home= df.loc[i, home_team]
            #print(away)
            #print(home)

            away_fc=df.loc[i, away_fouls]
            home_fc= df.loc[i, home_fouls]
            #print(away_fc)
            #print(home_fc)

            home_foul[j].append(home_fc)
            away_foul[j].append(away_fc)
            h_tot_lst.append(home_fc)
            a_tot_lst.append(away_fc)
            gamecount+=1

        
        elif (((split_1[2]== "19") and (int(split_1[0]) >=10)) or ((split_1[2]=="20") and (int(split_1[0])<=4))):
                #print("YEAR 19/20")
                away=df.loc[i, away_team]
                home= df.loc[i, home_team]
                #print(away)
                #print(home)

                away_fc=df.loc[i, away_fouls]
                home_fc= df.loc[i, home_fouls]
                #print(away_fc)
                #print(home_fc)

                home_foul[j].append(home_fc)
                away_foul[j].append(away_fc)
                h_tot_lst.append(home_fc)
                a_tot_lst.append(away_fc)
                gamecount+=1


            
        elif (((split_1[2]== "20") and (int(split_1[0]) >=10)) or ((split_1[2]=="21") and (int(split_1[0])<=4))):
                #print("YEAR 20/21")
                away=df.loc[i, away_team]
                home= df.loc[i, home_team]
                #print(away)
                #print(home)

                away_fc=df.loc[i, away_fouls]
                home_fc= df.loc[i, home_fouls]
                #print(away_fc)
                #print(home_fc)

                home_foul[j].append(home_fc)
                away_foul[j].append(away_fc)
                h_tot_lst.append(home_fc)
                a_tot_lst.append(away_fc)
                gamecount+=1


            
        elif (((split_1[2]== "21") and (int(split_1[0]) >=10)) or ((split_1[2]=="22") and (int(split_1[0])<=4))):
                #print("YEAR 21/22")
                away=df.loc[i, away_team]
                home= df.loc[i, home_team]
                #print(away)
                #print(home)

                away_fc=df.loc[i, away_fouls]
                home_fc= df.loc[i, home_fouls]
                #print(away_fc)
                #print(home_fc)

                home_foul[j].append(home_fc)
                away_foul[j].append(away_fc)
                h_tot_lst.append(home_fc)
                a_tot_lst.append(away_fc)
                gamecount+=1


            
        elif (((split_1[2]== "22") and (int(split_1[0]) >=10)) or ((split_1[2]=="23") and (int(split_1[0])<=4))):
                #print("YEAR 22/23")
                away=df.loc[i, away_team]
                home= df.loc[i, home_team]
                #print(away)
                #print(home)

                away_fc=df.loc[i, away_fouls]
                home_fc= df.loc[i, home_fouls]
                #print(away_fc)
                #print(home_fc)

                home_foul[j].append(home_fc)
                away_foul[j].append(away_fc)
                h_tot_lst.append(home_fc)
                a_tot_lst.append(away_fc)
                gamecount+=1


        i+=1
    j+=1     

 

h_tot_lst_filter = [x for x in h_tot_lst if x != 0]
a_tot_lst_filter = [x for x in a_tot_lst if x != 0]

print(h_tot_lst_filter)
print(a_tot_lst_filter)

#print(tot_lst_filter)
#print(tot_gamefouls/tot_gamecount)

i=0
for i in range(0,752):
    #print(ref_lst[i])
    home_foul_filt[i]= [x for x in home_foul[i] if x != 0]
    away_foul_filt[i]= [x for x in away_foul[i] if x != 0]

    if len(home_foul_filt[i])>1:
        print(home_foul_filt[i])
        t_result= stats.ttest_ind(a=home_foul_filt[i], b=h_tot_lst_filter, equal_var=False)
        #alex_result= alexandergovern(ref_lst_filt[i], tot_lst_filter)
        print("REF ", i, ":Home")
        #print(t_result)
        #print(alex_result)
        #print(ref_add[i]/ref_gamecount[i])
    
    if len(away_foul_filt[i])>1:
        print(away_foul_filt[i])
        t_result= stats.ttest_ind(a=away_foul_filt[i], b=a_tot_lst_filter, equal_var=False)
        #alex_result= alexandergovern(ref_lst_filt[i], tot_lst_filter)
        print("REF ", i, ":Away")
        #print(t_result)
        #print(alex_result)
        #print(ref_add[i]/ref_gamecount[i])

    i+=1

        


         
