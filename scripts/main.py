#Run all english test and create two outputs, csb file of frequency of the words
# and graph of the top 20 most common words
#Time it

import time 
import englishprocessing

starttime = time.time()

frequencies = englishprocessing.RunEnglishText(debug = True)

englishprocessing.FrequencyGraph(frequencies, graphfile = "../fig/frequenciesgraph.png")

englishprocessing.outputfrequencies(frequencies, freqfile = "../data/created/frequencies_100.csv")

endtime = time.time()

print(f"Time taken to run = {endtime - starttime:.2f} seconds")
