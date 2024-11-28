#2- REF FAVOR ANY TEAM? transpose of 1
"""
aup=[totfoulaup r1, totfoulaup r2, ..totfoulaup rn]
fgcu=[totfoulfgcu r1, totfoulfgcu r2, ..totfoulfgcu rn]
foneway[aup, fgcu,...]
"""
#compare all fouls from refs for one team to all fouls from refs to other teams

import pandas as pd
import numpy as np
from scipy.stats import f_oneway
from scipy import stats
from scipy.stats import friedmanchisquare
from scipy.stats import alexandergovern

#7-5-3
ref_foul = 'reffoulcountASUNall.csv'
ref_foul_team = 'reffoulgamecountASUNall.csv'
#7-4-6
#ref_foul= 'reffoulcountFLORIDAall.csv'
#ref_foul_team='reffoulgamecountFLORIDAall.csv'


ref = 'Ref'
fouls = 'TotFouls'
games = 'GameCount'
team = 'Team'

#team_lst=[[] for _ in range(1, 14)]
#team_lst_filt=[[] for _ in range(1, 14)]

team_lst=[[] for _ in range(1, 13)]
team_lst_filt=[[] for _ in range(1, 13)]

"""
teams = [
    'Austin Peay', 'Eastern Ky.', 'Jacksonville St.', 'Kennesaw St.',
    'Lipscomb', 'Central Ark.', 'North Ala.', 'North Florida',
    'Bellarmine', 'Jacksonville', 'Queens (NC)', 'Stetson', 'FGCU'
]
"""

teams=['Florida', 'Florida A&M', 'Florida St.','Bethune-Cookman', 'North Florida', 'USF', 'FIU', 'Jacksonville', 'FAU', 'FGCU', 'Stetson', 'Miami']


#teams_id=[0,1,2,3,4,5,6,7,8,9,10,11,12]
teams_id=[0,1,2,3,4,5,6,7,8,9,10,11]




df = pd.read_csv(ref_foul_team)

  
i=0
"""
while i<len(df):
    if df.loc[i,team]=='Austin Peay':
        team_id=0
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='Eastern Ky.':
        team_id=1
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='Jacksonville St.':
        team_id=2
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='Kennesaw St.':
        team_id=3
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='Lipscomb':
        team_id=4
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='Central Ark.':
        team_id=5
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='North Ala.':
        team_id=6
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='North Florida':
        team_id=7
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='Bellarmine':
        team_id=8
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='Jacksonville':
        team_id=9
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='Queens (NC)':
        team_id=10
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='Stetson':
        team_id=11
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='FGCU':
        team_id=12
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    
    i+=1
"""

while i<len(df):
    if df.loc[i,team]=='Florida':
        team_id=0
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='Florida A&M':
        team_id=1
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='Florida St.':
        team_id=2
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='Bethune-Cookman':
        team_id=3
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='North Florida':
        team_id=4
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='USF':
        team_id=5
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='FIU':
        team_id=6
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='Jacksonville':
        team_id=7
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='FAU':
        team_id=8
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='FGCU':
        team_id=9
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='Stetson':
        team_id=10
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    elif df.loc[i,team]=='Miami':
        team_id=11
        if df.loc[i,games] != "0":
            foul_count= df.loc[i, fouls]
            team_lst[team_id].append(foul_count)
    
    i+=1

for id in teams_id:
    print(teams[id], team_lst[id])

for id in teams_id:
    team_lst_filt[id]=list(filter(lambda x: x != 0, team_lst[id]))
    print(teams[id], team_lst_filt[id])

"""
lists_to_compare = [team_lst[i] for i in range(1, 13) if len(team_lst[i]) > 0]
f_result1 = f_oneway(*lists_to_compare)
#k_result1=stats.kruskal(*lists_to_compare)
#fman_result1 = friedmanchisquare(*lists_to_compare)
alex_result1= alexandergovern(*lists_to_compare)


lists_to_compare2 = [team_lst_filt[i] for i in range(1, 13) if len(team_lst_filt[i]) > 0]
f_result2 = f_oneway(*lists_to_compare2)
#k_result2=stats.kruskal(*lists_to_compare2)
#fman_result2 = friedmanchisquare(*lists_to_compare2)
alex_result2= alexandergovern(*lists_to_compare2)
"""

lists_to_compare = [team_lst[i] for i in range(1, 12) if len(team_lst[i]) > 0]
f_result1 = f_oneway(*lists_to_compare)
#k_result1=stats.kruskal(*lists_to_compare)
#fman_result1 = friedmanchisquare(*lists_to_compare)
alex_result1= alexandergovern(*lists_to_compare)


lists_to_compare2 = [team_lst_filt[i] for i in range(1, 12) if len(team_lst_filt[i]) > 0]
f_result2 = f_oneway(*lists_to_compare2)
#k_result2=stats.kruskal(*lists_to_compare2)
#fman_result2 = friedmanchisquare(*lists_to_compare2)
alex_result2= alexandergovern(*lists_to_compare2)


print("REF FAVOR ANY TEAM?")
print("compare all fouls from refs for one team to all fouls from refs to other teams")
#print("asun 5 szns")
print("florida 5 szns")
#print(f_result1)
#print(k_result1)
#print(fman_result1)
#print(alex_result1)
print("without zeros included in the lists")
print(f_result2)
#print(k_result2)
#print(fman_result2)
print(alex_result2)
#print("The one-way ANOVA tests the null hypothesis that two or more groups have the same population mean. The test is applied to samples from two or more groups, possibly with differing sizes.")
#print("The Kruskal-Wallis H-test tests the null hypothesis that the population median of all of the groups are equal.  It is a non-parametric version of ANOVA.  The test works on 2 or more independent samples, which may have different sizes. ")
#print("The Friedman test tests the null hypothesis that repeated samples of the same individuals have the same distribution.  It is often used to test for consistency among samples obtained in different ways.")
#print(" The Alexander-Govern approximation tests the equality of k independent means in the face of heterogeneity of variance. The test is applied to samples from two or more groups, possibly with differing sizes.")