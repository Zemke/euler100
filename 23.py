#!/usr/bin/env python


def abundant(n):
  summ = 0
  for i in range(n - 1, 0, -1):
    if n % i == 0:
      summ += i
  return summ > n


DP = set()
abundants = set()
thres = 28123

summ = 0
for i in range(1, thres+1):
  if abundant(i):
    abundants.add(i)
    for ab in abundants:
      DP.add(i + ab)
  if i not in DP:
    print(i)
    summ += i


print(summ)

