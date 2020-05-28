import random
import itertools
import functools

lamF1 = lambda a,b : (ord(a)^ord(b)).to_bytes(1,'big')
var1 = 'vvvsssbbbbbb777'
list1 = ((0,3),(1,4),(0,1),(3,4),(2,3),(1,2))
var1 = sorted(list(var1))
lamF2 = lambda a,b:bin((ord(a)-ord(b))^(int('1'*10,2)))[0]!='-'

def func1(li):
  arr=[li[i::3]for i in range(3)]
  for i in arr:
    while not func2(i):
      pass
  return arr
 
def func2(i):
  random.shuffle(i)
  a=[bool(int(bin(ord('e'))[2:][-1]))]
  return[func3(a,lamF2(i[list1[j][0]],i[list1[j][1]]))for j in range(len(list1))][-1]

def func3(g,k):
  g[0]=g[0]and k
  return g[0]

f=func1(var1)

a=open('input.txt','r').read()
m='output.txt'
open(m,'w').write(repr(b''.join([functools.reduce(lamF1,[(((ord(a[i])&(~ord(f[j][i%5])))|((~ord(a[i]))&(ord(f[j][i%5])))).to_bytes(1,"big"))for j in range(len(f))])for i in range(len(a))])))

print(open(m, 'r').read())

# if c%100000==0:
#   print(i)
#   print(c)
