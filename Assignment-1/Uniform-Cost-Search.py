graph = {
    'A':[[8,'B'],[5,'B']],
    'B':[[1,'C'],[2,'D']],
    'C':[[3,'F']],
    'D':[[3,'E']],
    'E':[[1,'G']],
    'G':[[4,'F']],
    'F':[]
}
# graph = {
#   'Arad' : [[140,'Sibiu'],[118,'Timisoara'],[75,'Zerind']],
#   'Sibiu' : [[140,'Arad'], [99,'Fagaras'],[151,'Oradea'],[80,'Rimnicu Vilcea']],
#   'Timisoara' : [[118,'Arad'],[111,'Lugoj']],
#   'Zerind' : [[75,'Arad'],[71,'Oradea']],
#   'Fagaras' : [[99,'Sibiu'],[211,'Bucharest']],
#   'Oradea' : [[71,'Zerind'],[151,'Sibiu']],
#   'Rimnicu Vilcea' : [[146,'Craiova'],[80,'Sibiu'],[97,'Pitesti']],
#   'Lugoj' : [[111,'Timisoara'],[70,'Mehadia']],
#   'Craiova' : [[146,'Rimnicu Vilcea'],[120,'Drobeta'],[138,'Pitesti']],
#   'Pitesti' : [[97,'Rimnicu Vilcea'],[138,'Craiova'],[101,'Bucharest']],
#   'Mehadia' : [[70,'Lugoj'],[75,'Drobeta']],
#   'Drobeta' : [[75,'Mehadia'],[120,'Craiova']],
#   'Bucharest' : [[101,'Pitesti'],[211,'Fagaras'],[90,'Giurgiu'],[85,'Urziceni']],
# }

visited=[]
queue=[]
# Funtion to sort the nodes according to the shortest weight
def function_sort(node):
    item=graph[node]
    item.sort()
    return item

# print(graph['D'][0][1])
# sortednode=function_sort("B")
# currnode=sortednode[0][1]
# print(currnode)



# print(len(graph['G']))
# print(function_sort('C'))

def UFC(visited,graph,node,goal):
    if node not in visited:
        visited.append(node)
        queue.append(node)
    while queue:
        node=queue.pop(0)  
        if node==goal:
            print(goal)
            return
        print(node,end="->")
        if len(graph[node])==0:
            continue
        elif len(graph[node])==1:
            if graph[node][0][1] not in visited:
                visited.append(graph[node][0][1])
                queue.append(graph[node][0][1])
        else:
            sortednode=function_sort(node)
            currnode=sortednode[0][1]
            if currnode not in visited:
                visited.append(currnode)
                queue.append(currnode)
            


UFC(visited,graph,'A','F')





# for item in graph:
#     temp=graph[item]
#     temp.sort()
#     print(temp)


# def sortlist(graph,node):
#     temp=graph[node].sort()
#     return temp


# node=sortlist(graph,'A');
# print(node);
# visited = set()

# def dfs(visited,graph,node):
#     if node in visited:
#         return
#     else:
#         for item in graph:
#             temp=graph[item]
#             temp=temp.sort()  
#             print(temp)
#             visited.add(item)

#             for subitem in temp[0]:
#                 dfs(visited,graph,subitem)


    
    
# dfs(visited,graph,'A')
