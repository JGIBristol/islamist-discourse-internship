import pandas as pd
import camel_tools.tokenizers.word
from camel_tools.tokenizers.word import simple_word_tokenize
from camel_tools.tokenizers.word import normalize_unicode
from camel_tools.utils.normalize import normalize_alef_maksura_ar
from camel_tools.utils.normalize import normalize_alef_ar
from camel_tools.utils.normalize import normalize_teh_marbuta_ar
from camel_tools.utils.dediac import dediac_ar
from nltk.corpus import stopwords
import warnings
import pandas as pd
import matplotlib.pyplot as plt

def ArabicNormalize(text):
    """
    Use this function first, it normalizes arabic text for example makes the
    following changes:
    ﷺ    
صلى الله عليه وسلم    
    
    Parameters
    ----------
    text : String
        Unnormalized text.

    Returns
    -------
    String
        Normalized and removed Arabic diacritical marks.

    """
    try:
        
        assert(type(text) == str)
        
    except AssertionError:
        
        warnings.warn(f"Expecting a string, recieved {type(text)} instead")
        
        raise TypeError
        
    norm = normalize_unicode(text)
    
    return dediac_ar(text)


def OrthographicNormalize(text):
    """
    Normalizes different variations of the same text e.g in arabic there are 
    different variations of the word alef

    Parameters
    ----------
    text : String
        String of text of the different variations of words.

    Returns
    -------
    String.
        Normalized text
    """
    try:
        
        assert(type(text) == str)
        
    except AssertionError:
        
        warnings.warn(f"Expecting a string, recieved {type(text)} instead")
        
        raise TypeError
    
    # Normalize alef variants to 'ا'
    text1 = normalize_alef_ar(text)
    
    # Normalize alef maksura 'ى' to yeh 'ي'
    text2 = normalize_alef_maksura_ar(text1)
    
    # Normalize teh marbuta 'ة' to heh 'ه'
    return normalize_teh_marbuta_ar(text2)



    

def ArabicSplitText(text):
    """
    Splits the text into words

    Parameters
    ----------
    text : String
        String of arabic text.

    Returns
    -------
    List
        list of words.

    """
    try:
        
        assert(type(text) == str)
        
    except AssertionError:
        
        warnings.warn(f"Expecting a string, recieved {type(text)} instead")
        
        raise TypeError
        
    return simple_word_tokenize(text)




def ArabicStopwords(array):
    """
    A function that takes in a list of words and outputs the same list of words
    but removes the meaningless words we dont want

    Parameters
    ----------
    array : List
        list of words.

    Returns
    -------
    List
        List of words with meaningless words removed.

    """
    try:
        
        assert(type(array) == list)
        
    except AssertionError:
        
        warnings.warn(f"Expecting a array, recieved {type(array)} instead")
        
        raise TypeError
        
    stopwords_list = stopwords.words('arabic')
    
    return [i for i in array if i not in stopwords_list]



def ArabicFrequency(array):
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
    try:
        
        assert(type(array) == list)
        
    except AssertionError:
        
        warnings.warn(f"Expecting a array, recieved {type(array)} instead")
        
        raise TypeError
    
    UniqueWords = {i : 0 for i in array}
        
    return sorted([(i, array.count(i)) for i in UniqueWords], key = lambda x : x[1])
    

def ArabicFrequencyGraph(frequency, graphfile, numwords = 20):
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
    plt.savefig(graphfile, bbox_inches='tight')
    plt.xlabel("words")
    plt.ylabel("words count")
    
    return None


def ArabicProcessSpeach(text):
    try:
        
        assert(type(text) == str)
        
    except AssertionError:
        
        warnings.warn(f"Expecting a string, recieved {type(text)} instead")
        
        raise TypeError
    
    
    
    return None


def ArabicRunText(debug = False):
    
    
    df = pd.read_csv('/Users/bashir_a1/Desktop/Internship/nlp-islamist-discourse/data/original/arabic_corpus.csv', index_col = False, sep = ',')
    
    
    
    bagofwords = []
    for i, row in df.iterrows():
        if i > 10 and debug == True:
            break
            
        
        if not pd.isna(row["Text"]):
            
            bagofwords += ArabicProcessSpeach(row["Text"])
            
            