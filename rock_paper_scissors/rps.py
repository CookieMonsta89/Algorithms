#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  outcomes = []
  variations = ['rock', 'paper', 'scissors']

  def find_winner(rounds_left, result=[]):
    if rounds_left == 0:
      outcomes.append(result)
      return
    for vari in variations:
      find_winner(rounds_left -1, result + [vari])

  find_winner(n, [])
  return outcomes

print(rock_paper_scissors(4))
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')