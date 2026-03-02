def pat(l):
  n = len(l)
  d = dict()
  x=[]
  for i in range(n-2,-1,-1):
    if l[i] not in x:
      d[l[i]]=n-i-1
      x.append(l[i])
  if l[n-1] not in x:
    d[l[n-1]]=n
  return d

def boyernmurr(l,p):
  n = len(l)
  m=len(p)
  d = pat(p)
  i = m-1
  while i<n:
    if p[-1] != l[i]:
      if l[i] in d:
        i+=d[l[i]]
      else:
        i+=m
    else:
      j=m-1-1
      k=i-1
      while j >= 0 and l[k]==p[j]:
        j-=1
        k-=1
      if j<0:
        print(f"position {i-m+1}")
        i+=m
      else:
        i+=d[p[j]]


s = "sdfjfd asdasd erdfasdkjf sdfsdfass asddasd"
y = "asd"
boyernmurr(s,y)