#read list of refs with p<0.05 compared to ref crew in gamedata
#if two refs are common save row of gamedata file 

import pandas as pd

ref1 = 'Ref1'
ref2 = 'Ref2'
ref3 = 'Ref3'

#gamedata_file = 'gamedataASUN5sznEDIT.csv'
#reffoulgamecount_file= 'reffoulgamecountASUNall.csv'
#ref-foul
#ref_siglist=[9, 22, 27, 28, 30, 98, 105, 108, 165, 180, 184, 194, 220, 227, 235, 240, 248, 282, 342, 345, 443, 464, 465, 466, 486, 593, 603, 643, 678, 731]
#m-ref-bias
#ref_siglist=[9, 12, 27, 48, 75, 76, 105, 110, 135, 177, 220, 227, 248, 254, 278, 282, 288, 352, 480, 543, 544, 545]
#f-ref-bias- note 0
#ref_siglist= [6, 22, 78, 105, 152, 174, 190, 194, 203, 222, 240, 303, 364, 365, 366, 379, 384, 424, 436, 614, 615]
#b-ref-bias
#ref_siglist=[6, 42, 99, 135, 177, 186, 220, 227, 273, 282, 288, 300, 304, 384]
#w-ref-bias- note 0
#ref_siglist=[14, 54, 74, 78, 99, 105, 126, 152, 183, 194, 195, 276, 301, 303, 340, 352, 614, 678, 718]
#h-bias
#ref_siglist=[9, 22, 30, 54, 74, 75, 98, 116, 152, 165, 184, 185, 227, 248, 265, 277, 284, 379, 382, 405, 420, 589, 602, 633]
#a-bias
#ref_siglist=[6, 8, 27, 45, 114, 194, 239, 240, 254, 282, 284, 288, 300, 303, 377, 384, 436, 441, 443, 493, 552, 575, 591, 614, 615, 654, 678, 735]


gamedata_file= 'gamedataFLORIDA5sznEDIT.csv'
#reffoulgamecount_file= 'reffoulgamecountFLORIDAall.csv'
#ref-foul
#ref_siglist=[24, 27, 28, 43, 69, 72, 82, 115, 118, 120, 121, 138, 144, 171, 177, 181, 192, 214, 216, 234, 255, 256, 270, 283, 291, 295, 310, 337, 365, 401, 408, 432, 434, 508, 662]
#m-ref-bias
#ref_siglist=[40, 42, 101, 118, 153, 177, 214, 225, 226, 227, 228, 234, 508, 561, 570]
#f-ref-bias
#ref_siglist=[14, 24, 27, 72, 102, 115, 120, 125, 146, 214, 255, 256, 408, 411, 418, 434]
#b-ref-bias
#ref_siglist=[9, 11, 14, 15, 118, 136, 138, 145, 153, 163, 171, 214, 226, 227, 228, 234, 235, 248, 255, 270, 295, 304, 308, 309, 349, 408, 508]
#w-ref-bias
#ref_siglist=[26, 27, 70, 72, 115, 121, 145, 146, 336, 344, 570, 598, 600, 635, 684]
#h-bias
#ref_siglist=[6, 16, 17, 24, 27, 72, 115, 120, 138, 144, 149, 153, 168, 171, 177, 184, 214, 233, 247, 256, 281, 290, 295, 308, 310, 394, 401, 508, 699]
#a-bias- note 0
ref_siglist=[14, 52, 69, 77, 105, 113, 114, 121, 126, 131, 136, 146, 147, 173, 174, 177, 191, 216, 234, 255, 256, 304, 310, 325, 332, 343, 408, 561, 600]

df = pd.read_csv(gamedata_file)


# Check for missing values in the hfouls and afouls columns and replace with 0
df[ref1] = pd.to_numeric(df[ref1], errors='coerce')
df[ref2] = pd.to_numeric(df[ref2], errors='coerce')
df[ref3] = pd.to_numeric(df[ref3], errors='coerce')

# Handle missing values by replacing NaN with 0
df[ref1].fillna(0, inplace=True)
df[ref2].fillna(0, inplace=True)
df[ref3].fillna(0, inplace=True)


i = 0
while i < len(df):

    #if pd.notna(df['Ref1'].iloc[i]) and df['Ref1'].iloc[i] != "":
    
    ref1id = df.loc[i, ref1]
    ref2id = df.loc[i, ref2]
    ref3id = df.loc[i, ref3]

    
    
    #print(i)
    

    if (ref1id in ref_siglist) and (ref2id in ref_siglist) and (ref3id in ref_siglist):
        print("GAMEDATA ROW: ", i)
        print(ref1id, ref2id, ref3id)
        print(df.loc[i, "AwayTeam"],"-", df.loc[i, "HomeTeam"])
    elif (ref1id in ref_siglist) and (ref2id in ref_siglist):
        print("GAMEDATA ROW: ", i)
        print(ref1id, ref2id)
        print(df.loc[i, "AwayTeam"],"-", df.loc[i, "HomeTeam"])
    elif (ref1id in ref_siglist) and (ref3id in ref_siglist):
        print("GAMEDATA ROW: ", i)
        print(ref1id, ref3id)
        print(df.loc[i, "AwayTeam"],"-", df.loc[i, "HomeTeam"])
    elif (ref2id in ref_siglist) and (ref3id in ref_siglist):
        print("GAMEDATA ROW: ", i)
        print(ref2id, ref3id)
        print(df.loc[i, "AwayTeam"],"-", df.loc[i, "HomeTeam"])
    
    i += 1
