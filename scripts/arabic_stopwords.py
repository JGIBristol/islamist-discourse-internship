"""
Downloads and saves arabic stopwords from NLTK (Natural Language ToolKit) to a text (.txt) file
"""

from nltk.corpus import stopwords

stopwords_list = stopwords.words('arabic')
with open('../data/created/arabic_stopwords_nltk.txt', 'w') as f:
    f.write('\n'.join(stopwords_list))
