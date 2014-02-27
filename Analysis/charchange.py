import re
import matplotlib.pyplot as plot

def getFrequencies():
    changevalues = []
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
            changevalues.append(msg[i] - hexes[i])
        line = infile.readline()
    infile.close()
    return changevalues

changev = getFrequencies()
plot.hist(changev, 512)
plot.ylabel("Occurences")
plot.xlabel("Displacement of character")
plot.title("Displacement of Character Values")
plot.show()
