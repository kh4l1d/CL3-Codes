# Author: Khalid - naam toh suna hi hoga
# Steps to run ->
# :~$ python yoyo.py

# we have to verify p,q,g and miller-rabin primality testing may be used
# so here's the deal -
# q must be - prime & 160bit in length
# p must be between 512 & 1024 bits in length and q should divide (p-1)
# g must be h raised to (p-1)/q % p where h is between 1 & p (usually h is taken as 2)
# you'll mostly get "False" as it's quite tough to get the ideal (p,q,g) tuple

import random

def numberOfBits(p):
    return (len(bin(p))-2)

def brutalPrime(n) :
    isPrime = True
    i = 2
    while (i < n/2) :   # RS Agarwal stuff - surprisingly i recalled it
        if n % i == 0 :
            isPrime = False
            return isPrime
        i = i + 1

    return isPrime

def pseudoPrimeMillerRabin(n) :
    k = 1000 # miller-rabin accuracy
    i = 0
    isProbablyPrime = True
    while i<k :
        randomCheck = random.randint(2,(n-2))
        if (n % randomCheck) == 0 :
            isProbablyPrime = False
            return isProbablyPrime
        i = i + 1

    return isProbablyPrime

print("")
print("Enter the parameter tuple (p,q,g) : ")
print("Enter value for p : ")
p = long(raw_input())
print("Enter value for q : ")
q = long(raw_input())
print("Enter value for g : ")
g = long(raw_input())
print("")
print("Here's how good the DSA tuple is -> ")
print("According to brute-force primality testing is q prime ?")
print(brutalPrime(q))
print("")
print("According to Miller-Rabin primality testing, q is most probably prime ?")
print(pseudoPrimeMillerRabin(q))
print("")
numberOfBitsOfQ = numberOfBits(q)
print("Is number of bits of q = 160 ?")
if numberOfBitsOfQ == 160 :
    print("True")
else :
    print("False")

print("")
print("Does q divide (p-1) ?")
if ((p-1) % q) == 0 :
    print("True")
else :
    print("False")

print("")
print("Is number of bits of p between 512 & 1024 ? ")
numberOfBitsOfP = numberOfBits(p)
if ((numberOfBitsOfP >= 512) and (numberOfBitsOfP <= 1024)) :
    print("True")
else :
    print("False")

print("")
print("Is g of the right form i.e. (h^((p-1)/q) mod p) where h = 2 ?")
h = 2
complexExponent = ((p-1) / q)
if (pow(h,complexExponent) % p) == g :
    print("True")
else :
    print("False")
print("")
