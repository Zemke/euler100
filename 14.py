#!/usr/bin/env python

def seq(n):
  cc = 0
  while n != 1:
    cc += 1
    if n % 2 == 0:
      n //= 2
    else:
      n = 3 * n + 1
  return cc + 1


m = 0
by = None
for i in range(1, 1000000):
  s = seq(i)
  if s> m:
    m = s
    by = i

print(by)

