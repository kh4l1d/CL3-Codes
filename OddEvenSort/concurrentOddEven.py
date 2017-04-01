#Author: Murtaza - Bass naam hi kafi hai
from threading import Thread

def even(x):
	for i in range(0, len(x)-1, 2):
			if x[i] > x[i+1]:
				x[i], x[i+1] = x[i+1], x[i]
				sorted = False
def odd(x):
	for i in range(1, len(x)-1, 2):
			if x[i] > x[i+1]:
				x[i], x[i+1] = x[i+1], x[i]
				sorted = False

def oddevensort(x):
	sorted = False
	while not sorted:
		sorted = True
		t =Thread(target = even(x))
		t1 =Thread(target = odd(x))
		t.start()
		t1.start()
		t.join()
		t1.join()
	for i in range(0,len(x)-1):
		if x[i]<x[i+1]:
			sorted = False
		else:
			x=oddevensort(x)
	return x
