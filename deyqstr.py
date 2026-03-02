import math

def argmin(T, S):
  amin = -1
  m = math.inf
  for i, t in enumerate(T):
    if t < m and i not in S:
      m = t
      amin = i
  return amin
map = [
  [0, 3, 1, 3, math.inf, math.inf],
  [3, 0, 4, math.inf, math.inf, math.inf],
  [1, 4, 0, math.inf, 7, 5],
  [3, math.inf, math.inf, 0, math.inf, 2],
  [math.inf, math.inf, 7, math.inf, 0, 4],
  [math.inf, math.inf, 5, 2, 4, 0]
]
N = len(map)
T = [math.inf]*N
v = 0
S = {v}
T[v] = 0
M = [0]*N
while v != -1:
  for j, dw in enumerate(D[v]):
    if j not in S:
      w = T[v] + dw
      if w < T[j]:
        T[j] = w
        M[j] = v

  v = argmin(T, S)
  if v >= 0:
    S.add(v)

start = 0
final = 4
P = [final]
while final != start:
  final = M[P[-1]]
  P.append(final)
print(P)