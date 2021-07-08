---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Natural Language Processing of Hezbollah speeches: English Translations

+++

We use the `Pandas` library to read in the data and use a regular expression (using the `re` library) to search for date-like strings in the "Title"s of the text. 
We then convert these strings (e.g. "22-09-2006" or "2020/22/5") to `datetime` objects.
Strings that could not be converted are logged in the `extract_date.log` logfile, revealing one English translation title and one Arabic title that are then corrected manually in the CSV files `arabic_with_date.csv` and `english-with-date.csv` after running the script.
