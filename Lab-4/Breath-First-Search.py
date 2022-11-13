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
  'A' : ['B','E'],
  'B' : ['C', 'D'],
  'C' : [],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited=[]
queue=[]

def bfs(visited,graph,node,goal):
    if node not in visited:
        visited.append(node)
        queue.append(node)
    while queue: #while queue is not empty
        element=queue.pop(0)
        print(element,end=" ")
        for subnode in graph[element]:
            if subnode not in visited:
                visited.append(subnode)
                queue.append(subnode)

bfs(visited,graph,'A','F')

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




