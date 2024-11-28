import pandas as pd

gamedata_file = 'gamedataFLORIDA5szn.csv'
ref_column = 'Refs'

# Read the CSV file
df = pd.read_csv(gamedata_file)

# Split the 'Refs' column and expand it into multiple columns
ref_split = df[ref_column].str.split(',', expand=True)

print(ref_split.shape)

# Rename the columns to Ref1, Ref2, Ref3
ref_split.columns = ['Ref1', 'Ref2', 'Ref3','Ref4']

# Concatenate the split columns with the original DataFrame
df = pd.concat([df, ref_split], axis=1)

# Clean up leading/trailing whitespaces in referee columns
df['Ref1'] = df['Ref1'].str.strip()
df['Ref2'] = df['Ref2'].str.strip()
df['Ref3'] = df['Ref3'].str.strip()

# Create a set of unique referees
ref_set = set(df[['Ref1', 'Ref2', 'Ref3']].values.flatten())

# Create a mapping of referees to IDs
ref_id_mapping = {referee: i + 1 for i, referee in enumerate(ref_set)}

# Map the referees to their corresponding IDs
df['Ref1_ID'] = df['Ref1'].map(ref_id_mapping)
df['Ref2_ID'] = df['Ref2'].map(ref_id_mapping)
df['Ref3_ID'] = df['Ref3'].map(ref_id_mapping)

# Write the updated DataFrame to a new CSV file
df.to_csv('updated_gamedata.csv', index=False)
