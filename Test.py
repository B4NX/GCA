from random import SystemRandom
import CAcrypto
import GCA
import datetime

letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '\\', '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?']

outfile = open("results.csv",'a')

randGen=SystemRandom()

def getRandWord():
    word = ""
    len= randGen.randint(1,100)
    for i in range(len):
        word+=letters[randGen.randint(0,31)]
        
    return word

def makeString(charArray:list):
    mssg=""
    for i in charArray:
        mssg+=i
    return mssg

def writeOut(mssg:str, enc, dec, seed, steps):
    outfile = open("results.csv",'a')
    time=str(datetime.datetime.now())
    outfile.write(str(mssg)+"\t"+str(enc)+"\t"+str(dec)+"\t"+str(seed)+"\t"+str(steps))
    outfile.close()

for x in range(0,1000):
    mssg=getRandWord()
    seed=CAcrypto.RandSeed(256)
    steps=randGen.randint(75,125)
    enc=GCA.EncryptMessage(mssg,seed,100)
    dec=GCA.DecryptMessage(enc,seed,100)
    writeOut(mssg,enc,dec,seed,100)

print("All done.")