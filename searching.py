def linearsearch(l,x):
  n = len(l)
  for i in range(n):
    if l[i]==x:
      return i
  return False

def binarysearch(l,x):
  n = len(l)
  s = 0
  h = n-1
  while s<=h:
    i = (s+h)//2
    if l[i]==x:
      return i
    elif l[i] < x:
      s = i+1
    else:
      h = i-1
  return False

def ternarysearch(l,x):
  n = len(l)
  s = 0
  h = n-1
  while s<=h:
    d = (h - s) // 3
    m1 = s + d
    m2 = h - d
    if l[m1]==x:
      return m1
    elif l[m2]==x:
      return m2
    elif l[m1]<x<l[m2]:
      s = m1+1
      h = m2-1
    elif l[m1]>x:
      h = m1-1
    elif l[m2]<x:
      s = m2+1
  return False

def jumpsearch(l,x):
  n = len(l)
  step = int((n)**0.5)
  i=0
  while i<n:
    if l[i] == x:
      return i
    else:
      i+=step
  i-=step
  for i in range(i,n):
    if l[i]==x:
      return i
  return False

def interpolationsearch(l,x):
  n=len(l)
  s=0
  h=n-1
  while s<=h:
    pos = s+int((x-l[s])*(h-s)/(l[h]-l[s]))
    if l[pos] == x:
      return pos
    elif l[pos] > x:
      h = pos-1
    else:
      s = pos+1
  return False

def exponentionalsearch(l,x):
  n = len(l)
  if l[0]==x:
    return 0
  i = 1
  j=0
  while i < n:
    if l[i]==x:
      return i
    elif l[i]>x:
      j = i//2+1
      if type(binarysearch(l[j:i],x)) == bool:
        return False
      else:
        return binarysearch(l[j:i],x) + j
    i*=2
  return binarysearch(l[i//2+1:],x)+i//2+1


l = [2,5,8,12,16,23,38,56,72,91]
x = 12
print(exponentionalsearch(l,x))
