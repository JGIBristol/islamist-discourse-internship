import string
import nltk 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
import sys
from nltk.corpus import wordnet
from nltk import pos_tag


def Lowercase(text):
    try:
        
        assert(type(text) == str)
        
    except AssertionError:
        
        warnings.warn(f"Expecting a string, recieved {typer(text)} instead")
        
        raise TypeError
    #Lowercase every word in a text input string output string
    return text.lower()

def RemovePunctuation(text):
    try:
        
        assert(type(text) == str)
        
    except AssertionError:
        
        warnings.warn(f"Expecting a string, recieved {typer(text)} instead")
        
        raise TypeError
    #Removes punctuation input string output string
    output = ""
    for i in range(len(text)):
        if text[i] not in string.punctuation:
            output += text[i]
    return output
            
def MeaninglessWords(array):
    try:
        
        assert(type(array) == list)
        
    except AssertionError:
        
        warnings.warn(f"Expecting a array, recieved {typer(array)} instead")
        
        raise TypeError
    #Removes meaningless words input string output string
    additional = ["also"]
    meaningless = stopwords.words('english') + additional
    
    return [i for i in array if i not in meaningless]

    

def SplitText(text):
    try:
        
        assert(type(text) == str)
        
    except AssertionError:
        
        warnings.warn(f"Expecting a string, recieved {typer(text)} instead")
        
        raise TypeError
    #Input string output list splits text in an array
    return word_tokenize(text)



def Lemmatization(array):
    try:
        
        assert(type(array) == list)
        
    except AssertionError:
        
        warnings.warn(f"Expecting a string, recieved {typer(array)} instead")
        
        raise TypeError
        
    #Lemmatizes each word in an array
    lemmatizer = WordNetLemmatizer()
    dictionary = {"V" : wordnet.VERB, "J" : wordnet.ADJ, "N" : wordnet.NOUN, "R" : wordnet.ADV}
    
    ReplaceDict = {"lebanese" : "lebanon"}
    
    new = []
    tags = pos_tag(array)

    for index, word in enumerate(array):
        
        tag = tags[index][1]
        
        if word in ReplaceDict:
            word = ReplaceDict[word]
            
        if tag[0] in dictionary:
            
            new.append(lemmatizer.lemmatize(word, pos = dictionary[tag[0]]))
        
        else:
            
            new.append(lemmatizer.lemmatize(word))

    return new





def FrequentWords(array):
    try: 
        assert(type(array) == list)
        
    except AssertionError:
        
        warnings.warn(f"Expecting a list, recieved {type(array)} instead")
        
        raise TypeError

    #Counts the amount of times each word is mentioned, creates a dictionary.
    count = 0
    UniqueWords = {i : 0 for i in array}
    for i in UniqueWords:
        for j in array:
            if i == j:
                count += 1
        UniqueWords[i] = count
        count = 0
        
    return sorted([(i, UniqueWords[i]) for i in UniqueWords], key = lambda x : x[1])
    


def Graph(output):
    x, y = zip(*output)
    plt.plot(x, y)
    plt.xticks(x, x, rotation='vertical')
    plt.margins(0.1)
    plt.subplots_adjust(bottom=0.15)
    plt.show()
    
    
def ProcessSpeach(text):
    #Run each function above in order on each text, returns lemmatizatization of text
    try:
        
        assert(type(text) == str)
        
    except AssertionError:
        
        warnings.warn(f"Expecting a string, recieved {typer(text)} instead")
        
        raise TypeError
    
    text = Lowercase(text)
    text = RemovePunctuation(text)
    array = SplitText(text)
    array = Lemmatization(array)
    array = MeaninglessWords(array)
    

    
    return array
    
        
def RunEnglishText(debug = False):
    '''
    Run whole processing pipeline, Main function.
    find most frequent words
    '''
    
    df = pd.read_csv('/Users/bashir_a1/Desktop/Internship/nlp-islamist-discourse/data/original/english_corpus.csv/english_corpus.csv', index_col = False, sep = ',')
    
    bagofwords = []
    for i, row in df.iterrows():
        if i > 10 and debug == True:
            break
            
        
        if not pd.isna(row["Text"]):
            
            bagofwords += ProcessSpeach(row["Text"])
            
    
    
    print(len(FrequentWords(bagofwords)))
    
    print(Graph(FrequentWords(bagofwords)[-20:]))
            
    

    
    return None


RunEnglishText(debug = True)
