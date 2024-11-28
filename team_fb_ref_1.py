#1-TEAM FAVORED BY ANY REF?
"""
r1=[auptotfoul r1, fgcutotfoul r1, ...]
foneway[r1, r2, ...rn]
"""
#compare list of all of r1 fouls per team to list of all of other ref fouls per team

import pandas as pd
import numpy as np
from scipy.stats import f_oneway
from scipy.stats import alexandergovern

#7-5-3
#ref_foul = 'reffoulcountASUNall.csv'
#ref_foul_team = 'reffoulgamecountASUNall.csv'
#7-4-6
ref_foul= 'reffoulcountFLORIDAall.csv'
ref_foul_team='reffoulgamecountFLORIDAall.csv'
ref = 'Ref'
fouls = 'TotFouls'
games = 'GameCount'
team = 'Team'

ref_lst=[[] for _ in range(1, 752)]
ref_lst_filt=[[] for _ in range(1, 752)]

df = pd.read_csv(ref_foul_team)

i=0
while i<len(df):
    if df.loc[i,games] != "0":
        foul_count= df.loc[i, fouls]
        ref_id= int(df.loc[i,ref])
        ref_lst[ref_id-1].append(foul_count)
    i+=1

for i, values in enumerate(ref_lst):
    print(f"ref_{i+1}: {values}")

for i, values in enumerate(ref_lst):
    ref_lst_filt[i]= list(filter(lambda x: x != 0, ref_lst[i]))
    print(ref_lst_filt[i])



lists_to_compare = [ref_lst[i-1] for i in range(1, 752) if len(ref_lst[i-1]) > 5]
result = f_oneway(*lists_to_compare)
alex_result1= alexandergovern(*lists_to_compare)


lists_to_compare2 = [ref_lst_filt[i-1] for i in range(1, 752) if len(ref_lst_filt[i-1]) > 5]
result2 = f_oneway(*lists_to_compare2)
alex_result2= alexandergovern(*lists_to_compare2)


print("TEAM FAVORED BY ANY REF?")
#print("asun 5 szns")
print("florida 5 szns")
print("comparing list of all of r1 fouls per team to list of all of other ref fouls per team")
#print(result)
#print(alex_result1)
print("without zeros included in the lists")
print(result2)
print(alex_result2)

    