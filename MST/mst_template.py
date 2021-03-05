# Prim’s Algorithm
# Time complexity: O(ElogV)
# Space complexity: O(V+E)
# Author: Huahua
from collections import defaultdict
from heapq import *
 
n = 4
edges = [[0,1,1],[0,3,3],[0,2,6],[2,3,2],[1,2,4],[1,3,5]]
g = defaultdict(list)
for e in edges:
  g[e[0]].append((e[1], e[2]))
  g[e[1]].append((e[0], e[2]))
 
q = []
cost = 0
seen = set()
heappush(q, (0, 0))
for _ in range(n):
  while True:
    w, u = heappop(q)
    if u in seen: continue  
    cost += w
    seen.add(u)
    for v, w in g[u]:
      if v in seen: continue
      heappush(q, (w, v))
    break
 
print(cost)

# Kruskal’s Algorithm
# Time complexity: O(ElogV)
# Space complexity: O(V+E)

from collections import defaultdict
from heapq import *
 
n = 4
edges = [[0,1,1],[0,3,3],[0,2,6],[2,3,2],[1,2,4],[1,3,5]]
p = list(range(n))
 
 
def find(x):
  if x != p[x]: p[x] = find(p[p[x]])
  return p[x]
 
cost = 0
for u, v, w in sorted(edges, key=lambda x: x[2]):
  ru, rv = find(u), find(v)
  if ru == rv: continue
  p[ru] = rv
  cost += w
 
print(cost)







