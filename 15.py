#!/usr/bin/env python


import sys

DP = {}

def walk(x, y):
  if x in DP and y in DP[x]:
    return DP[x][y]
  if x == 1 or y == 1:
    return 1
  if x not in DP:
    DP[x] = {}
  DP[x][y] = walk(x-1, y) + walk(x, y-1)
  return DP[x][y]

for n in range(3, 22):
  #print(" nop", n-1, nop(n, n))
  print("walk", n-1, walk(n, n))



"""
 _ _ _ 
|_|_|_|
|_|_|_|
|_|_|_|
"""

