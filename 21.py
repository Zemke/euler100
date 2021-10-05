#!/usr/bin/env python


def d(n):
  return sum([ div for div in range(n - 1, 0, -1) if n % div == 0 ])

  
amicc = []
for a in range(1, 10000):
  b = d(a)
  if a != b and a == d(b):
    if a < 10000 and a not in amicc:
        amicc.append(a)
    if b < 10000 and b not in amicc:
        amicc.append(b)
  a += 1

print(sum(amicc))




