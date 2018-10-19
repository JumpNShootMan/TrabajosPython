def find(c,a):
  if c[a]== a:
    return a
  else:
    abuelo= find(c,c[a])
    c[a]=abuelo
    return abuelo
  
def union(c,a,b):
  pa=find(c,a)
  pb=find(c,b)
  c[pb]=pa

def detectaciclo(G):
   n= len(G)
   c=[i for i in range(n)]
   for u in range(n):
     for v in G[u]:
       pu=find(c,u)
       pv= find(c,v)
       print(u,v,c)
       if pu==pv:
         return True
       else:
         union(c,pu,pv)
   return False
  
G=[[1,2],[],[]]
print(detectaciclo(G))
