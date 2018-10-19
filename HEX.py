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

EMPTY = -1
BLACK = 0
WHITE = 1
ERROR = -255

def findwinnerblacks(c,n):
  #n=math.floor(math.sqrt(len(c)))
  for i in range (n):
    for j in range (n):
      a = i
      b = (n-1)*n+j
      if find(c,a)==find(c,b):
        return True
  return False
def findwinnerwhites(c):
  #TODO seccion de whites n=math.floor(math.sqrt(len(c)))


def turn(t,cb,cw,i0,j0,piece): #cblancas , cwhites
  if t[i0][j0] != EMPTY: return ERROR
  n=len(t)
  t[i0][j0]=piece
  def verify(i, j):
    if i<0 or i>=n or j<0 or j>=n: return ERROR
    if t[i][j] == piece:
      idx = i*n+j
      idx0=i0*n+j0
      if piece==BLACK:
        union(cb,idx,idx0)
        print(cb)
      else:
        union(cw,idx,idx0)
    return 0
  verify(i0 -1,j0)
  verify(i0 -1,j0+1)
  verify(i0,j0-1)
  verify(i0,j0+1)
  verify(i0 +1,j0-1)
  verify(i0 +1,j0)
  if piece ==BLACK:
    if findwinnerblacks(cb,n):
      print('ganaron las fichas negras')
      print(cb)
      return True
  else:
    if findwinnerwhites(cw,n):
      print('Ganaron las fichas blancas')
      return True
  return False
n=5
t=[[EMPTY]*n for _ in range(n)]
cb= [i for i in range(n**2)]
cw= [i for i in range(n**2)]
turn(t,cb,cw,0,0,BLACK)
turn(t,cb,cw,1,0,BLACK)
turn(t,cb,cw,2,0,BLACK)
turn(t,cb,cw,3,0,BLACK)
turn(t,cb,cw,4,0,BLACK)
