import os, random
filename = raw_input("Enter the filename: ")+".xml"
file = open(filename,'w')
file.write("<Numbers>\n")
for i in range(10):
	file.write("\t<integer num = \""+str(random.randint(0,800))+"\" ></integer>\n")
file.write("</Numbers>\n")
file.close()
if(input("press 1 to see its contents:")==1):
	os.system("cat "+filename)
	if(input("press 2 to run quicksort")==2):
		os.system("python quicksort.py "+filename)
