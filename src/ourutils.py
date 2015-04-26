#utils for reading/writing and such

import ast

def readFile(fname="MSS_Problems.txt"):
    # input file
    problemList = []
    with open(fname, "r") as fileobj:
        print("Name of the file %s" % fileobj.name)

        line = fileobj.readlines()
        for i in line:
            if (i != '') and (i != '\n'):
                problemList.append(ast.literal_eval(i))

    return problemList

def writeFile(strArrs,fname="../bin/MSS_Solutions.txt"):
    # output file
    with open(fname, "w+") as fileobj:
        for strArr in strArrs:
            for str in strArr:
                fileobj.write(str)

def stringArr(array):
    s = "\nSolving for array: " + str(array).strip('[]')
    s += "\n"

    return s

def stringRes(array,bestsum,bestlower,bestupper):
    s = "\nThe best sum is %d" % bestsum
    s += "\nIt falls between positions %d and %d" % (bestlower, bestupper)
    s += "\n" + str(array[bestlower:bestupper + 1])
    s += "\n\n"
    s += "********************************************************"
    s += "\n\n"

    return s

def printArr(array):
    print(stringArr(array))

def printRes(array,bestsum,bestlower,bestupper):
    #print out our info about it
    print(stringRes(array,bestsum,bestlower,bestupper))
