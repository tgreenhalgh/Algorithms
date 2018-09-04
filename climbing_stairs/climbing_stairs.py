#!/usr/bin/python

import sys


def climbing_stairs(n):
    ways = [0 for x in range(n + 2)]  # we use 2 in case n = 0
    ways[0], ways[1] = 1, 1

    for i in range(2, n + 1):
        j = 1
        while j <= 3 and j <= i:
            ways[i] = ways[i] + ways[i-j]
            j += 1
    return ways[n]


if __name__ == "__main__":
    # Test out your implementation from the command line
    # with `python climbing_stairs.py [n]` with different n values
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')
