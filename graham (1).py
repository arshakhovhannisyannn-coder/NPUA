import math

def orientation(P,Q,R):
  return (Q[1]-P[1])*(R[0]-Q[0])-(Q[0]-P[0])*(R[1]-Q[1])
def distance(P, Q):
  return (P[0]-Q[0])**2+(P[1]-Q[1])**2

def grahamscan(points):
  n = len(points)
  P0 = min(points,key=lambda p: (p[1],p[0]))
  def angle(p):
    return math.atan2(p[1]-P0[1], p[0]-P0[0])
  psorted = sorted(points,key=lambda p: (angle(p), -distance(P0,p)))
  hull = psorted[:3]
  for p in psorted[3:]:
    while len(hull) >= 2 and orientation(hull[-2], hull[-1], p) < 0:
      hull.pop()
    hull.append(p)
  return hull

points = [[0,0],[1,1],[2,2],[3,1],[4,0],[4,3],[3,4],[2,3],[1,4],[0,3],[2,1],[1,2]]
print(grahamscan(points))
