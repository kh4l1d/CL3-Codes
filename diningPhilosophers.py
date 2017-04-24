# Author: https://github.com/djunderw/dining-philosophers/blob/master/dining-philosophers.py
# Steps to run ->
# :~$ python yoyo.py

from pymongo import MongoClient
client = MongoClient()

import sys,threading,time

db = client.diningPhilosophers # the name of the database
collection = db.diningPhilosophersCollection # name of the collection


doc0 = {
"number" : 0,
"name" : "Descartes",
"thought" : "A donut's hope proves it's existence."
}
doc1 = {
"number" : 1,
"name" : "Marx",
"thought" : "Everybody desires donuts."
}
doc2 = {
"number" : 2,
"name" : "Aristotle",
"thought" : "A donut contains it's donut-ness."
}
doc3 = {
"number" : 3,
"name" : "Hume",
"thought" : "Donuts exist because I imagine donuts."
}
doc4 = {
"number" : 4,
"name" : "Nietzsche",
"thought" : "Stop at nothing to get your donut."
}

doc_id = collection.insert_one(doc0) # the variable doc_id is not needed
doc_id = collection.insert_one(doc1)
doc_id = collection.insert_one(doc2)
doc_id = collection.insert_one(doc3)
doc_id = collection.insert_one(doc4)


#doc1_id = collection.insert_one(doc1)

#doc2 = collection.find_one({"number" : 1})
#print(doc2)

#myValues[i] = bla['value'] # getting specific value from a document


class Semaphore(object):
    def __init__(self, initialAmountOfChopSticks):
        self.lock = threading.Condition(threading.Lock())
        self.chopSticksAvailable = initialAmountOfChopSticks

    def up(self):
        with self.lock:
            self.chopSticksAvailable += 1
            self.lock.notify()

    def down(self):
        with self.lock:
            while self.chopSticksAvailable == 0:
                self.lock.wait()
            self.chopSticksAvailable -= 1

class ChopStick(object):
    def __init__(self, chopStickId):
        self.chopStickId = chopStickId           # chop stick ID
        self.philosopherId = -1                 # keep track of philosopher using it
        self.lock = threading.Condition(threading.Lock())
        self.chopStickTaken = False

    def take(self, philosopherId):         # used for synchronization
        with self.lock:
            while self.chopStickTaken == True:
                self.lock.wait()
            self.philosopherId = philosopherId
            self.chopStickTaken = True
            sys.stdout.write("p[%s] took c[%s]\n" % (philosopherId, self.chopStickId))
            self.lock.notifyAll()

    def drop(self, philosopherId):         # used for synchronization
        with self.lock:
            while self.chopStickTaken == False:
                self.lock.wait()
            self.philosopherId = -1
            self.chopStickTaken = False
            doc = collection.find_one({"number" : philosopherId})
            sys.stdout.write("p[%s] i.e. %s dropped c[%s] and thinks -> %s\n" % (philosopherId,doc["name"], self.chopStickId, doc["thought"]))
            self.lock.notifyAll()


class Philosopher (threading.Thread):

    def __init__(self, philosopherId, leftChopStick, rightChopStick, butler):
        threading.Thread.__init__(self)
        self.philosopherId = philosopherId            # philosopher number
        self.leftChopStick = leftChopStick
        self.rightChopStick = rightChopStick
        self.butler = butler

    def run(self):
        for i in range(20):
            self.butler.down()              # start service by butler
            time.sleep(0.1)                 # think
            self.leftChopStick.take(self.philosopherId)     # pickup left chopstick
            time.sleep(0.1)                 # (yield makes deadlock more likely)
            self.rightChopStick.take(self.philosopherId)    # pickup right chopstick
            time.sleep(0.1)                 # eat
            self.rightChopStick.drop(self.philosopherId)    # drop right chopstick
            self.leftChopStick.drop(self.philosopherId)     # drop left chopstick
            self.butler.up()                # end service by butler
        sys.stdout.write("p[%s] finished thinking and eating\n" % self.philosopherId)


def main():
    # number of philosophers / chop sticks
    n = 5

    # butler for deadlock avoidance (n-1 available)
    butler = Semaphore(n-1)

    # list of chopsticks
    c = [ChopStick(i) for i in range(n)]

    # list of philsophers
    p = [Philosopher(i, c[i], c[(i+1)%n], butler) for i in range(n)]

    for i in range(n):
        p[i].start()


if __name__ == "__main__":
    main()
