#!/usr/bin/env python3
#Algorithm 4 : Linear Time

import ourutils

def alg(problemList):
    strArr = []
    #for each array in file
    for array in problemList:
        strArr.append(ourutils.stringArr(array))

        #best sum out of all current sums
        bestsum = array[0]
        #best/curr indices
        bestlower = currlower = 0
        bestupper = currupper = 0

        #start at current sum
        currentsum = array[bestlower]
        if len(array) > 1:
            #loop through all values, appending each to the "array of solved max"
            for i in range(1,len(array)):
                #if our current array is <0 and curr value is >0
                #we'll just take the value as curr,
                #there's no way our past array would be greater with this ele
                #also, if its still negative, but our array is negative, we'll take it as "less neg"
                if array[i] > currentsum + array[i]:
                    currlower = i
                    currupper = i
                    currentsum = array[i]
                #if the array is greater than 0, we'd want to push the curr value to make it greater
                #if both the curr val and array sum is less than 0, add them
                else:
                    currupper = i
                    currentsum += array[i]

                #if the current value is negative, it
                #otherwise, it might change
                if currentsum > bestsum:
                    bestlower = currlower
                    bestupper = currupper
                    bestsum = currentsum

        s = ourutils.stringRes(array,bestsum,bestlower,bestupper)
        if s.find("None") > -1:
            raise Exception("WOAH!",s)
        strArr.append(s)

    return strArr

def main():
    strs = (alg(ourutils.readFile()))
    for str in strs:
        print(str)
