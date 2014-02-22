import random
import CA
from CAcrypto import *
from GCA import *

letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '\\', '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?']

def getRandWord():
    word = ""
    len = random.randint(1,100)
    for i in range(len):
        word+=letters[random.randint(0,31)]
        
    return word

def makeString(charArray:list):
    mssg=""
    for i in charArray:
        mssg+=i
    return mssg

correct = 0
total = 0

for n in range(1,2^256):
    word = getRandWord()
    seed = RandSeed(256)

    enc = encryptMessage(word,seed,256)

    dec = decryptMessage(enc,seed,256)

    #print(word)
    x=HexToBinary(dec)
    x=BinaryToChar(x)
    #print(makeString(x))
    if (word == buildString(BinaryToChar(HexToBinary(dec)))):
        correct+=1
    total+=1

print(str(correct) + " correct out of " + str(total))
print(str(correct / total) + "%")