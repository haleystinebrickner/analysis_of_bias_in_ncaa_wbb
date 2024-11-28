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

m_coach_foul=[[] for _ in range(0, 752)]
f_coach_foul=[[] for _ in range(0, 752)]

m_coach_foul_filt=[[] for _ in range(0, 752)]
f_coach_foul_filt=[[] for _ in range(0, 752)]


m_tot_lst=[]
f_tot_lst=[]

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
        #print(i)
        if (((df.loc[i, "Ref1"])==j) or ((df.loc[i, "Ref2"])==j) or ((df.loc[i, "Ref3"])==j)): 
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

                
                away_split = coaches_dict.get(away, ["", "", "", "", ""])
                home_split = coaches_dict.get(home, ["", "", "", "", ""])
                
                #away_split= coaches_dict[away][0].split("/")
                #home_split= coaches_dict[home][0].split("/")

                away_cg= away_split[0]
                home_cg= home_split[0]

                away_cg= away_cg.split("/")
                home_cg= home_cg.split("/")

                #print(away_cg)
                #print(home_cg)
                

                if away_cg[0]== "M":
                    m_coach_foul[j].append(away_fc)
                    m_tot_lst.append(away_fc)
                    gamecount+=1
                    #print(away_fc)
                elif away_cg[0]=="F":
                    f_coach_foul[j].append(away_fc)
                    f_tot_lst.append(away_fc)
                    gamecount+=1
                    #print(away_fc)
                

                if home_cg[0]== "M":
                    m_coach_foul[j].append(home_fc)
                    m_tot_lst.append(home_fc)
                    gamecount+=1
                    #print(home_fc)
                elif home_cg[0]=="F":
                    f_coach_foul[j].append(home_fc)
                    f_tot_lst.append(home_fc)
                    gamecount+=1
                    #print(home_fc)
            
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

                    
                    away_split = coaches_dict.get(away, ["", "", "", "", ""])
                    home_split = coaches_dict.get(home, ["", "", "", "", ""])
                    
                    #away_split= coaches_dict[away][0].split("/")
                    #home_split= coaches_dict[home][0].split("/")

                    away_cg= away_split[1]
                    home_cg= home_split[1]

                    away_cg= away_cg.split("/")
                    home_cg= home_cg.split("/")

                    #print(away_cg)
                    #print(home_cg)
                    

                    if away_cg[0]== "M":
                        m_coach_foul[j].append(away_fc)
                        m_tot_lst.append(away_fc)
                        gamecount+=1
                        #print(away_fc)
                    elif away_cg[0]=="F":
                        f_coach_foul[j].append(away_fc)
                        f_tot_lst.append(away_fc)
                        gamecount+=1
                        #print(away_fc)
                    

                    if home_cg[0]== "M":
                        m_coach_foul[j].append(home_fc)
                        m_tot_lst.append(home_fc)
                        gamecount+=1
                        #print(home_fc)
                    elif home_cg[0]=="F":
                        f_coach_foul[j].append(home_fc)
                        f_tot_lst.append(home_fc)
                        gamecount+=1
                        #print(home_fc)

                
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

                    
                    away_split = coaches_dict.get(away, ["", "", "", "", ""])
                    home_split = coaches_dict.get(home, ["", "", "", "", ""])
                    
                    #away_split= coaches_dict[away][0].split("/")
                    #home_split= coaches_dict[home][0].split("/")

                    away_cg= away_split[2]
                    home_cg= home_split[2]

                    away_cg= away_cg.split("/")
                    home_cg= home_cg.split("/")

                    #print(away_cg)
                    #print(home_cg)
                    

                    if away_cg[0]== "M":
                        m_coach_foul[j].append(away_fc)
                        m_tot_lst.append(away_fc)
                        gamecount+=1
                        #print(away_fc)
                    elif away_cg[0]=="F":
                        f_coach_foul[j].append(away_fc)
                        f_tot_lst.append(away_fc)
                        gamecount+=1
                        #print(away_fc)
                    

                    if home_cg[0]== "M":
                        m_coach_foul[j].append(home_fc)
                        m_tot_lst.append(home_fc)
                        gamecount+=1
                        #print(home_fc)
                    elif home_cg[0]=="F":
                        f_coach_foul[j].append(home_fc)
                        f_tot_lst.append(home_fc)
                        gamecount+=1
                        #print(home_fc)

                
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

                    
                    away_split = coaches_dict.get(away, ["", "", "", "", ""])
                    home_split = coaches_dict.get(home, ["", "", "", "", ""])
                    
                    #away_split= coaches_dict[away][0].split("/")
                    #home_split= coaches_dict[home][0].split("/")

                    away_cg= away_split[3]
                    home_cg= home_split[3]

                    away_cg= away_cg.split("/")
                    home_cg= home_cg.split("/")

                    #print(away_cg)
                    #print(home_cg)
                    

                    if away_cg[0]== "M":
                        m_coach_foul[j].append(away_fc)
                        m_tot_lst.append(away_fc)
                        gamecount+=1
                        #print(away_fc)
                    elif away_cg[0]=="F":
                        f_coach_foul[j].append(away_fc)
                        f_tot_lst.append(away_fc)
                        gamecount+=1
                        #print(away_fc)
                    

                    if home_cg[0]== "M":
                        m_coach_foul[j].append(home_fc)
                        m_tot_lst.append(home_fc)
                        gamecount+=1
                        #print(home_fc)
                    elif home_cg[0]=="F":
                        f_coach_foul[j].append(home_fc)
                        f_tot_lst.append(home_fc)
                        gamecount+=1
                        #print(home_fc)

                
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

                    
                    away_split = coaches_dict.get(away, ["", "", "", "", ""])
                    home_split = coaches_dict.get(home, ["", "", "", "", ""])
                    
                    #away_split= coaches_dict[away][0].split("/")
                    #home_split= coaches_dict[home][0].split("/")

                    away_cg= away_split[4]
                    home_cg= home_split[4]

                    away_cg= away_cg.split("/")
                    home_cg= home_cg.split("/")

                    #print(away_cg)
                    #print(home_cg)
                    

                    if away_cg[0]== "M":
                        m_coach_foul[j].append(away_fc)
                        m_tot_lst.append(away_fc)
                        gamecount+=1
                        #print(away_fc)
                    elif away_cg[0]=="F":
                        f_coach_foul[j].append(away_fc)
                        f_tot_lst.append(away_fc)
                        gamecount+=1
                        #print(away_fc)
                    

                    if home_cg[0]== "M":
                        m_coach_foul[j].append(home_fc)
                        m_tot_lst.append(home_fc)
                        gamecount+=1
                        #print(home_fc)
                    elif home_cg[0]=="F":
                        f_coach_foul[j].append(home_fc)
                        f_tot_lst.append(home_fc)
                        gamecount+=1
                        #print(home_fc)

        i+=1 
    j+=1   

m_tot_lst_filter = [x for x in m_tot_lst if x != 0]
f_tot_lst_filter = [x for x in f_tot_lst if x != 0]

#print(tot_lst_filter)
#print(tot_gamefouls/tot_gamecount)

i=1
for i in range(0,752):
    #print(ref_lst[i])
    m_coach_foul_filt[i]= [x for x in m_coach_foul[i] if x != 0]
    f_coach_foul_filt[i]= [x for x in f_coach_foul[i] if x != 0]

    if len(m_coach_foul_filt[i])>1:
        print(m_coach_foul_filt[i])
        t_result= stats.ttest_ind(a=m_coach_foul_filt[i], b=m_tot_lst_filter, equal_var=False)
        #alex_result= alexandergovern(ref_lst_filt[i], tot_lst_filter)
        print("REF ", i, ":Male")
        print(t_result)
        #print(alex_result)
        #print(ref_add[i]/ref_gamecount[i])
    
    if len(f_coach_foul_filt[i])>1:
        print(f_coach_foul_filt[i])
        t_result= stats.ttest_ind(a=f_coach_foul_filt[i], b=f_tot_lst_filter, equal_var=False)
        #alex_result= alexandergovern(ref_lst_filt[i], tot_lst_filter)
        print("REF ", i, ":Female")
        print(t_result)
        #print(alex_result)
        #print(ref_add[i]/ref_gamecount[i])

    i+=1


