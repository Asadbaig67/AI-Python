import queue
graph={
    '1':['2','4','5'],
    '2':['4','3'],
    '3':['3'],
    '4':['2','3'],
    '5':[],
    '6':['2','3']
}

queue=[]

def bfs(graph,node,goal):
    
    if node==goal:
        print(node)
    
    queue.append(node)
    while queue: #while queue is not empty
        element=queue.pop(0)
        if element==goal:
            print(element)
        print(element,end="->")
        for subnode in graph[element]:
                queue.append(subnode)

bfs(graph,'1','3')