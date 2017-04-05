#Author: Murtaza - Bass naam hi kafi hai
#steps python createXMLfile.py
#keep createXMLfile.py and quickSort.py in same folder
from xml.etree import ElementTree
import random
import sys
from threading import Thread, current_thread
#=========================================
def read_xml(file_path):
  doc = ElementTree.parse(file_path)
  root = doc.getroot()
  arr = []
  for value in root.iter('integer'):
	arr.append(int(value.attrib.values()[0]))
  return arr
#=========================================
def swap(arr,left,right):
	temp = arr[left]
	arr[left] = arr[right]
	arr[right] = temp
#=========================================
def partition(arr,low,high):
	try:
		left=low
		pivot = arr[low]
		right = high
		done = False
    		while not done:
        		while left <= right and arr[left] <= pivot:
            			left = left + 1
        		while arr[right] >= pivot and right >=left:
            			right = right -1
        		if right < left:
            			done= True
        		else:
				swap(arr,left,right)
		swap(arr,low,right)
	except IndexError:
		print ""
	return right
#=========================================
def quicksort(arr,low,high):
	if low<high:
    		pivot = partition(arr, low, high)
       		t =Thread(target = quicksort, args = (arr, low, pivot - 1))
       		t.start()
       		t.join()
       		t1=Thread(target = quicksort, args = (arr, pivot + 1, high))
       		t1.start()
       		t1.join()
  	return arr
#=========================================
arr = read_xml(sys.argv[1]);
arr1 = quicksort(arr, 0, len(arr)-1)
print arr1
#=========================================
