from xml.etree import ElementTree
import sys
from threading import Thread, current_thread

class quick:
    def read_xml(self,file_path):
      data = ElementTree.parse(file_path)
      root = data.getroot()
      arr = []
      for num in root.iter('integer'):
    	arr.append(int(num.attrib.values()[0]))
      return arr

    def swap(self,arr,first,second):
    	temp = arr[first]
    	arr[first] = arr[second]
    	arr[second] = temp

    def partition(self,arr,low,high):
    	pivot = arr[low]
    	self.left= low
    	self.right = high
    	while self.left<self.right:
    		while arr[self.left] < pivot:
        			self.left = self.left + 1
    		while arr[self.right] > pivot:
        			self.right = self.right -1
    		self.swap(arr,self.left,self.right)
    	return self.right

    def quicksort(self,arr,low,high):
        if low >= high:
            return
        self.pivot = self.partition(arr, low, high)
        t =Thread(target = self.quicksort, args = (arr, low, self.pivot - 1))
        t.start()
        t.join()
        t1=Thread(target = self.quicksort, args = (arr, self.pivot + 1, high))
        t1.start()
        t1.join()
        return arr

if __name__ == '__main__':
    obj = quick()
    arr = obj.read_xml(sys.argv[1]);
    result = obj.quicksort(arr, 0, len(arr)-1)
    print result
