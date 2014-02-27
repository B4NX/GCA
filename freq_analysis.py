import re
import matplotlib.pyplot as plot

def getFrequencies():
    frequencies = [[i, 0] for i in range(256)]
    infile = open("Frequency_results.tsv",'r')
    line = infile.readline()
    n = 0
    while (line != "" and n < 5):
        l = line.split("\t")
        enc = l[2]
        hexes = enc.split(":")
        hexes = [int(i, 16) for i in hexes]
        for i in range(len(hexes) - 1):
            frequencies[hexes[i]][1] += 1
        line = infile.readline()
    infile.close()
    return frequencies

def writeFrequencies(frequencies):
    outfile = open("freq.txt",'a')
    outfile.write(str(frequencies))
    outfile.close()

print(getFrequencies())
plot.hist(getFrequencies())
plot.ylabel("Occurences")
plot.xlabel("ASCII value of character")
plot.title("Histogram of character frequencies")
plot.show()
