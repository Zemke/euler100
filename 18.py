#!/usr/bin/env python

from sys import exit
from pprint import pprint

maxint = 9223372036854775807

#s = """03
#07 04
#02 04 06
#08 05 09 03
#99 05 09 03 20"""
s = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

rows = [ list(map(lambda s: int(s), row.split(" "))) for row in s.split("\n")]
print("rows", rows)


class Vertex:
  def __init__(self, row, col):
    self.row = row
    self.col = col
    self.weight = 100 - (rows[self.row][self.col])  # let's find shortest
    self.nn = []
      
  def __repr__(self):
    nn = list(map(lambda v: "Vertex(row={}, col={}, weight={})".format(v.row, v.col, 100 - v.weight), self.nn))
    return "Vertex(row={}, col={}, weight={}, nn={})".format(self.row, self.col, 100 - self.weight, nn)

  def __hash__(self):
    return hash((self.row, self.col))

  def __eq__(self, o):
    return isinstance(o, Vertex) and o.row == self.row and o.col == self.col

  @staticmethod
  def safe(row, col):
    if 0 <= row < len(rows) and 0 <= col < len(rows[row]):
      return Vertex(row, col)
    return None


G = []  # list of vertices
S = [Vertex(0, 0)]
while len(S) > 0:
  v = S.pop()
  if v not in G:
    G.append(v)
  nn = list(filter(lambda x: x is not None, [Vertex.safe(v.row + 1, v.col), Vertex.safe(v.row + 1, v.col + 1)]))
  for n in nn:
    v.nn.append(n)
  S.extend(nn)


for v in G:
  print("v", v)


def Dijkstra(G, source):
  Q = set()
  dist = {}
  for v in G:
    dist[v] = maxint
    Q.add(v)
  dist[source] = 0
  while len(Q) > 0:
    u = None
    least = maxint
    for v in Q:
      if v is None or dist[v] < least:
        u = v
        least = dist[v]
    Q.remove(u)
    for v in u.nn:
      if v not in Q:
        continue
      alt = v.weight + dist[u]
      if alt < dist[v]:
        dist[v] = alt
  return dist


    
print("Dijkstra")
root = G[0]
dist = Dijkstra(G, root)
print("result")
pprint(dist)

t = None
t_d = None
for v, d in dist.items():
  if v.row == len(rows) - 1:
    if t is None or d < t_d:
      t = v
      t_d = d

print("target", t, t_d)  # target Vertex(row=14, col=9, weight=93, nn=[]) 401
summ = 100 - t.weight
prev = t

for row in range(len(rows)-2, -1, -1):
  nn = []
  for v in G:
    if v.row == row:
      if prev == v.nn[0]:
        nn.append(v)
      elif prev == v.nn[1]:
        nn.append(v)
  if len(nn) < 2 or dist[nn[0]] < dist[nn[1]]:
    prev = nn[0]
  else:
    prev = nn[1]
  summ += 100 - prev.weight

print("sum", summ)

