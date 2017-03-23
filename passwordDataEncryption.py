# Author: Khalid - naam toh suna hi hoga (heavily inspired from http://stackoverflow.com/questions/2490334)
# Steps to run ->
# :~$ python yoyo.py

import base64

def vigenereEncryptionUsedToMeanSomethingBackInTheDay(key,message) :
    cipherTextCharacters = []
    for i in range(len(message)) :
        keyForCurrentCharacter = key[(i % len(key))] # the % 'wraps' the key over the message repeatedly

        currentCipherTextCharacter = chr(ord(message[i]) + ord(keyForCurrentCharacter) % 256)
        # this is what the built-in functions chr() and ord() do ->
        # chr(97) returns 'a'
        # ord('a') returns 97
        # keep in mind that 'a' is a string of length = 1 and not chars

        cipherTextCharacters.append(currentCipherTextCharacter)
    cipherText = "".join(cipherTextCharacters) # combines the characters in the character array to form a string
    return cipherText
    # urlsafe_b64encode - standard encoding of the string so that it can be sent SAFELY as part of a URL/mail etc

def vigenereDecryptionUsedToMeanSomethingBackInTheDay(key,cipherText) :
    decryptedTextCharacters = []
    for i in range(len(cipherText)) :
        keyForCurrentCharacter = key[(i % len(key))]
        currentDecryptedTextCharacter = chr((256 + ord(cipherText[i]) - ord(keyForCurrentCharacter)) % 256) # observe the order of operations
        decryptedTextCharacters.append(currentDecryptedTextCharacter)
    decryptedText = "".join(decryptedTextCharacters)
    return decryptedText    # origial message so no need of urlsafe_b64encode

print("Enter your password (i.e. key) - ")
key = raw_input()
print("")
print("Enter your message to be encrypted - ")
message = raw_input()
print("")
print("This is the cipher text generated - which can totally not be cracked ;) - ")
cipherText = vigenereEncryptionUsedToMeanSomethingBackInTheDay(key,message)
gibberish = base64.urlsafe_b64encode(cipherText) # if cipherText is printed directly, you cannot see the actual characters
print(gibberish)
print("")
print("This is the decrypted message using your password which is supposed to match your original message - ")
decryptedText = vigenereDecryptionUsedToMeanSomethingBackInTheDay(key,cipherText)
print(decryptedText)
print("")
