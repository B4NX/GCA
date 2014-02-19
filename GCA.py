#import antigravity
import CA
from CAcrypto import *

def buildString(x:list):
    """Builds a string from a list"""
    thing = ""
    for i in x:
        try:
            thing+=str(i)
        except UnicodeEncodeError:
            thing+=chr(178)
    return thing

#TESTSEED = RandSeed(seedlen)
##TESTSEED = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#TESTMESSAGE = "The Quick Brown Fox Jumped Over the Lazy Dog"

#print("Enter a message to encrypt, leave blank for default message: ")
#mssg = input()

#if (mssg == ""):
#    mssg = TESTMESSAGE

#print(IntsToHex(MessageToInts(mssg)))
#enc = encryptMessage(mssg,TESTSEED,seedlen)
#print(enc)

#print(buildString(BinaryToChar(HexToBinary(decryptMessage(enc,TESTSEED,seedlen)))))

#print("Press enter to exit")
#input()