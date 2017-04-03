#Author: Murtaza - Bass naam hi kafi hai
from threading import Thread

def sort(x,l):
	for i in range(l, len(x)-1, 2):
			if x[i] > x[i+1]:
				x[i], x[i+1] = x[i+1], x[i]
				sorted = False
			if x[i] == x[i+1]:
				i+=2
def oddevensort(x):
	sorted = False
	while not sorted:
		sorted = True
		t =Thread(target = sort(x,0)) # for even
		t1 =Thread(target = sort(x,1)) # for odd
		t.start()
		t1.start()
		t.join()
		t1.join()
	for i in range(0,len(x)-1):
		if x[i]<=x[i+1]:
			sorted = False
		else:
			x=oddevensort(x)
	return x
