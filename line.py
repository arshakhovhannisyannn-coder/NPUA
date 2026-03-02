def line(A,B,C,D):
  x1,y1 = A
  x2,y2 = B
  x3,y3 = C
  x4,y4 = D
  a1 = y2-y1
  b1 = x1-x2
  c1 = a1*x1+b1*y1
  a2 = y4-y3
  b2 = x3-x4
  c2 = a2*x3+b2*y3
  det = a1*b2 - a2*b1
  if det == 0:
    return None
  x = (c1*b2-c2*b1)/det
  y = (a1*c2-a2*c1)/det
  return [x, y]

A1 = [1,1]
B1 = [5,5]
C1 = [0,4]
D1 = [4,0]
print(line(A1,B1,C1,D1))
