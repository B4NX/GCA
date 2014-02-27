from random import SystemRandom
import time as pythonTime

import CAcrypto
import GCA
import datetime
import Test

from Test import randGen
from Test import letters


for i in range(0,10):
    print(i)

    word = Test.getRandWord()
    wordList = list(word)

    seed = CAcrypto.RandSeed(256)
    steps = randGen.randint(75,125)

    enc = GCA.encrpytMessage(word,seed,steps)

    x=CAcrypto.HexToBinary(enc)
    tmp=CAcrypto.BinaryToChar(x)

    print(tmp)