#Author: Murtaza - Bass naam hi kafi hai
from threading import Thread
sorted = False 							#change num 1
def sort(x,l):
	global sorted 						#change num 2
	for i in range(l, len(x)-1, 2):
			if x[i] > x[i+1]:
				x[i], x[i+1] = x[i+1], x[i]
				sorted = False
			'''if x[i] == x[i+1]:			Change num 3
				i+=2'''
def oddevensort(x):
	global sorted						#Change num 4
	sorted = False
	while not sorted:
		sorted = True
		t =Thread(target = sort(x,0)) # for even
		t1 =Thread(target = sort(x,1)) # for odd
		t.start()
		t1.start()
		t.join()
		t1.join()
	'''for i in range(0,len(x)-1):				Change num 5 
		if x[i]<=x[i+1]:
			sorted = False
		else:
			x=oddevensort(x)'''
	return x
