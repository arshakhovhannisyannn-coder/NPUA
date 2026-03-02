def bfs(graph, start):
  visited = set()
  queue = [start]
  res = []
  while queue:
    node = queue.pop(0)
    if node in visited:
      continue
    visited.add(node)
    res.append(node)
    for neighbor in graph[node]:
      if neighbor not in visited:
        queue.append(neighbor)
  return res

map = {
  'A': ['B','C'],
  'B': ['A','G','I'],
  'C': ['A','D','E','F'],
  'D': ['C','E'],
  'E': ['C','D','K'],
  'F': ['C','H'],
  'G': ['B','J'],
  'H': ['F','I'],
  'I': ['B','H','J'],
  'J': ['G','I'],
  'K': ['E'],
  'L': ['M'],
  'M': ['L']
}
print(bfs(map,'I'))