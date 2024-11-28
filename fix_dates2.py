import pandas as pd

# Read the CSV file
df = pd.read_csv('dates_edit.csv')


# Function to correct the date format
def correct_date_format(date):
    if pd.isnull(date):
        return None
    parts = date.split('/')
    if len(parts) == 3 and len(parts[1]) == 2 and parts[1] in {'18', '19', '20', '21', '22', '23'}:
        # Swap second and third parts
        return f"{parts[0]}/{parts[2]}/{parts[1]}"
    return date

# Apply the function to correct the date format
df['Date'] = df['Date'].apply(correct_date_format)

# Save the corrected DataFrame to a new CSV file
df.to_csv('dates_edit2.csv', index=False)

print("File saved successfully.")
