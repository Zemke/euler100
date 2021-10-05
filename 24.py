#!/usr/bin/env python

from sys import exit
import math


def swappery(init, fixed):
  """Find all permutations"""
  r = set()
  for i in range(fixed, len(init)):
    for k in range(fixed+1, len(init)):
      nex = init[::]
      nex.insert(i, nex.pop(k))
      nex_joined = "".join(nex)
      if nex_joined not in r:
        print(nex_joined)
        r.add(nex_joined)
      r.update(swappery(nex, fixed+1))
  return r


def nex(init):
  print("init", init)

  fci = None  # index of first character
  for i in range(len(init)-2, -1, -1):
    if init[i] < init[i+1]:
      fci = i
      break
  print("fci", fci)

  sci = fci+1  # index of second character
  for i in range(fci+2, len(init)):
    if init[i] > init[fci] and init[i] < init[sci]:
      sci = i
  print("sci", sci)

  nex = init[::]
  nex.insert(fci, nex.pop(sci))

  ssubstr = []  # sorted substr from fci to sci
  for i in nex[fci+1:]:
    idx = 0
    while idx < len(ssubstr) and ssubstr[idx] < i:
      idx += 1
    ssubstr.insert(idx, i)
  print("ssubstr", nex[fci+1:], ssubstr)

  return [*nex[:fci+1], *ssubstr]


init = [i for i in range(10)]
curr = nex(init)
for i in range(2, 1000000):
  curr = nex(curr)
print("millionth permutation:", "".join([str(i) for i in curr]))

