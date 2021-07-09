import string
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pandas as pd

df = pd.read_csv('/Users/bashir_a1/Desktop/Internship/nlp-islamist-discourse/data/original/english_corpus.csv/english_corpus.csv', sep = '\n' or ',', skiprows = 3)

print(df)

print(df.loc[0][0])


def SplitText(text):
    return word_tokenize(text)

def Lowercase(text):
    return text.lower()

def RemovePunctuation(text):
    output = ""
    for i in range(len(text)):
        if text[i] not in string.punctuation:
            output += text[i]
    return output
            
def MeaninglessWords(text):
    meaningless = stopwords.words('english')
    words = SplitText(text)
    return ''.join([i for i in words if i not in meaningless])

def Lemmatization(x):
    return 0

print(MeaninglessWords(df.loc[0][0]))