def gumhan(X,Y,k)
  n = len(X)
  Z = []
  for i in range(n)
    Z.append([])
    for j in range(n)
      Z[i].append(X[i][j]+kY[i][j])
  return Z


def strassenmul(X,Y)
  n = len(X)
  if n == 2
    a = X[0][0]
    b = X[0][1]
    c = X[1][0]
    d = X[1][1]
    e = Y[0][0]
    f = Y[0][1]
    g = Y[1][0]
    h = Y[1][1]
    P1 = a(f-h)
    P2 = (a+b)h
    P3 = (c+d)e
    P4 = d(g-e)
    P5 = (a+d)(e+h)
    P6 = (b-d)(g+h)
    P7 = (a-c)(e+f)
    return [[P5+P4-P2+P6,P1+P2],[P3+P4,P1+P5-P3-P7]]
  A = []
  for i in range(n2)
    A.append([])
    for j in range(n2)
      A[i].append(X[i][j])
  B = []
  for i in range(n2)
    B.append([])
    for j in range(n2,n)
      B[i].append(X[i][j])
  C = []
  for i in range(n2,n)
    C.append([])
    for j in range(n2)
      C[i-n2].append(X[i][j])
  D = []
  for i in range(n2,n)
    D.append([])
    for j in range(n2,n)
      D[i-n2].append(X[i][j])
  E = []
  for i in range(n2)
    E.append([])
    for j in range(n2)
      E[i].append(Y[i][j])
  F = []
  for i in range(n2)
    F.append([])
    for j in range(n2,n)
      F[i].append(Y[i][j])
  G = []
  for i in range(n2,n)
    G.append([])
    for j in range(n2)
      G[i-n2].append(Y[i][j])
  H = []
  for i in range(n2,n)
    H.append([])
    for j in range(n2,n)
      H[i-n2].append(Y[i][j])
  p1 = strassenmul(A,gumhan(F,H,-1))
  p2 = strassenmul(gumhan(A,B,1),H)
  p4 = strassenmul(D,gumhan(G,E,-1))
  p3 = strassenmul(gumhan(C,D,1),E)
  p5 = strassenmul(gumhan(A,D,1),gumhan(E,H,1))
  p6 = strassenmul(gumhan(B,D,-1),gumhan(G,H,1))
  p7 = strassenmul(gumhan(A,C,-1),gumhan(E,F,1))
  A0 = gumhan(gumhan(p5,p6,1),gumhan(p4,p2,-1),1)
  B0 = gumhan(p1,p2,1)
  C0 = gumhan(p3,p4,1)
  D0 = gumhan(gumhan(p1,p7,-1),gumhan(p5,p3,-1),1)
  Z = []
  for i in range(n2)
    Z.append(A0[i] + B0[i])
  for i in range(n2)
    Z.append(C0[i] + D0[i])
  return Z


x = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
y = [[17,18,19,20],[21,22,23,24],[25,26,27,28],[29,30,31,32]]
strassenmul(x,y)



