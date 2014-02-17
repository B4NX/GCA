#import antigravity
import CA

def encryptMessage(message:str, seed, steps:int):
    assert len(seed) > 20
    CA.r_initCA(seed, steps) #Start up the CA with the specified seed and steps
    m_data = ",".join(message).split(",") # get message as list instead of string
    m_data = [ord(i) for i in m_data]
    m_head = 0
    ca_m_head = 4
    ca_enc_head = len(seed) - 9

    while (CA.steps <= 0):
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

    return str(["%02X"%(i) for i in m_data]).replace(", ",":").replace("\'","")[1:-1]
#def decryptMessage(message, seed, steps):
testSeed = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1]
print(encryptMessage("Hello world", testSeed, 100))
print(str(["%02X"%(ord(i)) for i in "Hello world"]).replace(", ",":").replace("\'","")[1:-1])