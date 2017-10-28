# CL3-Codes
Instructions and solutions to common issues (please read) ->
--------------------------------------------------------------------------------------------------------------------------------
### Downloading :wink:

1. Say you want to download the binarySearch.py file through the terminal, just enter in the following command: 

```
wget https://raw.githubusercontent.com/kh4l1d/CL3-Codes/master/binarySearch.py
```
       

2. It's of the form: 

```
wget URL/file.txt
```

3. Although it is worth mentioning that repos should ideally be "git clone"-d like this: https://www.youtube.com/watch?v=oDUOWC4yib0

```
git clone https://github.com/kh4l1d/CL3-Codes.git
```

### Other similar works ->

1. BE Sem1 CL1-Codes -> https://github.com/kh4l1d/CL1-Codes

2. TE Sem1 & Sem2 (Download link) -> https://www.dropbox.com/s/jlsz28bgrpkx7us/Khalid%27s%20Third%20Year.zip?dl=0

3. SE Sem1 & Sem2 (Download link) -> https://www.dropbox.com/s/158agkqibt2cgoh/Khalid%27s%20Second%20Year.zip?dl=0

--------------------------------------------------------------------------------------------------------------------------------
### quickSort.py

1. Keep the files createXMLfile.py and quickSort.py in the same directory.

2. Simply run createXMLfile.py and you're done.

--------------------------------------------------------------------------------------------------------------------------------
### passwordDataEncryption.py

1. The syllabus vaguely mentions "encryption method overloading" - now I've searched online for this and found no results. I'm assuming this is a mis-print. However if you find a reasonable meaning to it (apart from function overloading), then please do notify me.

2. Python offers rich libraries (such as pycrypto) for a variety of encryption functions - but since here at SPPU we love re-inventing the wheel, the functions have been hard-coded.

--------------------------------------------------------------------------------------------------------------------------------
### pseudoRandomNumberGenerator.py (and SHA-1)

1. Ideal PRNGs like https://en.wikipedia.org/wiki/Mersenne_Twister requires one to learn specific numbers & positions for it to be effective - just see the diagram in the wiki and you'll know what I mean. Thus, only simple PRNGs will be coded as and when encountered.

2. For the practical exam, if you get this code, you will have to probably club it with the SHA-1 code. Head to the SHA-1+PRNG directory. It's essentially the same code as SHA-1, the only difference being that the value of k (in SHA-1) is randomly generated for each session.

3. Steps for the SHA-1+PRNG code are simple. First create a blank file called "randomKeyForSession.txt" and then run "generateRandomKeyForSession.py". This will generate a random number and store it in the text file. Then normally run your server and client codes.

![alt tag](https://i.stack.imgur.com/ZWHjC.gif)

--------------------------------------------------------------------------------------------------------------------------------
### trigonometryCalculatorActivity.java

![alt tag](https://github.com/kh4l1d/CL3-Codes/blob/master/trigonometryCalculatorPic.png)

--------------------------------------------------------------------------------------------------------------------------------
### Booths

1. For this code to run, it's necessary to install a Python module called bitstring - which greatly simplifies tasks such as 2's complement. It can be installed by the following command : 

```
sudo pip install bitstring
```
       

2. If you don't have pip installed (it doesn't come bundled with some Python versions), install pip by the following commands :

```
sudo apt-get install python-setuptools
sudo easy_install pip
```

--------------------------------------------------------------------------------------------------------------------------------
### Plagiarism

1. For this code to run, it's necessary to install a Python module called flask - which is a micro web framework for Python. It can be installed by the following command : 

```
sudo pip install Flask
```
       

2. If you don't have pip installed (it doesn't come bundled with some Python versions), install pip by the following commands :

```
sudo apt-get install python-setuptools
sudo easy_install pip
```

3. Simply run plagiarismChecker.py and then open the browser at 127.0.0.1:5000
--------------------------------------------------------------------------------------------------------------------------------
### diningPhilosopher.py

1. For this code to run, it's necessary to install a Python module called pymongo - which basically connects our MongoDB to our python code. It can be installed by the following command : 

```
sudo pip install pymongo
```
       

2. If you don't have pip installed (it doesn't come bundled with some Python versions), install pip by the following commands :

```
sudo apt-get install python-setuptools
sudo easy_install pip
```

3. MongoDB needs to be installed for this code to work. If the mongo shell doesn't open when you enter 'mongo' in the terminal, it's probably because the MongoDB daemon is not started. To resolve this, enter :
       
```
sudo service mongod start
```

--------------------------------------------------------------------------------------------------------------------------------
### Plagiarism & OddEvenSort

1. Both of these codes require a web application and as such Flask (a Python module has been used). To see the output on the browser at 127.0.0.1:5000 you HAVE to create a folder named "templates" and store the html files in it. Flask searches for html files to be rendered in a "templates" folder and if there isn't one, nothing would be displayed.
`
--------------------------------------------------------------------------------------------------------------------------------
