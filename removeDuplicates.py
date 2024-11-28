import csv
import pandas as pd


#gamedata_file= 'gamedata24fla-2.csv'
gamedata_file= 'gamedataFLORIDA5szn.csv'
#gamedata_file_edit= 'gamedata24fla-2-edit.csv'
gamedata_file_edit= 'gamedataFLORIDA5sznEDIT.csv'
a_score='AScore'
h_score='HScore'
a_team='AwayTeam'
h_team='HomeTeam'
game_date='Gamedate'
ref_column= 'Refs'



df = pd.read_csv(gamedata_file)



duplicate_rows = df.duplicated(subset=[a_score, h_score, a_team, h_team, game_date], keep='first')

# Invert the boolean mask to keep non-duplicate rows
df_filtered = df[~duplicate_rows]

# Save the filtered DataFrame to a new CSV file
df_filtered.to_csv(gamedata_file_edit, index=False)


"""

# Group the DataFrame by the columns of interest and keep only the first occurrence in each group
df_filtered = df.groupby([a_score, h_score, a_team, h_team, game_date]).first().reset_index()

# Save the filtered DataFrame to a new CSV file
df_filtered.to_csv(gamedata_file_edit, index=False)
"""

#above worked without gameID
"""

rows_to_remove = set()  # Using a set to ensure uniqueness

df = pd.read_csv(gamedata_file)

for index1, row1 in df.iterrows():
    if index1 not in rows_to_remove:
        for index2, row2 in df.iterrows():
            if index1 != index2 and index2 not in rows_to_remove:  # Avoid comparing the same row and rows already marked for removal
                if (row1[a_score] == row2[h_score]) and (row1[a_team] == row2[h_team]):
                    rows_to_remove.add(index2)
                    break  # Stop further comparison if a match is found

# Remove duplicate rows
df.drop(index=rows_to_remove, inplace=True)

# Reset the index after removing rows
df.reset_index(drop=True, inplace=True)

# Display the DataFrame after removing duplicates
print(rows_to_remove)

# Save the edited DataFrame to a new CSV file
df.to_csv(gamedata_file_edit, index=False)
"""