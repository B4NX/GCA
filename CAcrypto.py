#import antigravity
import CA, CAslice, random
from CAslice import Slice

seedlen = 256

def encryptMessage(message:str, seed, steps:int):
    global seedlen
    assert len(seed) > 20
    CA.r_initCA(seed, steps) #Start up the CA with the specified seed and steps
    m_data = ",".join(message).split(",") # get message as list instead of string
    m_data = [ord(i) for i in m_data]
    m_head = 0
    ca_m_head = 4
    ca_enc_head = seedlen // 2 - 4

    d = dlast = []

    while (CA.steps <= 0):
        dlast = d
        d = CA.update()
        if (d[ca_m_head] == 1):
            m_head += 1
            if (m_head >= len(m_data)):
                m_head = 0
        else:
            pass #don't move m_head
        b = "0b"
        r = d.range()
        for i in range(r[0] + ca_enc_head, r[0] + ca_enc_head + 8):
            b += str(d[i])
        m_data[m_head] = m_data[m_head] ^ int(b, 2)

    return str(["%02X"%(i) for i in m_data]).replace(", ",":").replace("\'","")[1:-1], d, dlast


def decryptMessage(message:str, seed, steps:int):
    assert len(seed) > 20
    CA.r_initCA(seed, steps) #Start up the CA with the specified seed and steps
    m_data = message.split(":") # get message as list instead of string
    m_data = [int(i, 16) for i in m_data]
    m_head = 0
    ca_m_head = 4
    ca_enc_head = seedlen // 2 - 4

    d = dlast = []
    while (CA.steps < 3):
        dlast = d
        d = CA.update()
        if (d[ca_m_head] == 1):
            m_head += 1
            if (m_head >= len(m_data)):
                m_head = 0
        else:
            pass #don't move m_head

    CA.rows = [d, dlast]
    CA.steps = -steps
    CA.init()

    while (CA.steps <= 0):
        dH = 0
        d = CA.update()
        CA.update_screen(d)
        if (d[ca_m_head] == 1):
            dH = -1
            if (m_head < 0):
                m_head = len(m_data) - 1
        else:
            dH = 0
        b = "0b"
        r = d.range()
        for i in range(r[0] + ca_enc_head, r[0] + ca_enc_head + 8):
            b += str(d[i])
        m_data[m_head] = m_data[m_head] ^ int(b, 2)
        m_head += dH

    #return str([chr(i) for i in m_data]).replace(", ","").replace("\'","")[1:-1]
    return str(["%02X"%(i) for i in m_data]).replace(", ",":").replace("\'","")[1:-1]

def HexToBinary(text:str):
    """Turns a string of hex into an array of binary numbers"""
    hexArray=text.split(":")
    binaryArray=[]
    for i in hexArray:
        binaryArray.append(int(i,16))
    return binaryArray

def BinaryToChar(nums:list):
    """Turns a list of binary numbers into an array of strings(chars)"""
    charArray=[]
    for n in nums:
        charArray.append(chr(n))
    return charArray
def RandSeed(len:int):
    """Returns a random seed of the specified length"""
    seed=[-1]*len
    for i in seed:
        i=random.randint(0,1)
    return seed

testSeed = RandSeed(128)
enc, d, dlast = encryptMessage("Hello world", testSeed, 100)
print(enc)
dec = decryptMessage(enc, testSeed, 100)
print(dec)
print(str(["%02X"%(ord(i)) for i in "Hello world"]).replace(", ",":").replace("\'","")[1:-1])
