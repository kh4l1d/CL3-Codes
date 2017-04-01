#Author - Murtaza - Bass naam hi kafi hai
# Steps to run ->  
# python yoyo.py

#from multiprocessing.dummy import Pool as ThreadPool
#pool = ThreadPool(4)

#a = []
#print("")
#print("Enter number of elements in array : ")
#n = int(input())
#print("")
#print("Enter all numbers : ")
#i = 0
#w#hile i<n :
#    a.append(int(input()))
#    i = i + 1

from threading import Thread, current_thread

def oddEvenSort(a,n) :
    isSorted = False

    while(isSorted == False) :
        isSorted = True
# for the odd guys
        i = 1
        while i <= (n-2) :
            if a[i] > a[i+1] :
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                isSorted = False
            i = i + 2
# for the even guys
        i = 0
        while i <= (n-2) :
            if a[i] > a[i+1] :
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                isSorted = False
            i = i + 2

#results = pool.map(oddEvenSort(a,n))
#oddEvenSort(a,n)
#print(a)
#print("")

def main(a,n) :
    t = Thread(target = oddEvenSort, args = (a,n))
    t.start()
    t.join()
