import math
import heapq as hq

def prim(G):
  n=len(G)
  dist=[math.inf]*n
  path=[-1]*n
  visited=[False]*n
  q=[]
  dist[0]=0
  hq.heappush(q,(0,0))
  while len(q)>0:
    _, u= hq.heappop(q)
    if not visited[u]:
      for v,w in G[u]:
        if not visited[v] and w < dist[v]:
          dist[v]=w
          path[v]=u
          hq.heappush(q,(w,v))

  return path, dist

G=[[(1,2),(2,3),(4,6)], #arco de 0 a 1 que pesa 2... de 0 a 2
    [(0,2),(4,2),(5,3)],
    [(0,3),(4,1),(3,5)],
    [(2,5),(4,5),(5,6)],
    [(0,6),(1,2),(2,1),(3,5),(5,4)],
    [(1,3),(3,6),(4,4)]]
  
print(prim(G))
