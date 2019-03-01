#!/usr/bin/python

import sys

def climbing_stairs(n):
  # base case
  if n < 0:
    return 0

  if n == 0:
    return 1

  # this step moves towards our base case
  else:
    return climbing_stairs(n-1) + climbing_stairs(n-2) + climbing_stairs(n-3)

print(climbing_stairs(3))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')