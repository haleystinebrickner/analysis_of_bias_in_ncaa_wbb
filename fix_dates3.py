import pandas as pd

input_file = "dates_edit2.csv"
column_name = "Date"
output_file = "dates_edit3.csv"

def fix_date_format(date_str):
    # Check if date_str has format 'YYYY/MM/DD'
    if len(date_str) == 10 and date_str[4] == '-':
        # Check if the first term starts with '20', indicating year
        if date_str.startswith('20'):
            # Remove '20' from the first term to make it a month
            date_str = date_str[2:]
        # Split the date string into parts
        parts = date_str.split('-')
        # Rearrange the parts: switch middle and last terms

        return f"{parts[1]}/{parts[2]}/{parts[0]}"
            
    else:
        return date_str

def fix_csv_date_column(input_file, column_name, output_file):
    # Read CSV file
    df = pd.read_csv(input_file)

    # Fix date format in specified column
    df[column_name] = df[column_name].apply(fix_date_format)

    # Write corrected data to new CSV file
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    fix_csv_date_column(input_file, column_name, output_file)
