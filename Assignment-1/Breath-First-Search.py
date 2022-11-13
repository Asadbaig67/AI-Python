import queue

# graph = {
#   'A' : ['B','C'],
#   'B' : ['D', 'E'],
#   'C' : ['F'],
#   'D' : [],
#   'E' : ['F'],
#   'F' : []
# }
graph = {
  'Arad' : ['Sibiu','Timisoara','Zerind'],
  'Sibiu' : ['Arad', 'Fagaras','Oradea','Rimnicu Vilcea'],
  'Timisoara' : ['Arad','Lugoj'],
  'Zerind' : ['Arad','Oradea'],
  'Oradea' : ['Zerind','Sibiu'],
  'Rimnicu Vilcea' : ['Craiova','Sibiu','Pitesti'],
  'Fagaras' : ['Sibiu','Bucharest'],
  'Lugoj' : ['Timisoara','Mehadia'],
  'Craiova' : ['Rimnicu Vilcea','Drobeta','Pitesti'],
  'Pitesti' : ['Rimnicu Vilcea','Craiova','Bucharest'],
  'Mehadia' : ['Lugoj','Drobeta'],
#   'Drobeta' : ['Mehadia','Craiova'],
#   'Bucharest' : ['Pitesti','Fagaras','Giurgiu','Urziceni'],
}

visited=[]
queue=[]

def bfs(visited,graph,node,goal):
    if node==goal:
        print(node)
        return
    if node not in visited:
        visited.append(node)
        queue.append(node)
    while queue: #while queue is not empty
        element=queue.pop(0)
        if element==goal:
            print(element)
            return
        print(element,end="->")
        for subnode in graph[element]:
            if subnode not in visited:
                visited.append(subnode)
                queue.append(subnode)

bfs(visited,graph,'Arad','Bucharest')

# for item in graph['A']:
# print(len(graph['A']))
# print(len(graph['C']))
# print(len(graph['F']))
# print(graph['A'][0])


# queue.append('A')
# queue.append('B')
# queue.append('C')
# queue.append('D')
# queue.append('E')
# queue.append('F')

# print(queue)
# queue.append('G')
# # [a,b,c,d,e,f,g,h]
# # queue.append(graph['B'])
# # queue.append(graph['C'])
# # queue.append(graph['D'])
# # queue.append(graph['E'])
# # queue.append(graph['F'])

# while queue:
#     element =queue.pop()
    # print(element)




