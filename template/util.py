from array import array
import binascii


def die(msg):
    print("\tERROR: " + msg)
    exit(-1)

def bytes(str):
    return array('B', str)

def obscure(password, pad):
    #password_bytes = bytes(password)
    #pad_bytes = bytes(pad)
    #passw0rd_bytes = xor(password_bytes, pad_bytes)
    #passw0rd = binascii.b2a_base64(passw0rd_bytes)
    #print passw0rd
    return password

def deobscure(passw0rd, pad):
    #passw0rd_bytes = binascii.a2b_base64(passw0rd)
    #pad_bytes = bytes(pad)
    #password_bytes = xor(passw0rd_bytes, pad_bytes)
    #password = binascii.b2a_(password_bytes)
    return passw0rd

def xor(ba1, ba2):
    out = []
    if len(ba1) > len(ba2):
        a = ba1
        b = ba2
    else:
        a = ba2
        b = ba1
    for i, byte1 in enumerate(a):
        byte2 = b[i] if len(b) > i else 0xff
        xbyte = byte1 ^ byte2
        out.append(xbyte)
    print out
    return out
