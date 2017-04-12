# Author: http://philosophyforprogrammers.blogspot.in/2011/05/booths-multiplication-algorithm-in.html
# Steps to run as a standalone program ->
# :~$ python yoyo.py
# To implement the client-server logic, make sure sha.py,client.py & server.py are in the same directory.
# Run server.py first and then run client.py
# IMPORTANT - bitstring module is needed for this code to run
# Install bitstring using the following command on terminal ->
# :~$ sudo pip install bitstring

from bitstring import BitArray

'''
   Returns m * r using Booth's algorithm.
   x = len(m) and y = len(r). Note that this is the length in base 2.

'''
def booth(m, r, x, y):
	# Initialize
	totalLength = x + y + 1
	mA = BitArray(int = m, length = totalLength)
	A = mA << (y+1)
	S = BitArray(int = -m, length = totalLength)  << (y+1)
	P = BitArray(int = r, length = y)
	P.prepend(BitArray(int = 0, length = x))
	P = P << 1
	print "Initial values"
	print "A", A.bin
	print "S", S.bin
	print "P", P.bin
	print "Starting calculation"
	for i in range(1,y+1):
		if P[-2:] == '0b01':
			P = BitArray(int = P.int + A.int, length = totalLength)
			print "P +  A:", P.bin
		elif P[-2:] == '0b10':
			P = BitArray(int = P.int +S.int, length = totalLength)
			print "P +  S:", P.bin
		P = arith_shift_right(P, 1)
		print "P >> 1:", P.bin
	P = arith_shift_right(P, 1)
	print "P >> 1:", P.bin
	return P.int

def arith_shift_right(x, amt):
	l = x.len
	x = BitArray(int = (x.int >> amt), length = l)
	return x

if __name__ == "__main__":
    print("")
