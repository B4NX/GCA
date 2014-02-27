import re
import matplotlib.pyplot as plot
import numpy as np

def getFrequencies():
    changevalues = []
    frequencies = [[i, 0] for i in range(400)]
    infile = open("Frequency_results.tsv",'r')
    line = infile.readline()
    n = 0
    while (line != "" and n < 5):
        l = line.split("\t")
        msg = l[1]
        msg = list(msg)
        msg = [ord(i) for i in msg]
        enc = l[2]
        hexes = enc.split(":")
        hexes = [int(i, 16) for i in hexes]
        for i in range(len(hexes) - 1):
            change = hexes[i] - msg[i]
            changevalues.append(change)
            frequencies[change + 150][1] += 1
        line = infile.readline()
        #print("\n")
        #n += 1
    infile.close()
    return changevalues, frequencies

def writeFrequencies(frequencies):
    outfile = open("charchange.txt",'w')
    outfile.seek(0)
    outfile.write(str([[i - 150, frequencies[i]] for i in range(len(frequencies))]))
    outfile.write("\n")
    outfile.write("\nMean: " + str(np.mean(frequencies)))
    outfile.write("\nMedian: " + str(np.median(frequencies)))
    outfile.close()

changev, freq = getFrequencies()
writeFrequencies([freq[i][1] for i in range(len(freq))])
fig = plot.figure(3, (8, 5), 300)
plot.hist(changev, 1024, color='black')
plot.ylabel("Occurences")
plot.xlabel("Displacement of character")
plot.title("Displacement of Character Values")
#plot.show()
fig.savefig("figure-3.png", dpi=300)
