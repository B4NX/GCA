#import antigravity
from random import *
import CA
from CAcrypto import *

letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '\\', '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?']

def buildString(x:list):
    """Builds a string from a list"""
    thing = ""
    for i in x:
        try:
            thing+=str(i)
        except UnicodeEncodeError:
            thing+=chr(178)
    return thing

def padMessage(mssg:str):
    mssgLen = len(mssg)
    front = 0
    back = 0
    charNeeded = 64 - mssgLen
    while True:
        front = randint(0,charNeeded)
        back = randint(0,charNeeded)
        if (front + back + mssgLen == 64):
            break
        else:
            continue
    tmp = getRandString(front) + mssg + getRandString(back)
    return tmp

def getRandString(len:int):
    tmp = ""
    for i in range(0,len):
        tmp+=random.choice(letters)
    return tmp

TESTSEED = RandSeed(seedlen)
#TESTSEED = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
TESTMESSAGE = "The Quick Brown Fox Jumped Over the Lazy Dog"

print("Enter a message to encrypt, leave blank for default message: ")
mssg = input()

if (mssg == ""):
    mssg = TESTMESSAGE

mssg=padMessage(mssg)

print(IntsToHex(MessageToInts(mssg)))
enc = encryptMessage(mssg,TESTSEED,seedlen)
print(enc)

print(buildString(BinaryToChar(HexToBinary(decryptMessage(enc,TESTSEED,seedlen)))))

print("Press enter to exit")
input()