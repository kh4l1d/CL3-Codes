#Author: Murtaza - Bass naam hi kafi hai
#steps python 8q.py
#keep 8q.py and 8q.joson in same folder 
import json
N=8
queens = [-1,-1,-1,-1,-1,-1,-1,-1]
def isValid(col,row):
	for i in range(col):
		if(queens[i] == row):
			return False
	for i in range(col):
		if(abs(col-i) == abs(row-queens[i])):
			return False
	return True
			
def place(n):
	placed = False;
	for i in range(N):
		if(isValid(n,i)):
			queens[n] = i
			placed=True
			break

	if(not placed): 
		return False
		
	if( n == (N-1)):
		return True
		
	while(not place(n+1)):
		placed =  False
		for i in range(queens[n]+1,N):
			if(isValid(n,i)):
				queens[n] = i
				placed=True;
				break		
		if(not 	placed):
			return False
	return True

inputFile = open("8queens.json")
data = json.loads(inputFile.read())

data=data["matrix"]
for i in data:
	print(i)
print "\n"
for i in range(0,N):
	if(data[i][0] == 1):
		queens[0] = i
place(1)

print queens
print "\n"
outfile = open("out.json","w")
data = {}
matrix = [[],[],[],[],[],[],[],[]]

for i in range(0,N) :
	for j in range(0,N):
		if(queens[j] == i):
			matrix[i].insert(j,1)
		else:
			matrix[i].insert(j,0)
			
data["matrix"] = matrix
json.dump(data,outfile)
for i in matrix:
	print(i)
	
