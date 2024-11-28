
import csv
import pandas as pd
import numpy as np


gamedata_file= 'gamedataFLORIDA5szn.csv'
ref_column= 'Refs'
full_reflist=[]
refset=set()
edit_reflist=[]
ref_id=[]

#read_column= pd.read_csv(gamedata_file)[ref_column]

df= pd.read_csv(gamedata_file)
#read_column = df[ref_column]

df['Ref1']=""
df['Ref2']=""
df['Ref3']=""

i = 0


while i < len(df):
#while i<1458:
    s = df.loc[i, ref_column]
    print(i)
    if pd.notna(s) and s != 'Refs':
        reflist = s.split(',')
        reflist = [string.strip() for string in reflist]
        full_reflist= full_reflist+reflist
        # Assign values based on the length of reflist
        if len(reflist) >= 1:
            df.at[i, 'Ref1'] = reflist[0]
            print(reflist[0])
        if len(reflist) >= 2:
            df.at[i, 'Ref2'] = reflist[1]
            print(reflist[1])
        if len(reflist) >= 3:
            df.at[i, 'Ref3'] = reflist[2]
            print(reflist[2])
        

    i += 1

print("test")

df.to_csv(gamedata_file, index=False)





# Remove spaces from the strings 
#cleaned_reflist = [string.strip() for string in full_reflist]

#print("Clean", cleaned_reflist)
#print(len(cleaned_reflist))

print(full_reflist)

for item in full_reflist:
    if item not in refset:
        edit_reflist.append(item)
        refset.add(item)

print("edit list")
print(len(edit_reflist))



for index, element in enumerate(edit_reflist):
    number = 1 + index
    ref_id.append(number)
    #print(f"{element}: {number}")

value_mapping= dict(zip(edit_reflist, ref_id))
for element in edit_reflist:
    value=value_mapping[element]
    print(f"{element}: {value}")

#print(value_mapping['Lou Moglino'])
#df = pd.read_csv(gamedata_file)
#print(df.at[0, 'Ref1'])



df = pd.read_csv(gamedata_file)

i = 0

while i < len(df):
    initial_val=df.at[i, 'Ref1']
    #new_val= value_mapping[initial_val]
    new_val = value_mapping.get(initial_val, initial_val)
    #new_val = value_mapping.get(initial_val)
    df.at[i,'Ref1']= new_val
    print(new_val)

    initial_val=df.at[i, 'Ref2']
    #new_val= value_mapping[initial_val]
    new_val = value_mapping.get(initial_val, initial_val)
    #new_val = value_mapping.get(initial_val)
    df.at[i,'Ref2']= new_val
    print(new_val)

    initial_val=df.at[i, 'Ref3']
    #new_val= value_mapping[initial_val]
    new_val = value_mapping.get(initial_val, initial_val)
    #new_val = value_mapping.get(initial_val)
    df.at[i,'Ref3']= new_val
    print(new_val)

    i+=1

    

df.to_csv(gamedata_file, index=False)

