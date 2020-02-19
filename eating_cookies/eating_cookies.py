#!/usr/bin/python

import sys


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    DP = [0 for i in range(0, n)]

    # base cases
    DP[0] = DP[1] = DP[2] = 1

    # Iterate for all values from 4 to n
    for i in range(3, n):
        DP[i] = DP[i - 1] + DP[i - 2] + DP[i - 3]

    return DP[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies),
                                                                                    n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
