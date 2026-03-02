def fsm(x):
  graph = {
    'S0': {'a':'S1', 'b':'S0'},
    'S1': {'a':'S1', 'b':'S2'},
    'S2': {'a':'S1', 'b':'S3'},
    'S3': {'a':'S1', 'b':'S0'}
  }
  state = 'S0'
  for s in x:
    if s in graph[state]:
      state = graph[state][s]
    else:
      return False
  return state == 'S3'

print(fsm('aababb'))
print(fsm('aaab'))
