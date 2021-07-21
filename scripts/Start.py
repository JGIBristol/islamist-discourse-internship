import string
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np





def SplitText(text):
    #Input string output list splits text in an array
    return word_tokenize(text)

def Lowercase(text):
    #Lowercase every word in a text input string output string
    return text.lower()

def RemovePunctuation(text):
    #Removes punctuation input string output string
    output = ""
    for i in range(len(text)):
        if text[i] not in string.punctuation:
            output += text[i]
    return output
            
def MeaninglessWords(text):
    #Removes meaningless words input string output string
    meaningless = stopwords.words('english')
    words = SplitText(text)
    return ' '.join([i for i in words if i not in meaningless])

def Lemmatization(x):
    return 0


def FrequentWords(text):
    count = 0
    array = SplitText(text)
    UniqueWords = {i : 0 for i in array}
    for i in UniqueWords:
        for j in array:
            if i == j:
                count += 1
        UniqueWords[i] = count
        count = 0
    return UniqueWords
    

def Graph(diction):
    x = np.array([i for i in range(len(diction))])
    print(diction)
    y = np.array([diction[i] for i in diction])
    xmap = [i for i in diction]
    plt.xticks(x, xmap)
    plt.plot(x, y)
    plt.show()

        
def RunEnglishText(debug = False):
    '''
    Run whole processing pipeline, Main function.
    find most frequent words
    '''
    
    df = pd.read_csv('/Users/bashir_a1/Desktop/Internship/nlp-islamist-discourse/data/original/english_corpus.csv/english_corpus.csv', index_col = False, sep = ',')
    
    bagofwords = []
    for i, row in df.iterrows():
        if i > 100 and debug == True:
            break
        
        if not pd.isna(row["Text"]):
            bagofwords += SplitText(row["Text"])
    print(type(bagofwords))
    text = " ".join(bagofwords)
    LowerText = Lowercase(text)
    PunctText = RemovePunctuation(LowerText)
    MeaningfulText = MeaninglessWords(PunctText)
    MostFreqWords = FrequentWords(MeaningfulText)

    
    return None


RunEnglishText(debug = True)
