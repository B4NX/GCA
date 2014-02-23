import random
import CAcrypto
from CAcrypto import *
import datetime


def intify(bits:list):
    num = 0
    for i in range(len(bits)):
        num += 2**i * bits[len(bits) - i - 1]
    return num

def writeOut(mssg, enc, dec, seed, steps):
    outfile = open("results_integral.tsv",'a')
    time=str(datetime.datetime.now())
    outfile.write(time+"\t"+mssg+"\t"+str(enc)+"\t"+str(dec)+"\t"+str(seed)+"\t"+str(steps)+"\n")
    outfile.close()

messagePart1 = [intify([random.randint(0, 1) for i in range(8)]) for i in range(24)]
presetSeed = RandSeed(256)

for x in range(0,10):
    print(x)
    mssg=messagePart1 + [intify([random.randint(0, 1) for i in range(8)]) for i in range(8)]
    seed=presetSeed
    steps=512
    enc=Encrypt(mssg,seed,steps)
    dec=Decrypt(enc,seed,steps)
    writeOut(IntsToHex(mssg), IntsToHex(enc), IntsToHex(dec),seed,steps)

print("All done.")
