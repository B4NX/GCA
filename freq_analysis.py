import re

def getFrequencies():
    frequencies = [0 for i in range(256)]
    infile = open("results.tsv",'r')
    line = infile.readline()
    n = 0
    while (line != "" and n < 5):
        l = line.split("\t")
        enc = l[2]
        hexes = enc.split(":")
        hexes = [int(i, 16) for i in hexes]
        for i in range(len(hexes) - 1):
            frequencies[hexes[i]] += 1
        line = infile.readline()
    infile.close()
    return frequencies

def writeFrequencies(frequencies:list):
    outfile = open("freq.txt",'a')
    outfile.write(str(frequencies))
    outfile.close()

writeFrequencies(getFrequencies())