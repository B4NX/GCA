from random import SystemRandom
import CAcrypto
import GCA
import datetime

letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '\\', '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?']

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
    outfile = open("results.tsv",'a')
    time=str(datetime.datetime.now())
    outfile.write(time+"\t"+str(mssg)+"\t"+str(enc)+"\t"+str(dec)+"\t"+str(seed)+"\t"+str(steps)+"\n")
    outfile.close()

for x in range(0,5):
    print(x)
    mssg=getRandWord()
    seed=CAcrypto.RandSeed(256)
    steps=randGen.randint(75,125)
    enc=GCA.EncryptMessage(mssg,seed,steps)
    dec=GCA.DecryptMessage(enc,seed,steps)
    writeOut(mssg,enc,dec,seed,steps)

print("All done.")
