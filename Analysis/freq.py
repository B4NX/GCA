import re
import matplotlib.pyplot as plot

def getFrequencies():
    hexvalues = []
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
            hexvalues.append(hexes[i])
            frequencies[hexes[i]][1] += 1
        line = infile.readline()
    infile.close()
    return hexvalues, frequencies

def writeFrequencies(frequencies):
    outfile = open("freq.txt",'a')
    outfile.write(str(frequencies))
    outfile.close()

hexv, freq = getFrequencies()
writeFrequencies(freq)
fig = plot.figure(3, (8, 5), 300)
plot.hist(hexv, 256, color='black')
plot.ylabel("Occurences")
plot.xlabel("ASCII value of character")
plot.title("Histogram of character frequencies")
plot.show()
fig.savefig("figure-2.png", dpi=300)
