#import antigravity
import CA, CAslice, testCA, random
from CAslice import Slice

seedlen = 266

debug = open('debug.log', 'w')

def encryptMessage(message:str, seed, steps:int):
    global seedlen, debug
    assert len(seed) > 20
    CA.r_initCA(seed, steps) #Start up the CA with the specified seed and steps
    m_data = MessageToInts(message)
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
        DumpCurrentRow(CA.steps, m_head, m_data, ca_m_head, d, b)
    debug.write("\n\n\n")
    return IntsToHex(m_data)

def decryptMessage(message:str, seed, steps:int):
    assert len(seed) > 20
    CA.r_initCA(seed, steps) #Start up the CA with the specified seed and steps
    m_data = message.split(":") # get message as list instead of string
    m_data = [int(i, 16) for i in m_data]
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
        debug.write("mhead: " + str(m_head) + "\tdelta mhead: " + str(d[ca_m_head]) + "\n")
    debug.write("\n\n\n")
    CA.rows = [d, dlast]
    CA.steps = -steps
    #CA.init() # starts the pygame window

    ##Todo: refactor these two runs into the below code to maximize reuse
    for n in (d, dlast):
        dH = 0
        #CA.update_screen(d) # updates the pygame window
        if (n[ca_m_head] == 1):
            dH = -1
            if (m_head < 0):
                m_head = len(m_data) - 1
        else:
            dH = 0
        b = "0b"
        r = n.range()
        for i in range(r[0] + ca_enc_head, r[0] + ca_enc_head + 8):
            b += str(n[i])
        m_data[m_head] = m_data[m_head] ^ int(b, 2)
        m_head += dH
        debug.write("d\t")
        DumpCurrentRow(CA.steps, m_head, m_data, ca_m_head, d, b)

    while (CA.steps <= -2):
        dH = 0
        d = CA.update()
        #CA.update_screen(d) # updates the pygame window
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
        DumpCurrentRow(CA.steps, m_head, m_data, ca_m_head, d, b)
    debug.close()
    return IntsToHex(m_data)

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

def MessageToInts(message:str):
    return [ord(i) for i in list(message)]

def IntsToHex(nums:list):
    return str(["%02X"%(i) for i in nums]).replace(", ",":").replace("\'","")[1:-1]

def RandSeed(len:int):
    """Returns a random seed of the specified length"""
    seed=[random.randint(0, 1) for i in range(len)]
    return seed

def DumpCurrentRow(steps:int, m_head:int, m_data:list, ca_m_head:int, d:Slice, b:str):
    debug.write(str(steps))
    debug.write("\t" )
    for i in range(len(m_data)):
        if (i == m_head):
            debug.write(str(("__" + str(m_data[i]) + "__")))
        else:
            debug.write("  " + str(m_data[i]) + "  ")
        if (i != len(m_data) - 1):
            debug.write(", ")
    debug.write("\t\t")
    debug.write(b)
    debug.write("\t")
    debug.write(str(d[ca_m_head]))
    debug.write("\n")
#testSeed =  RandSeed(seedlen)
#enc, d, dlast = encryptMessage("Hello world", testSeed, 100)
#print(enc)
#dec = decryptMessage(enc, testSeed, 100)
#print(BinaryToChar(HexToBinary(dec)))
