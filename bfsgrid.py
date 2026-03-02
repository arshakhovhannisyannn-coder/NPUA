def bfs(grid, start):
  n = len(grid)
  m = len(grid[0])
  visited = set()
  queue = [start]
  res = []
  directions = [(-1,0),(1,0),(0,-1),(0,1)]
  while queue:
    r, c = queue.pop(0)
    if (r,c) in visited:
      continue
    visited.add((r,c))
    res.append((r,c))
    for dr, dc in directions:
      nr, nc = r + dr, c + dc
      if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0 and (nr,nc) not in visited:
        queue.append((nr,nc))
  out = []
  for r in range(n):
    row = []
    for c in range(m):
      if (r,c) in visited:
        row.append('X')
      elif grid[r][c] == 1:
        row.append('1')
      else:
        row.append('0')
    out.append(' '.join(row))
  return '\n'.join(out)

grid = [
  [0,1,0,0,1,1],
  [0,0,1,0,1,0],
  [1,0,0,0,1,0],
  [0,0,1,0,1,1]
]
start = (0,0)
print(bfs(grid, start))