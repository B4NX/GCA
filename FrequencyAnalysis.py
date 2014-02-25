from random import SystemRandom
import time as pythonTime

import CAcrypto
import GCA
import datetime
import Test

from Test import randGen
from Test import letters

def writeOut(wordl:list, enc, seed, steps):
    outfile = open("Frequency_results.tsv",'a')
    time=pythonTime.strftime("%H:%M:%S",pythonTime.gmtime())
    outfile.write(time + "\t" + str(wordl) + "\t" + str(enc) + "\t" + str(seed) + "\t" + str(steps) + "\n")
    outfile.close()

for i in range(0,864000):
    print(i)

    word = Test.getRandWord()
    wordList = list(word)

    seed = CAcrypto.RandSeed(256)
    steps = randGen.randint(75,125)

    enc = GCA.encrpytMessage(word,seed,steps)

    writeOut(wordList,enc,seed,steps)

time=pythonTime.strftime("%H:%M:%S",pythonTime.gmtime())
print("All done at: "+time)