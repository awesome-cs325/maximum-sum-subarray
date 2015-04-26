#!python3
#Algorithm 3 : Divide and Conquer

import ourutils
import math

# the combining half of algorithm3
def mergeHalves(lowerHalf, upperHalf):
    #set bounds of new combined array
    j = lowerHalf[0]
    k = upperHalf[1]

    #compute max sum of combined arrays
    # it will either be:
    #   the max sum of lowerHalf
    #   the max sum of upperHalf
    #   the combined sums upper end of lowerHalf and lower end of upperHalf
    if lowerHalf[2] > upperHalf[2]:
        newMaxSum = lowerHalf[2]
        maxSumJ = lowerHalf[3]
        maxSumK = lowerHalf[4]
    else:
        newMaxSum = upperHalf[2]
        maxSumJ = upperHalf[3]
        maxSumK = upperHalf[4]
    suffixMaxSum = lowerHalf[7] + upperHalf[5]
    if suffixMaxSum > newMaxSum:
        newMaxSum = suffixMaxSum
        maxSumJ = lowerHalf[8]
        maxSumK = upperHalf[6]

    return [j, k, newMaxSum, maxSumJ, maxSumK, -1, -1, -1, -1]


# recursive solution to finding the max sum (algorithm 3)
def algorithm3(array, lower, upper):
    upperSum = [];
    lowerSum = [];
    # format of array that holds return data:
    # Bounds of subarray:
    # [0] lower bound of subarray
    # [1] upper bound of subarray
    # MaxSum data within that array:
    # [2] bestMaxSum
    # [3] lower bound of range that holds bestMaxSum
    # [4] upper bound of range that holds bestMaxSum
    # Best sum that overlaps along the lower bound of subarray:
    # [5] bestMaxSum that includes lower bound of the subarray
    # [6] upper bound of the range that creates bestMaxSum(Lower)
    # Best sum that overlaps along the upper bound of subarray:
    # [7] bestMaxSum that includes upper bound of the subarray
    # [8] lower bound of the range that creates bestMaxSum(Upper)
    bestMaxSum = [lower, upper, -99999, 0, 0, -99999, 0, -99999, 0]
    if lower == upper:  #size of subarray is 1
        bestMaxSum = [lower, upper, array[lower], lower, upper, array[lower], lower, array[upper], upper]
    else:   # split array into 2 subarrays and recursively merge their answers
        mid = math.floor((upper + lower) / 2)
        lowerSum = algorithm3(array, lower, mid)
        upperSum = algorithm3(array, mid+1, upper)
        bestMaxSum = mergeHalves(lowerSum, upperSum)


        #find best sum that covers the lower suffix of the joined array
        best_here = 0
        best_so_far = 0
        best_pos = 0

        for i in range(bestMaxSum[0], bestMaxSum[1]+1):
            best_here = array[i] + best_here
            if best_here > best_so_far:
                best_so_far = best_here
                best_pos = i

        bestMaxSum[5] = best_so_far
        bestMaxSum[6] = best_pos

        #find best sum that covers the upper suffix of the joined array
        best_here = 0
        best_so_far = 0
        best_pos = 0
        for j in range(bestMaxSum[1], bestMaxSum[0]-1, -1):
            best_here = array[j] + best_here
            if best_here > best_so_far:
                best_so_far = best_here
                best_pos = j

        bestMaxSum[7] = best_so_far
        bestMaxSum[8] = best_pos

    return bestMaxSum

def alg(problemList):
    strArr = []

    result = []
    # solve for finding the max sum
    for array in problemList:
        strArr.append(ourutils.stringArr(array))

        result = algorithm3(array, 0, len(array) - 1)

        #print(result)

        bestsum = result[2]
        bestlower = result[3]
        bestupper = result[4]

        s = ourutils.stringRes(array,bestsum,bestlower,bestupper)
        if s.find("None") > -1:
            raise Exception("WOAH!",s)
        strArr.append(s)

    return strArr

def main():
    strs = (alg(ourutils.readFile()))
    for str in strs:
        print(str)
