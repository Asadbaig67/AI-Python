graph = {
  'Arad' : ['Sibiu','Timisoara','Zerind'],
  'Sibiu' : ['Arad', 'Fagaras','Oradea','Rimnicu Vilcea'],
  'Timisoara' : ['Arad','Lugoj'],
  'Zerind' : ['Arad','Oradea'],
  'Fagaras' : ['Sibiu','Bucharest'],
  'Oradea' : ['Zerind','Sibiu'],
  'Rimnicu Vilcea' : ['Craiova','Sibiu','Pitesti'],
  'Lugoj' : ['Timisoara','Mehadia'],
  'Craiova' : ['Rimnicu Vilcea','Drobeta','Pitesti'],
  'Pitesti' : ['Rimnicu Vilcea','Craiova','Bucharest'],
  'Mehadia' : ['Lugoj','Drobeta'],
  'Drobeta' : ['Mehadia','Craiova'],
  'Bucharest' : ['Pitesti','Fagaras','Giurgiu','Urziceni'],
}

visited = set()

# def dfs(visited,graph,node):
#     if node not in visited:
#         print(node)
#         visited.add(node)
#         for item in graph[node]:
#             dfs(visited,graph,item)
def dfs(visited,graph,node,goal):
    if node==goal:
        print(node)
        return
    if node in visited:
        return
    else:
        print(node,end='->')
        visited.add(node)
        for item in graph[node]:
            dfs(visited,graph,item,goal)


dfs(visited,graph,'Arad','Bucharest')

      