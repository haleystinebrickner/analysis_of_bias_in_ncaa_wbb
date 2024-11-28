import pandas as pd
import numpy as np
from scipy.stats import f_oneway
"""
import scipy.stats as stats
import os
import random

import statsmodels.api as sm
import statsmodels.stats.multicomp

from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
"""
ref_foul='reffoulcount.csv'
ref_foul_team='reffoulgamecount2.csv'
ref='Ref'
fouls='TotFouls'
games= 'GameCount'
team= 'Team'

ref_list_foul=[]
ref_list_game=[]
ftst=[]

aup=[]
eku=[]
jax=[]
ksu=[]
lip=[]
uca=[]
una=[]
unf=[]
bu=[]
ju=[]
qu=[]
su=[]
fgcu=[]

df = pd.read_csv(ref_foul_team)


ref_count=1
while ref_count<343:
    i=0
    while i < len(df):
        ref_num = df.loc[i, ref]
        if ref_num== ref_count:
            ref_foul= df.loc[i, fouls]
            game_count= df.loc[i, games]
            reffoul_pgame= ref_foul/game_count
            ref_list_foul.append(ref_foul/game_count)
        team_name= df.loc[i, team]
        if team_name== 'Austin Peay':
            aup[ref_count]= reffoul_pgame    
        elif team_name== 'Eastern Ky.':
            eku[ref_count]= reffoul_pgame
        elif team_name=='Jacksonville St.':
            jax[ref_count]=reffoul_pgame
        elif team_name=='Kennesaw St.':
            ksu[ref_count]= reffoul_pgame
        elif team_name=='Lipscomb':
            lip[ref_count]= reffoul_pgame
        elif team_name=='Central Ark.':
            uca[ref_count]=reffoul_pgame
        elif team_name=='North Ala.':
            una[ref_count]= reffoul_pgame
        elif team_name=='North Florida':
            unf[ref_count]=reffoul_pgame
        elif team_name=='Bellarmine':
            bu[ref_count]= reffoul_pgame
        elif team_name=='Jacksonville':
            ju[ref_count]= reffoul_pgame
        elif team_name== 'Queens (NC)':
            qu[ref_count]= reffoul_pgame
        elif team_name=='Stetson':
            su[ref_count]= reffoul_pgame
        elif team_name=='FGCU':
            fgcu[ref_count]=reffoul_pgame

        i+=1
    ref_count+=1

ref_count=1    
while ref_count<343:
    aup_ref= aup[ref_count]
    eku_ref= eku[ref_count]
    jax_ref= jax[ref_count]
    ksu_ref= ksu[ref_count]
    lip_ref= lip[ref_count]
    uca_ref= uca[ref_count]
    una_ref= una[ref_count]
    unf_ref= unf[ref_count]
    bu_ref= bu[ref_count]
    ju_ref= ju[ref_count]
    qu_ref= qu[ref_count]
    su_ref= su[ref_count]
    fgcu_ref= fgcu[ref_count]

    ftst[ref_count]=f_oneway(aup_ref, eku_ref, jax_ref, ksu_ref, lip_ref, uca_ref, una_ref, unf_ref, bu_ref, ju_ref, qu_ref, su_ref, fgcu_ref)

    ref_count+=1

    
for refcount in ftst:
    print (ftst[refcount])


   





