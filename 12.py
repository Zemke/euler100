#!/usr/bin/env python

from sys import exit


primes = [2, 3, 5, 7, 11, 13, 17, 19,
          23, 29, 31, 37, 41, 43, 47,
          53, 59, 61, 67, 71, 73, 79,
          83, 89, 97]
DP_prime = dict(enumerate([ (i in primes) for i in range(0, 101) ]))


def prime(n):
  if n in DP_prime:
    return DP_prime[n]
  for i in range(2, n):
    if n % i == 0:
      DP_prime[n] = False
      return DP_prime[n]
  DP_prime[n] = True
  return DP_prime[n]


def factors(n, P=None):
  """factor tree"""
  if P is None:
    P = []
  if prime(n):
    return [n]
  x = 2
  while n % x != 0 and x < n:
    x += 1
  for c in [ x, n // x ]:
    if prime(c):
      P.append(c)
    else:
      factors(c, P)
  return P
    

def t(n):
  r = 0
  ii = range(1, n + 1)
  for i in ii:
    r += i
  return r


def ff(n):
  bb = [ i for i in range(n, 0, -1) ]
  ff = []
  for b in bb:
    if n % b == 0:
      ff.append(b)
  return ff

def ff_count(factors):
  F = {}
  for f in factors:
    if f not in F:
      F[f] = 1
    F[f] += 1
  res = 1
  for f in F.values():
    res *= f
  return res
    

i = 1
prev_t = 1
while True:
  i += 1
  res_t = i + prev_t
  prev_t = res_t
  res_ff_count = ff_count(factors(res_t))
  if res_ff_count > 500:
    print(res_t)
    break

