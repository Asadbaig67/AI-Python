from queue import PriorityQueue

graph={
    'S':[[3,'A'],[6,'B'],[5,'C']],
    'A':[[9,'D'],[8,'E']],
    'B':[[12,'F'],[14,'G']],
    'C':[[7,'H']],
    'H':[[5,'I'],[6,'J']],
    'I':[[1,'K'],[10,'L'],[2,'M']],
    'D':[],
    'E':[],
    'F':[], 
    'G':[],
    'J':[],
    'K':[],
    'L':[],
    'M':[]
}
q = PriorityQueue()

def BFS(graph,node,goal):
    if node==goal: 
        print(node)
        return
    print(node,end=" ")
    # if len(graph[node])>=2:
    for items in graph[node]:
        q.put(items)
    # print(q.queue)    
    while not q.empty():
    # while q:
        currnode=q.get()
        # print(currnode[1])
        if currnode[1]==goal: #Checking if the goal is already reached or not
            print(currnode[1])
            return
        print(currnode[1],end=" ")
        # if len(graph[currnode[1]])<1:
        #     continue
        for items in graph[currnode[1]]:
            # print(items)
            q.put(items)

BFS(graph,'S','I')




