#!python3

#runs against MSS_Problems.txt

import ourutils
import Algorithm1
import Algorithm2
import Algorithm3
import Algorithm4

def test():
    strs = [""]
    strs.append("\n\n"+Algorithm1.__name__)
    strs.append(Algorithm1.alg(ourutils.readFile()))
    strs.append("\n\n"+Algorithm2.__name__)
    strs.append(Algorithm2.alg(ourutils.readFile()))
    strs.append("\n\n"+Algorithm3.__name__)
    strs.append(Algorithm3.alg(ourutils.readFile()))
    strs.append("\n\n"+Algorithm4.__name__)
    strs.append(Algorithm4.alg(ourutils.readFile()))

    ourutils.writeFile(strs)

test()
