#Home vs Away Fouls 

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

home_foul_89=[]
away_foul_89=[]

home_foul_90=[]
away_foul_90=[]

home_foul_01=[]
away_foul_01=[]

home_foul_12=[]
away_foul_12=[]

home_foul_23=[]
away_foul_23=[]


#team_list = ['Austin Peay', 'Eastern Ky.', 'Jacksonville St.', 'Kennesaw St.', 'Lipscomb', 'Central Ark.', 'North Ala.', 'North Florida', 'Bellarmine', 'Jacksonville', 'Queens (NC)', 'Stetson', 'FGCU']
team_list=['Florida', 'Florida A&M', 'Florida St.','Bethune-Cookman', 'UCF', 'North Florida', 'USF', 'FIU', 'Jacksonville', 'FAU', 'FGCU', 'Stetson', 'Miami']

df = pd.read_csv(gamedata_file)

# Check for missing values in the hfouls and afouls columns and replace with 0

df_dict = df.to_dict(orient='records')

# Convert string columns to numeric
def to_numeric(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None  # or any other fallback value

for row in df_dict:
    row[away_fouls] = to_numeric(row.get(away_fouls))
    row[home_fouls] = to_numeric(row.get(home_fouls))

# Handle missing values by replacing None with 0
for row in df_dict:
    if row[away_fouls] is None:
        row[away_fouls] = 0
    if row[home_fouls] is None:
        row[home_fouls] = 0

# Convert back to DataFrame if needed
df = pd.DataFrame(df_dict)


i=0
gamecount=0

for team in team_list: 
    print(team)

    i=0
    while i<len(df):
        pre_split= df.loc[i,year].split("-")
        
        #print(pre_split)
        pre_split= ''.join(pre_split)

        if pre_split.startswith('20'):
            #print(pre_split)
            
            pre_split= pre_split[2:] 
            
            split_1= [pre_split[i:i+2] for i in range(0, len(pre_split), 2)]
        else:
        
            split_1 = pre_split
            split_1 = pre_split.split('/')

        #print(split_1) 
        #print(split_1[0], type(split_1[0])) 
        #print(split_1[1], type(split_1[1])) 
        #print(split_1[2], type(split_1[2])) 
        
        

        
    

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

            if team==home:
                home_foul_89.append(home_fc)
            elif team==away:
                away_foul_89.append(away_fc)
            
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

                if team==home:
                    home_foul_90.append(home_fc)
                elif team==away:
                    away_foul_90.append(away_fc)
            
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

                if team==home:
                    home_foul_01.append(home_fc)
                elif team==away:
                    away_foul_01.append(away_fc)
            
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

                if team==home:
                    home_foul_12.append(home_fc)
                elif team==away:
                    away_foul_12.append(away_fc)
            
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

                if team==home:
                    home_foul_23.append(home_fc)
                elif team==away:
                    away_foul_23.append(away_fc)
            
                gamecount+=1


        i+=1    

 
    print("2018-19")
    #print(home_foul_89)
    #print(away_foul_89)
    result1= f_oneway(home_foul_89, away_foul_89)
    #result2= alexandergovern(home_foul_89, away_foul_89)
    print(result1)
    #print(result2)
    #describe2= stats.describe(result2)
    #print(describe2)

    print("2019-20")
    #print(home_foul_90)
    #print(away_foul_90)
    result3= f_oneway(home_foul_90, away_foul_90)
    #result4= alexandergovern(home_foul_90, away_foul_90)
    print(result3)
    #print(result4)
    #describe4= stats.describe(result4)
    #print(describe4)

    print("2020-21")
    #print(home_foul_01)
    #print(away_foul_01)
    result5= f_oneway(home_foul_01, away_foul_01)
    #result6= alexandergovern(home_foul_01, away_foul_01)
    print(result5)
    #print(result6)
    #describe6= stats.describe(result6)
    #print(describe6)

    print("2021-22")
    #print(home_foul_12)
    #print(away_foul_12)
    result7= f_oneway(home_foul_12, away_foul_12)
    #result8= alexandergovern(home_foul_12, away_foul_12)
    print(result7)
    #print(result8)
    #describe8= stats.describe(result8)
    #print(describe8)

    print("2022-23")
    #print(home_foul_23)
    #print(away_foul_23)
    result9= f_oneway(home_foul_23, away_foul_23)
    #result10= alexandergovern(home_foul_23, away_foul_23)
    print(result9)
    #print(result10)
    #describe10= stats.describe(result10)
    #print(describe10)
