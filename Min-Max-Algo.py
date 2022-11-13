graph = {
  'A': ['B', 'C'],
  'B': [5],
  'C': [1]
}


def Min_Max(graph, node, turn):

    if type(graph[node][0]) == int:
        return graph[node][0]

    print(node)
    min = 0
    max = 0

    for items in graph[node]:

        if turn == 0:
            value=Min_Max(graph,items,turn)
            print(value)


Min_Max(graph,'A')

# print(type(graph['B']))
