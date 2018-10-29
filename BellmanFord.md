```python
#Bellman Ford
import math
import heapq

def bellmanford(G, origen):
  n=len(G)
  #vecvis=[False]*n
  #vecpos=[]*n
  vecpadre=[None]*n
  vecwidth=[math.inf]*n
  vecwidth[origen]=0
  for i in range(n-1): #recorremos n-1 veces
    for u in range(n): # G es un arreglo de listas
      for v,w in G[u]: # el doble for permite recorrer todos los arcos de G
        f = vecwidth[u]+w
        #w=peso, u=nodo origen v=nodo destino #se sacan los elementos de cada vertice
        if vecwidth[v] > f: 
          vecwidth[v]=f
          vecpadre[v]=u
  for u in range(n):
    for v,w in G[u]:
      if vecwidth[v] > vecwidth[u] + w:
        print("Oh no! , Ciclo negativo")
        return
  return vecpadre,vecwidth


#En la pos 0, llega a nodo 1 con costo 6 y nodo 3 con costo 7... etc
G=[[(1,6),(3,7)],
  [(2,5),(3,8),(4,-4)],
  [(1,-2),(4,7)],
  [(2,-3),(4,9)],
  [(0,2)]]

print(bellmanford(G,0))
```
