#MvF Coaches Total Fouls 

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

m_coach_foul_89=[]
f_coach_foul_89=[]

m_coach_foul_90=[]
f_coach_foul_90=[]

m_coach_foul_01=[]
f_coach_foul_01=[]

m_coach_foul_12=[]
f_coach_foul_12=[]

m_coach_foul_23=[]
f_coach_foul_23=[]

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

i=0
gamecount=0
while i<len(df):
    pre_split= df.loc[i,year].split("-")
    
    print(pre_split)
    pre_split= ''.join(pre_split)

    if pre_split.startswith('20'):
        #print(pre_split)
        
        pre_split= pre_split[2:] 
        
        split_1= [pre_split[i:i+2] for i in range(0, len(pre_split), 2)]
    else:
       
        split_1 = pre_split
        split_1 = pre_split.split('/')

    print(split_1) 
    print(split_1[0], type(split_1[0])) 
    print(split_1[1], type(split_1[1])) 
    print(split_1[2], type(split_1[2])) 
    
    

    
   

    if ((split_1[2]== "18") or ((split_1[2]== "19") and (int(split_1[0]) <=4))):
        print("YEAR 18/19")
        away=df.loc[i, away_team]
        home= df.loc[i, home_team]
        print(away)
        print(home)

        away_fc=df.loc[i, away_fouls]
        home_fc= df.loc[i, home_fouls]
        print(away_fc)
        print(home_fc)

        
        away_split = coaches_dict.get(away, ["", "", "", "", ""])
        home_split = coaches_dict.get(home, ["", "", "", "", ""])
        
        #away_split= coaches_dict[away][0].split("/")
        #home_split= coaches_dict[home][0].split("/")

        away_cg= away_split[0]
        home_cg= home_split[0]

        away_cg= away_cg.split("/")
        home_cg= home_cg.split("/")

        print(away_cg)
        print(home_cg)
        

        if away_cg[0]== "M":
            m_coach_foul_89.append(away_fc)
            gamecount+=1
            print(away_fc)
        elif away_cg[0]=="F":
            f_coach_foul_89.append(away_fc)
            gamecount+=1
            print(away_fc)
        

        if home_cg[0]== "M":
            m_coach_foul_89.append(home_fc)
            gamecount+=1
            print(home_fc)
        elif home_cg[0]=="F":
            f_coach_foul_89.append(home_fc)
            gamecount+=1
            print(home_fc)
    
    elif (((split_1[2]== "19") and (int(split_1[0]) >=10)) or ((split_1[2]=="20") and (int(split_1[0])<=4))):
            print("YEAR 19/20")
            away=df.loc[i, away_team]
            home= df.loc[i, home_team]
            print(away)
            print(home)

            away_fc=df.loc[i, away_fouls]
            home_fc= df.loc[i, home_fouls]
            print(away_fc)
            print(home_fc)

            
            away_split = coaches_dict.get(away, ["", "", "", "", ""])
            home_split = coaches_dict.get(home, ["", "", "", "", ""])
            
            #away_split= coaches_dict[away][0].split("/")
            #home_split= coaches_dict[home][0].split("/")

            away_cg= away_split[1]
            home_cg= home_split[1]

            away_cg= away_cg.split("/")
            home_cg= home_cg.split("/")

            print(away_cg)
            print(home_cg)
            

            if away_cg[0]== "M":
                m_coach_foul_90.append(away_fc)
                gamecount+=1
                print(away_fc)
            elif away_cg[0]=="F":
                f_coach_foul_90.append(away_fc)
                gamecount+=1
                print(away_fc)
            

            if home_cg[0]== "M":
                m_coach_foul_90.append(home_fc)
                gamecount+=1
                print(home_fc)
            elif home_cg[0]=="F":
                f_coach_foul_90.append(home_fc)
                gamecount+=1
                print(home_fc)

        
    elif (((split_1[2]== "20") and (int(split_1[0]) >=10)) or ((split_1[2]=="21") and (int(split_1[0])<=4))):
            print("YEAR 20/21")
            away=df.loc[i, away_team]
            home= df.loc[i, home_team]
            print(away)
            print(home)

            away_fc=df.loc[i, away_fouls]
            home_fc= df.loc[i, home_fouls]
            print(away_fc)
            print(home_fc)

            
            away_split = coaches_dict.get(away, ["", "", "", "", ""])
            home_split = coaches_dict.get(home, ["", "", "", "", ""])
            
            #away_split= coaches_dict[away][0].split("/")
            #home_split= coaches_dict[home][0].split("/")

            away_cg= away_split[2]
            home_cg= home_split[2]

            away_cg= away_cg.split("/")
            home_cg= home_cg.split("/")

            print(away_cg)
            print(home_cg)
            

            if away_cg[0]== "M":
                m_coach_foul_01.append(away_fc)
                gamecount+=1
                print(away_fc)
            elif away_cg[0]=="F":
                f_coach_foul_01.append(away_fc)
                gamecount+=1
                print(away_fc)
            

            if home_cg[0]== "M":
                m_coach_foul_01.append(home_fc)
                gamecount+=1
                print(home_fc)
            elif home_cg[0]=="F":
                f_coach_foul_01.append(home_fc)
                gamecount+=1
                print(home_fc)

        
    elif (((split_1[2]== "21") and (int(split_1[0]) >=10)) or ((split_1[2]=="22") and (int(split_1[0])<=4))):
            print("YEAR 21/22")
            away=df.loc[i, away_team]
            home= df.loc[i, home_team]
            print(away)
            print(home)

            away_fc=df.loc[i, away_fouls]
            home_fc= df.loc[i, home_fouls]
            print(away_fc)
            print(home_fc)

            
            away_split = coaches_dict.get(away, ["", "", "", "", ""])
            home_split = coaches_dict.get(home, ["", "", "", "", ""])
            
            #away_split= coaches_dict[away][0].split("/")
            #home_split= coaches_dict[home][0].split("/")

            away_cg= away_split[3]
            home_cg= home_split[3]

            away_cg= away_cg.split("/")
            home_cg= home_cg.split("/")

            print(away_cg)
            print(home_cg)
            

            if away_cg[0]== "M":
                m_coach_foul_12.append(away_fc)
                gamecount+=1
                print(away_fc)
            elif away_cg[0]=="F":
                f_coach_foul_12.append(away_fc)
                gamecount+=1
                print(away_fc)
            

            if home_cg[0]== "M":
                m_coach_foul_12.append(home_fc)
                gamecount+=1
                print(home_fc)
            elif home_cg[0]=="F":
                f_coach_foul_12.append(home_fc)
                gamecount+=1
                print(home_fc)

        
    elif (((split_1[2]== "22") and (int(split_1[0]) >=10)) or ((split_1[2]=="23") and (int(split_1[0])<=4))):
            print("YEAR 22/23")
            away=df.loc[i, away_team]
            home= df.loc[i, home_team]
            print(away)
            print(home)

            away_fc=df.loc[i, away_fouls]
            home_fc= df.loc[i, home_fouls]
            print(away_fc)
            print(home_fc)

            
            away_split = coaches_dict.get(away, ["", "", "", "", ""])
            home_split = coaches_dict.get(home, ["", "", "", "", ""])
            
            #away_split= coaches_dict[away][0].split("/")
            #home_split= coaches_dict[home][0].split("/")

            away_cg= away_split[4]
            home_cg= home_split[4]

            away_cg= away_cg.split("/")
            home_cg= home_cg.split("/")

            print(away_cg)
            print(home_cg)
            

            if away_cg[0]== "M":
                m_coach_foul_23.append(away_fc)
                gamecount+=1
                print(away_fc)
            elif away_cg[0]=="F":
                f_coach_foul_23.append(away_fc)
                gamecount+=1
                print(away_fc)
            

            if home_cg[0]== "M":
                m_coach_foul_23.append(home_fc)
                gamecount+=1
                print(home_fc)
            elif home_cg[0]=="F":
                f_coach_foul_23.append(home_fc)
                gamecount+=1
                print(home_fc)

    i+=1    





print("2018-19")
print(m_coach_foul_89)
print(f_coach_foul_89)
result1= f_oneway(m_coach_foul_89, f_coach_foul_89)
result2= alexandergovern(m_coach_foul_89,f_coach_foul_89)
print(result1)
print(result2)
describe2= stats.describe(result2)
print(describe2)

print("2019-20")
print(m_coach_foul_90)
print(f_coach_foul_90)
result3= f_oneway(m_coach_foul_90, f_coach_foul_90)
result4= alexandergovern(m_coach_foul_90,f_coach_foul_90)
print(result3)
print(result4)
describe4= stats.describe(result4)
print(describe4)

print("2020-21")
print(m_coach_foul_01)
print(f_coach_foul_01)
result5= f_oneway(m_coach_foul_01, f_coach_foul_01)
result6= alexandergovern(m_coach_foul_01,f_coach_foul_01)
print(result5)
print(result6)
describe6= stats.describe(result6)
print(describe6)

print("2021-22")
print(m_coach_foul_12)
print(f_coach_foul_12)
result7= f_oneway(m_coach_foul_01, f_coach_foul_12)
result8= alexandergovern(m_coach_foul_01,f_coach_foul_12)
print(result7)
print(result8)
describe8= stats.describe(result8)
print(describe8)

print("2022-23")
print(m_coach_foul_23)
print(f_coach_foul_23)
result9= f_oneway(m_coach_foul_01, f_coach_foul_23)
result10= alexandergovern(m_coach_foul_01,f_coach_foul_23)
print(result9)
print(result10)
describe10= stats.describe(result10)
print(describe10)
"""

m_coach_foul_89_clean = [foul for foul in m_coach_foul_89 if not np.isnan(foul)]
f_coach_foul_89_clean = [foul for foul in f_coach_foul_89 if not np.isnan(foul)]

m_coach_foul_90_clean = [foul for foul in m_coach_foul_90 if not np.isnan(foul)]
f_coach_foul_90_clean = [foul for foul in f_coach_foul_90 if not np.isnan(foul)]

m_coach_foul_01_clean = [foul for foul in m_coach_foul_01 if not np.isnan(foul)]
f_coach_foul_01_clean = [foul for foul in f_coach_foul_01 if not np.isnan(foul)]

m_coach_foul_12_clean = [foul for foul in m_coach_foul_12 if not np.isnan(foul)]
f_coach_foul_12_clean = [foul for foul in f_coach_foul_12 if not np.isnan(foul)]

m_coach_foul_23_clean = [foul for foul in m_coach_foul_23 if not np.isnan(foul)]
f_coach_foul_23_clean = [foul for foul in f_coach_foul_23 if not np.isnan(foul)]

print("2018-19")
print(m_coach_foul_89_clean)
print(f_coach_foul_89_clean)
result1= f_oneway(m_coach_foul_89_clean, f_coach_foul_89_clean)
result2= alexandergovern(m_coach_foul_89_clean,f_coach_foul_89_clean)
print(result1)
print(result2)
describe2= stats.describe(result2)
print(describe2)

print("2019-20")
print(m_coach_foul_90_clean)
print(f_coach_foul_90_clean)
result3= f_oneway(m_coach_foul_90_clean, f_coach_foul_90_clean)
result4= alexandergovern(m_coach_foul_90_clean,f_coach_foul_90_clean)
print(result3)
print(result4)
describe4= stats.describe(result4)
print(describe4)

print("2020-21")
print(m_coach_foul_01_clean)
print(f_coach_foul_01_clean)
result5= f_oneway(m_coach_foul_01_clean, f_coach_foul_01_clean)
result6= alexandergovern(m_coach_foul_01_clean,f_coach_foul_01_clean)
print(result5)
print(result6)
describe6= stats.describe(result6)
print(describe6)

print("2021-22")
print(m_coach_foul_12_clean)
print(f_coach_foul_12_clean)
result7= f_oneway(m_coach_foul_01_clean, f_coach_foul_12_clean)
result8= alexandergovern(m_coach_foul_01_clean,f_coach_foul_12_clean)
print(result7)
print(result8)
describe8= stats.describe(result8)
print(describe8)

print("2022-23")
print(m_coach_foul_23_clean)
print(f_coach_foul_23_clean)
result9= f_oneway(m_coach_foul_01_clean, f_coach_foul_23_clean)
result10= alexandergovern(m_coach_foul_01_clean,f_coach_foul_23_clean)
print(result9)
print(result10)
describe10= stats.describe(result10)
print(describe10)       
"""
        


         
