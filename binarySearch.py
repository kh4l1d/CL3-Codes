# Author: Khalid - naam toh suna hi hoga
# Steps to run ->
# :~$ python yoyo.py

def bubbleSort(a,n) :
    i = 0
    while i < n :
        j = i + 1
        while j < n :
            if a[i] > a[j] :
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
            j = j + 1
        i = i + 1

print("Enter size of array : ")
n = int(input())
print("Enter unsorted elements of array : ")
a = [] # take care - python doesn't have arrays (lists are used instead)
i = 0
while i<n :
    a.append(int(input()))
    i = i + 1

# a.sort() # sort is built-in for lists - a better option is sorted
# since size matters, a bubbleSort function is added but a.sort() is more optimal
bubbleSort(a,n)


print("Enter number to be searched : ")
key = int(input())
left = 0
right = n - 1
mid = (left + right) // 2 # Floor Division

if key not in a:
    print("Key is absent !")
else:
    while left <= right :
        if a[mid] == key :
            print("Key was found at position = " + str(mid+1))
            break
        elif a[mid] < key :
            left = mid + 1
        else :
            right = mid - 1

        mid = (left + right) // 2 # Floor Division 

    
