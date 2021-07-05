"""
The original data contains a title field which often has a date of publication in the title. This script extracts that
 date using a regular expression (since it can be in multiple formats), and then saves it as a new file with a date
 field.
"""

import pandas as pd
import re
from dateutil import parser

# Reads CSV file of original data:
df = pd.read_csv('../data/original/arabic_corpus.csv', sep=',')

title_col = 'Title'
date_col = 'Date_of_Publication'
dates = []
for title in df[title_col]:
    reg = re.search(r'(\d+-?\/?\d+-?\/?\d+)', title)  # regex searches for date-like string in the title column
    if reg is not None:
        date_string = reg.group(0)
        try:
            date = parser.parse(date_string)
        except parser.ParserError:
            print(f"Could not parse date string {date_string} from title '{title}'."
                  f"  Check input file and rerun or correct manually. \n\n")
    else:
        date = None
    dates.append(date)
df[date_col] = pd.Series(dates, index=df.index)
print(f"Finds {len(df[~df[date_col].isna()])} out of {len(df)} dates.")

# Save new CSV file containing datetime field
df.to_csv('../data/created/arabic_with_date.csv', sep=',', index=False)



