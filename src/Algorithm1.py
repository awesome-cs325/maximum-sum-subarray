#!python3
# Algorithm 1 : Enumeration
# Loop over the entire array with indices i, j and keep the best sum.

import ourutils

def alg(problemList):
    strArr = []
    # solve for finding the max sum
    # on every array in the file
    for array in problemList:
        strArr.append(ourutils.stringArr(array))
        #for each array in the file
        bestsum = array[0]
        #one index
        bestupper = 0
        #the other index
        bestlower = 0
        #find the best sum by comparing every single possible sum between two indices
        #loop our first index across every value
        for n in range(len(array)):
            #and loop our second index across every value as well
            for m in range(n, len(array)):
                currentsum = 0
                #calculate the sum between our two current indices
                for p in range(n, m + 1):
                    currentsum = currentsum + array[p]
                #print("The sum between position %d and position %d is %d" % (n, m, currentsum))
                #if its greater than our current best sum, use it, else keep the reigning champion
                if currentsum > bestsum:
                    bestsum = currentsum
                    bestupper = m
                    bestlower = n

        s = ourutils.stringRes(array,bestsum,bestlower,bestupper)
        if s.find("None") > -1:
            raise Exception("WOAH!",s)
        strArr.append(s)

    return strArr

def main():
    strs = (alg(ourutils.readFile()))
    for str in strs:
        print(str)
