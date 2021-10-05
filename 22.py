#!/usr/bin/env python

from math import floor

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def compare(a, b):
  min_length = min(len(a), len(b))
  x = a[:min_length]
  y = b[:min_length]
  if x.startswith(y):
    return len(a) - len(b)
  for xi in range(len(x)):
    if x[xi] == y[xi]:
      return compare(x[xi+1:], y[xi+1:])
    else:
      return -1 if x[xi] < y[xi] else 1
  return 0

def mysort(nn):
  abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  count = 0
  while count < len(nn):
    mv = nn.pop()
    t_idx = 0
    while compare(mv, nn[t_idx]) > 0 and t_idx < count:
      t_idx += 1
    nn.insert(t_idx, mv)
    count += 1


with open('22.in', 'r') as f:
  read = [ n.strip('"') for n in f.read().split(",") ]
  mysort(read)
  print(read)
  summ = 0
  for idx, name in enumerate(read):
    score = 0
    for n in name:
      score += abc.index(n) + 1
    summ += (idx+1) * score
  print(summ)


