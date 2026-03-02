def pat(l):
  n=len(l)
  j=0
  i=1
  p=[0]
  while i<n:
    if l[j] != l[i]:
      if j == 0:
        p.append(0)
        i+=1
      else:
        j=p[j-1]
    else:
      j+=1
      i+=1
      p.append(j)
  return p

def kmp(l,p):
  i = 0
  j=0
  n = len(l)
  m=len(p)
  x = pat(p)
  while i < n:
    if l[i] == p[j]:
      i+=1
      j+=1
      if j==m:
        print(f"position {i-m}")
        j=x[j-1]
    else:
      if j == 0:
        i+=1
      else:
        j = x[j-1]

s = "aaabbababbabbabababbab"
y = "abbab"
kmp(s,y)