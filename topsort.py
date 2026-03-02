def kahn(graph):
  indegree = {}
  for u in graph:
    indegree[u] = 0
  for u in graph:
    for v in graph[u]:
      indegree[v] += 1
  queue = []
  for node in indegree:
    if indegree[node] == 0:
      queue.append(node)
  res = []
  while queue:
    node = queue.pop(0)
    res.append(node)
    for neighbor in graph[node]:
      indegree[neighbor] -= 1
      if indegree[neighbor] == 0:
        queue.append(neighbor)
  return res

graph = {
  'A': ['C'],
  'B': ['C', 'D'],
  'C': ['E'],
  'D': ['F'],
  'E': ['H', 'F'],
  'F': ['G'],
  'G': [],
  'H': []
}
print(kahn(graph))
