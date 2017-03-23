# Author: https://en.wikipedia.org/wiki/SHA-1
# Steps to run as a standalone program ->
# :~$ python yoyo.py
# To implement the client-server logic, make sure sha.py,client.py & server.py are in the same directory.
# Run server.py first and then run client.py

def chunks(bits,chunkSize) :
    return [bits[i:i+chunkSize] for i in range(0, len(bits), chunkSize)]    # slice & dice

def rotateLeft(bits,positions) :
    return ((bits << positions) | (bits >> (32 - positions))) & 0xffffffff  # apparently this how it's done

def shaDigest(data) :

    # slices of the digest
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE # reverse of h1
    h3 = 0x10325476 # reverse of h0
    h4 = 0xC3D2E1F0 # end pairings

# so first things first we need to get the input characters -> int form -> bit form
    bitFormOfData = ""
    for c in range(len(data)) :
        bitFormOfData = bitFormOfData + '{0:08b}'.format(ord(data[c]))
        # ord does this -> ord('a') returns 97
        # the {0:08b} formats it into 8 bits so 9 is 00001001 instead of 1001

    originalBitFormOfData = bitFormOfData   # needed later for appending
    bitFormOfData = bitFormOfData + "1" # for some strange reason, 1 is appended

    # now we need to pad 0's till len(bitFormOfData) = 448 mod 512
    while ((len(bitFormOfData) % 512) != 448) :
        bitFormOfData = bitFormOfData + "0"

    # appending original message so length of it would be an exact multiple of 512
    # also format it to 64-bit representation
    bitFormOfData = bitFormOfData + '{0:064b}'.format(len(originalBitFormOfData))


    # essentially, this is what's being done ->
    # break bitFormOfData into 512 slices
    # break 32 bit slices from a single 512 bit slice - this is our word
    # effectively, we are TRANSFORMING each 32-bit word into a 80-bit list (i dunno why)
    # now operations will be done on this 80-bit list called w
    for c in chunks(bitFormOfData , 512) : # c is a slice of 512 bits from bitFormOfData
        words = chunks(c,32) # words is a slice of 32 bits from c => there will be 16 such slices
        w = [0] * 80 # w = [0,0,0,0,0,.........(80 times)] -> it's a list

        for n in range(0,16) :
            w[n] = int(words[n] , 2) # prototype of int(x,base = 10) , here base = 2 for binary

        for i in range(16,80) :
            w[i] = rotateLeft((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1) # ^ is for XOR

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        # the k values could be anything (but the receiver should also have the same ones in a digital signature scenario)
        for i in range(0,80) :
            if (0 <= i <= 19) :
                f = b ^ c ^ d   # f here is a function
                k = 0x5A827999  # could be anything
            elif (20 <= i <= 39) :
                f = b ^ c ^ d   # the idea is that for each range there will be a different f
                k = 0x6ED9EBA1  # could be anything
            elif (40 <= i <= 59) :
                f = b ^ c ^ d   # f could be b ^ c & d OR !c ^ d - or whatever
                k = 0x8F1BBCDC  # could be anything
            elif (60 <= i <= 79) :
                f = b ^ c ^ d   # lazy much,hence same function everywhere
                k = 0xCA62C1D6  # could be anything

            temp = rotateLeft(a, 5) + f + e + k + w[i] & 0xffffffff
            e = d
            d = c
            c = rotateLeft(b , 30)
            b = a
            a = temp

        h0 = h0 + a
        h1 = h1 + b
        h2 = h2 + c
        h3 = h3 + d
        h4 = h4 + e

    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

if __name__ == "__main__": # so that it can be imported
    print("Enter a message : ")
    message = raw_input()
    print("")
    digest = shaDigest(message)
    print("It's SHA-1 digest is -> ")
    print(digest)
    print("")
