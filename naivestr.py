def naivestr(l,p):
  i = 0
  j=0
  n = len(l)
  m=len(p)
  for i in range(n-m+1):
    j=0
    while j<m and l[i+j]==p[j]:
        j+=1
    if j==m:
      print(f"position {i}")

s = "aaabbababbabbabababbab"
y = "abbab"
naivestr(s,y)