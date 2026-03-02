def orientation(P,Q,R):
  return (Q[1]-P[1])*(R[0]-Q[0])-(Q[0]-P[0])*(R[1]-Q[1])
def distance(P, Q):
  return (P[0]-Q[0])**2+(P[1]-Q[1])**2
def jarvismarch(points):
  n = len(points)
  start = 0
  for i in range(1,n):
    if points[i][0] <points[start][0]:
      start = i
  convexhull = []
  P = start
  while True:
    convexhull.append(points[P])
    Q = (P+1)%n
    for R in range(n):
      o = orientation(points[P],points[Q],points[R])
      if o > 0:
        Q = R
      elif o == 0:
        if distance(points[P],points[R]) > distance(points[P],points[Q]):
          Q = R
    P = Q
    if P == start:
      break
  return convexhull

points = points = [[0,0],[1,1],[2,2],[3,1],[4,0],[4,3],[3,4],[2,3],[1,4],[0,3],[2,1],[1,2]]
print(jarvismarch(points))
