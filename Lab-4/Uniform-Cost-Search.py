graph = {
    'A':[[8,'B'],[5,'B']],
    'B':[[1,'C'],[2,'D']],
    'C':[3,'F'],
    'D':[3,'E'],
    'E':[1,'G'],
    'G':[4,'F'],
    'F':[]
}

# Funtion to sort the nodes according to the shortest weight
def function_sort(node):
    item=graph[node]
    item.sort()
    return item



visited=[]
queue=[]



def UFC(visited,graph,node,goal):
    if node not in visited:
        visited.append(node)
        queue.append(node)
    while queue:
        node=queue.pop(0)  
        if node==goal:
            print(node)
            return

        print(node,end=" ")
        
        if len(graph[node])>=2:
            sortednode=function_sort(node)
            currnode=sortednode[0][1]
            if currnode not in visited:
                visited.append(currnode)
                queue.append(currnode)
        elif len(graph[node])==1:
            if graph[node][1] not in visited:
                visited.append(graph[node][1])
                queue.append(graph[node][1])
        else:
            continue
            


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
