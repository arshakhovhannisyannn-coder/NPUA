def dfs(graph,start,visited):
  res = []
  stack = [start]
  while stack:
    node = stack.pop()
    if node in visited:
      continue
    visited.add(node)
    res.append(node)
    for v in graph[node]:
      if v not in visited:
        stack.append(v)
  return res

def components(graph):
  visited = set()
  components = []
  for i in graph:
    if i not in visited:
      comp = dfs(graph,i,visited)
      components.append(comp)
  return components
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
comp = components(map)
for i in comp:
  print(i)