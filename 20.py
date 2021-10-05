#!/usr/bin/env python


def fact(n):
  product = 1
  while n > 0:
    product *= n
    n -= 1
  return product


fact10 = fact(100)
summ = sum([int(i) for i in  str(fact10)])
print(summ)


