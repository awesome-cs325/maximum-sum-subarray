#!python3
#Algorithm 2 : Better Enumeration

import ourutils

def alg(problemList):
    strArr = []
    # solve for finding the max sum
    # for each array in file
    for array in problemList:
        strArr.append(ourutils.stringArr(array))

        bestsum = array[0]
        bestupper = 0
        bestlower = 0

        currentsum = 0
        # loop over each value with the first index
        for n in range(len(array)):
            lastsum = 0
            #just loop over future indices with the second index
            for m in range(n, len(array)):
                #short-cut : if m==n, we know the sum is equal to the value at array[n==m]
                #plus, it resets our 'lastsum' each time n increases by 1, since m starts at n
                if m == n:
                    currentsum = array[n]
                # increment our current sum by adding the current value instead of recalculating each time
                else:
                    currentsum = lastsum + array[m]
                lastsum = currentsum
                #print("The sum between position %d and position %d is %d" % (n, m, currentsum))
                #save the info of our currentsum if its greater than the last bestsum
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
