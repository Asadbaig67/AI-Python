graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = set()

# def dfs(visited,graph,node):
#     if node not in visited:
#         print(node)
#         visited.add(node)
#         for item in graph[node]:
#             dfs(visited,graph,item)
def dfs(visited,graph,node):
    if node in visited:
        return
    else:
        print(node,end=' ')
        visited.add(node)
        for item in graph[node]:
            dfs(visited,graph,item)


dfs(visited,graph,'A')

      