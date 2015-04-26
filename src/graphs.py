import matplotlib.pyplot as plt
import numpy as np
import scipy as sc

import timings

def plot(timedict):
    xs = timedict.pop("ns")
    for alg, times in timedict.items():
        ys = ([np.mean(ts) for ts in times])

        plt.plot(xs,ys,label=alg)

    plt.xlabel('array size')
    plt.ylabel('time')

    plt.legend()
    plt.title("Running Times of Various\nMaximum Sum Subarray Algorithms")

    plt.savefig("../bin/testrun.png",bbox_inches="tight")
    plt.show()



plot(timings.timefuncs())
