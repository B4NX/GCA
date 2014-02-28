from random import SystemRandom
import time as pythonTime

import CAcrypto
import GCA
import datetime
import Test

from Test import randGen
from Test import letters


def writeOut(mssg:str, enc, dec, seed, steps):
    outfile = open("Data3.tsv",'a')
    time = pythonTime.strftime("%H:%M:%S",pythonTime.gmtime())
    outfile.write(time + "\t" + str(mssg) + "\t" + str(enc) + "\t" + str(dec) + "\t" + str(seed) + "\t" + str(steps) + "\n")
    outfile.close()

for i in range(0,28800):
    print(i)

    word = Test.getRandWord()
    wordList = list(word)

    seed = CAcrypto.RandSeed(256)
    steps = randGen.randint(75,125)

    enc = GCA.encrpytMessage(word,seed,steps)
    dec = GCA.decryptMessage(enc,seed,steps)
    
    writeOut(word,enc,dec,seed,steps)