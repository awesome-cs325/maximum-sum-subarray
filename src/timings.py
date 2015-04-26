#!python3

import Algorithm1
import Algorithm2
import Algorithm3
import Algorithm4
import time
import random
import pprint

def timefunc(func,args):

    startTime = time.time()
    func(args)
    elapsedTime = time.time() - startTime

    return elapsedTime

def timegen(func,ns):
    arrs = []
    #for each size n...
    for n in ns:
        #list comprehension doesnt like 2d arrays
        arr = []
        #for 10 times...
        for x in range(10):
            #generate a random array of size n
            arr.append([[int(1000*random.random()-500) for i in range(n)]])
        arrs.append(arr)

    times = []
    #for each input size
    for aa in arrs:
        #calculate the time for each of the 10 generated arrays
        times.append([timefunc(func,a) for a in aa])

    return times

def timefuncs():
    ns = list(range(10,91,10))
    timedict = {}
    #generate dictionaries for ease of labels in graphing
    for algType in [Algorithm1,Algorithm2,Algorithm3,Algorithm4]:
        timedict[str(algType.__name__)] = timegen(algType.alg,ns)

    timedict["ns"] = ns
    return timedict

def main():
    timedict = timefuncs()
    pprint.pprint(timedict)
