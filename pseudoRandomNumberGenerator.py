# Author: Khalid - naam toh suna hi hoga (heavily inspired from http://stackoverflow.com/questions/3062746)
# :~$ python yoyo.py

seed = 123456789 # any random number will do

a = 1103515245
c = 12345
m = pow(2,32)
# Linear Congruential Generator is the simplest & oldest
# for LCG, the values of a,c & m may be anything but for it's full potential (i.e. longest unrepeated sequence) ->
# c & m should be co-prime (means they have no common factor other than 1)
# (a-1) should be divisible by all prime factors of m
def LCG() :
    global seed # Python would otherwise create a local seed in the next statement instead of using the global seed
    seed = (a * seed + c) % m
    return seed

print("How many random numbers do you want ? ")
n = int(raw_input())
print("")
i = 0
while i<n :
    print(LCG())
    i = i + 1
print("")
