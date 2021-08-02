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
#sklearn tf term freq <<<<<

def Lowercase(text):
    """
    Takes in a string and returns the same string with letters all lowercase

    Parameters
    ----------
    text : String
        Text of each speach.

    Returns
    -------
    String
        Lowercase of the text input.

    """

    try:
        
        assert(type(text) == str)
        
    except AssertionError:
        
        warnings.warn(f"Expecting a string, recieved {type(text)} instead")
        
        raise TypeError
    #Lowercase every word in a text input string output string
    return text.lower()



def RemovePunctuation(text):
    """
    A function that takes in a string and removes the punctuation of the text

    Parameters
    ----------
    text : String
        Text of each speach.

    Returns
    -------
    String
        Text without punctuation.

    """
    try:
        
        assert(type(text) == str)
        
    except AssertionError:
        
        warnings.warn(f"Expecting a string, recieved {type(text)} instead")
        
        raise TypeError
    #Removes punctuation input string output string
    output = ""
    for i in range(len(text)):
        if text[i] not in string.punctuation:
            output += text[i]
    return output


            
def MeaninglessWords(array):
    """
    A function that takes in a list of words and outputs the same list of words
    but removes the meaningless words we dont want

    Parameters
    ----------
    array : List
        List of words for each speach.

    Returns
    -------
    list
        List of words we want.

    """
    try:
        
        assert(type(array) == list)
        
    except AssertionError:
        
        warnings.warn(f"Expecting a array, recieved {type(array)} instead")
        
        raise TypeError
        
    #Removes meaningless words input string output string
    additional = ["also"]
    meaningless = stopwords.words('english') + additional
    
    return [i for i in array if i not in meaningless]

    

def SplitText(text):
    """
    A function that takes a string as a input and tokanizes the text
    
    Parameters
    ----------
    text : String
        String of text.


    Returns
    -------
    List
        Tokanized version of the text.

    """
    try:
        
        assert(type(text) == str)
        
    except AssertionError:
        
        warnings.warn(f"Expecting a string, recieved {type(text)} instead")
        
        raise TypeError
    #Input string output list splits text in an array
    return word_tokenize(text)



def Lemmatization(array):
    """
    A function that lemmatizes the list of words, taking words to their root meaning

    Parameters
    ----------
    array : List
        List of words.

    Returns
    -------
    new : List
        List of words that have been lemmatized.

    """
    try:
        
        assert(type(array) == list)
        
    except AssertionError:
        
        warnings.warn(f"Expecting a string, recieved {type(array)} instead")
        
        raise TypeError
        
    #Lemmatizes each word in an array
    lemmatizer = WordNetLemmatizer()
    dictionary = {"V" : wordnet.VERB, "J" : wordnet.ADJ, "N" : wordnet.NOUN, "R" : wordnet.ADV}
    
    ReplaceDict = {"lebanese" : "lebanon", 
                   "israeli" : "israel",
                   "syrian" : "syria"
                   }
    
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
    """
    
    Counts the amount of times each word is mentioned in a list of words.

    Parameters
    ----------
    array : List
        List of words.


    Returns
    -------
    List
        List of touples that has a word on the first element and amount of times
        the word is repeated in the list of words.

    """
    
    #pandas, valuecounts 
    
    try: 
        assert(type(array) == list)
        
    except AssertionError:
        
        warnings.warn(f"Expecting a list, recieved {type(array)} instead")
        
        raise TypeError
        
        
    #Counts the amount of times each word is mentioned, creates a dictionary.
    UniqueWords = {i : 0 for i in array}
        
    return sorted([(i, array.count(i)) for i in UniqueWords], key = lambda x : x[1])
    
    
#, graphfile, numwords = 20

def FrequencyGraph(frequency, numwords = 20):
    """
    Creates a frequency graph and saves it to a location.
    
    Parameters
    ----------
    frequency : list of tuples
    First element is the word and second element is the frequency of the word.
    
    graphfile : string
    path to where we save the graph
    
    numwords : int
    number of words we want to go through

    Returns
    -------
    None.
    
    """
    
    x, y = zip(*frequency[-numwords:])
    plt.plot(x, y)
    plt.xticks(x, x, rotation='vertical')
    plt.margins(0.1)
    plt.subplots_adjust(bottom=0.15)
    #plt.savefig(graphfile, bbox_inches='tight')
    plt.xlabel("words")
    plt.ylabel("words count")
    
    return None
    

def outputfrequencies(frequencies, freqfile, numwords = 100):
    """
    Creates a frequency csv file and saves it to a location.
    
    Parameters
    ----------
    frequencies : list of tuples
        First element is the word and second element is the frequency of the word
        .
    freqfile : string
        path to where we save the csv file.
    numwords : int
        number of words we want to go through.
        
        
    todo : opposite order sorted

    Returns
    -------
    None.

    """
    output = frequencies[::-1]
    
    df = pd.DataFrame(output[:numwords], columns = ["Words", "Frequencies"])
    df.to_csv(freqfile)
    
    return None
    
    
def ProcessSpeach(text):
    """
    Runs all the previous functions so our main function is readable
    
    Parameters
    ----------
    text : String
        Text of each speach.

    Returns
    -------
    array : List
        List of words that have gone through each function.

    """
    
    try:
        
        assert(type(text) == str)
        
    except AssertionError:
        
        warnings.warn(f"Expecting a string, recieved {type(text)} instead")
        
        raise TypeError
    
    text = Lowercase(text)
    text = RemovePunctuation(text)
    array = SplitText(text)
    array = Lemmatization(array)
    array = MeaninglessWords(array)
    

    
    return array
    
        
def RunEnglishText(debug = False):
    """
    Run whole processing pipeline, Main function.
    
    Parameters
    ----------
    debug : Boolian
        Used for testing the dataset so we dont run the whole text file every time.
        The default is False.

    Returns
    -------
    List
        List of touples from the dataset.

    """

    
    df = pd.read_csv('/Users/bashir_a1/Desktop/Internship/nlp-islamist-discourse/data/created/english_with_date.csv', index_col = False, sep = ',')
    
    bagofwords = []
    FrequencyDates = []
    random = "1"
    count = 1
    
    for i, row in df.iterrows():
        
        if i > 10 and debug == True:
            break
            
        
        if not pd.isna(row["Text"]):
            if type(row["Date_of_Publication"]) == str:
                FrequencyDates.append((row["Date_of_Publication"], ProcessSpeach(row["Text"]).count("lebanon")))
            else:
                FrequencyDates.append(("unknown" + random, ProcessSpeach(row["Text"]).count("lebanon")))
                count += 1
                random += str(count)
                #dropna function pandas
                #term freq over time
            
            bagofwords += ProcessSpeach(row["Text"])
            
        
    
    print(FrequencyGraph(FrequencyDates))



RunEnglishText(debug = True)
