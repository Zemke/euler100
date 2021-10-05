#!/usr/bin/env python


def is_leap(y):
  return y % 4 == 0 and y % 100 == 0 and y % 400 != 0


def days_in_month(m, y):
  if m in [9, 4, 6, 11]:
    return 30
  if m == 2:
    return 29 if is_leap(y) else 28
  return 31


# date of first sunday on the first in the 20th century
m = 9
y = 1901
passed = 0

r = 1

while y <= 2000:
  passed += days_in_month(m, y)
  if m < 12:
    m += 1
  else:
    m = 1
    y += 1
  if passed % 7 == 0:
    r += 1

print("result", r)

