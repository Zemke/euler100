#!/usr/bin/env python

D = {
  0: "",
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10: "ten",
  11: "eleven",
  12: "twelve",
  13: "thirteen",
  14: "fourteen",
  15: "fifteen",
  16: "sixteen",
  17: "seventeen",
  18: "eighteen",
  19: "nineteen",
  20: "twenty",
  30: "thirty",
  40: "forty",
  50: "fifty",
  60: "sixty",
  70: "seventy",
  80: "eighty",
  90: "ninety",
}


def assemble(i):
  if i in D:
    return D[i]
  elif i < 100:
    return D[int(str(i)[0] + "0")] + D[int(str(i)[-1])]
  raise Exception()
  

rr = 0
for i in range(1, 1001):
  print(i, end=' ')
  word = ''
  if i < 100:
    word += assemble(i)
  elif i >= 100 and i < 1000:
    word += D[int(str(i)[0])] + "hundred"
    if str(i)[-2:] != "00":
      word += "and"
    word += assemble(int(str(i)[1:]))
  elif i == 1000:
    word += "onethousand"
  else:
    raise Exception()
  print(word)
  rr += len(word)


print(rr)

