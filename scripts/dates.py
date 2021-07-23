"""
The original data contains a title field which often has a date of publication in the title. This script extracts that
 date using a regular expression (since it can be in multiple formats), and then saves it as a new file with a date
 field.
"""

import pandas as pd
import re
from dateutil import parser
import logging
import warnings


date_col = 'Date_of_Publication'
title_col = 'Title'


def add_date(df):
    """
    Uses a regular expression to extract dates from the Title, and converts them to a datetime object.
    :param df: pandas DataFrame
    :return:
    """

    if title_col not in df.columns:
        warnings.warn(f"Expecting column '{title_col}'")

    dates = []
    for i, row in df.iterrows():

        title = row[title_col]

        if pd.isna(title):
            date = None
            dates.append(date)
            continue

        reg = re.search(r'(\d+-?\/?\d+-?\/?\d+)', title)  # regex searches for date-like string in the title column
        if reg is not None:
            date_string = reg.group(0)
            try:
                date = parser.parse(date_string)
            except parser.ParserError:
                logging.warning(f"Could not parse date string {date_string} from title '{title.strip()}' on row {i}. "
                                f"Check input file and rerun or correct manually.")
                date = None
        else:
            # logging.debug(f"Could not find date in {title.strip()}")
            date = None
        dates.append(date)
    df[date_col] = pd.Series(dates, index=df.index)
    logging.info(f"Finds {len(df[~df[date_col].isna()])} out of {len(df)} dates.")
    return df


def add_date_arabic():
    """Adds date to the arabic corpus"""
    logging.info("Beginning creating date for Arabic corpus")
    df = pd.read_csv('../data/original/arabic_corpus.csv', sep=',')
    df = add_date(df)

    df.loc[285, date_col] = parser.parse('2020/5/22')  # Error in Title, see `extract_date.log`
    logging.info("Fixing row 285")

    df.to_csv('../data/created/arabic_with_date.csv', sep=',', index=False)
    logging.info("Finished creating date for Arabic corpus")


def add_date_english():
    """Adds date to the english corpus"""
    logging.info("Beginning creating date for English corpus")
    df = pd.read_csv('../data/original/english_corpus.csv', sep=',')
    df = add_date(df)

    df.loc[3, date_col] = parser.parse('22-09-2006')  # Error in Title, see `extract_date.log`
    logging.info("Fixing row 3")

    df.to_csv('../data/created/english_with_date.csv', sep=',', index=False)
    logging.info("Finished creating date for English corpus")


if __name__ == '__main__':
    logging.basicConfig(filename='../logfiles/extract_date.log',
                        format='%(asctime)s:%(levelname)s:%(message)s',
                        level=logging.DEBUG)

    add_date_arabic()
    add_date_english()
    
    
    
    
    
    