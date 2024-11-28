#perform t tests to determine ref with bias foul count call

import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import f_oneway
from scipy.stats import alexandergovern




away_fouls= "APf"
home_fouls="HPf"

tot_fouls= 'TotFouls'

gamedata_file = 'gamedataASUN5sznEDIT.csv'
reffoulgamecount_file= 'reffoulgamecountASUNall.csv'

#gamedata_file= 'gamedataFLORIDA5sznEDIT.csv'
#reffoulgamecount_file= 'reffoulgamecountFLORIDAall.csv'

ref_lst=[[] for _ in range(0, 752)]
ref_lst_filt=[[] for _ in range(0, 752)]
tot_lst=[]

df = pd.read_csv(reffoulgamecount_file)

i=0
while i<len(df):

    j=1

    while j<= 751:

        if int(df.loc[i, "Ref"])==j:
            print("Ref ",j)
            game_foul= df.loc[i,tot_fouls]
            ref_lst[j].append(game_foul)
            tot_lst.append(game_foul)

        j+=1
    
    i+=1

print(tot_lst)

tot_lst_filter = [x for x in tot_lst if x != 0]

print(tot_lst_filter)

i=1
for i in range(1,752):
    #print(ref_lst[i])
    ref_lst_filt[i]= [x for x in ref_lst[i] if x != 0]
    if len(ref_lst_filt[i])>1:
        print(ref_lst_filt[i])
        t_result= stats.ttest_ind(a=ref_lst_filt[i], b=tot_lst_filter, equal_var=False)
        alex_result= alexandergovern(ref_lst_filt[i], tot_lst_filter)
        print("REF ", i)
        print(t_result)
        print(alex_result)

    i+=1

#lists_to_compare = [ref_lst[i-1] for i in range(1, 752)]

