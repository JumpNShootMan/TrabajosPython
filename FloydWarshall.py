import math
import heapq

def floydwarshall(G):
  n=len(G)
  d=[[math.inf]*n for _ in range(n)]
  p=[[-1]*n for _ in range(n)]
  for u in range(n):
    d[u][u]=0
    for v,w in G[u]:
      d[u][v]=w
      p[u][v]=u

  for k in range(n):
    for i in range(n):
      for j in range(n):
        f=d[i][k] + d[k][j]
        if d[i][j] > f:
          d[i][j] = f
          p[i][j] = k

  return p,d

G=[[(1,6),(3,7)],
  [(2,5),(3,8),(4,4)],
  [(1,2),(4,7)],
  [(2,3),(4,9)],
  [(0,2)]]

print(floydwarshall(G))
