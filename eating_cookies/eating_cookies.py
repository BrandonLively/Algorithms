#!/usr/bin/python

import sys


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    if n <= 1:
        return 1
    calc = [0 for i in range(0, n+1)]

    # base cases
    calc[0] = calc[1] = 1
    calc[2] = 2

    # Iterate for all values from 4 to n
    for i in range(3, n + 1):
        calc[i] = calc[i - 1] + calc[i - 2] + calc[i - 3]

    return calc[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies),
                                                                                    n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
