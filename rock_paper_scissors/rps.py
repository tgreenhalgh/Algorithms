#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    if n > 0:
        list = [["rock"], ["paper"], ["scissors"]]
        results = []

        def recurse(plays):
            if len(plays) == n:
                results.append(plays)
                return

            for l in list:
                recurse(plays + l)

        recurse([])

        return results

    return [[]]


if __name__ == "__main__":
    # Test out your implementation from the command line
    # with `python rps.py [n]` with different n values
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

# print(rock_paper_scissors(2))
