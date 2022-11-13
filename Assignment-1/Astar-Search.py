from queue import PriorityQueue

# graph={
#     'S':[[3,'A'],[6,'B'],[5,'C']],
#     'A':[[9,'D'],[8,'E']],
#     'B':[[12,'F'],[14,'G']],
#     'C':[[7,'H']],
#     'H':[[5,'I'],[6,'J']],
#     'I':[[1,'K'],[10,'L'],[2,'M']],
#     'D':[],
#     'E':[],
#     'F':[], 
#     'G':[],
#     'J':[],
#     'K':[],
#     'L':[],
#     'M':[]
# }
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

# EXAMPLE GRAPH NO 1 FOR A*
# graph={
#     'S':[[3,'A'],[4,'D']],
#     'A':[[3,'S'],[5,'D'],[4,'B']],
#     'D':[[4,'S'],[5,'A'],[2,'E']],
#     'B':[[4,'A'],[5,'E'],[4,'C']],
#     'E':[[2,'D'],[5,'B'],[4,'F']],
#     'C':[[4,'B']],
#     'F':[[4,'E'],[3,'G']], 
#     'G':[[3,'F']],
# }
# heuristic={
#     'S':11.0,
#     'A':10.4,
#     'D':8.9,
#     'B':6.7,
#     'E':6.9,
#     'C':4.0,
#     'F':3.0,
#     'G':0
# }

# EXAMPLE GRAPH NO 2 FOR A*
# graph={
#     'S':[[4,'B'],[3,'C']],
#     'B':[[5,'F'],[12,'E']],
#     'C':[[10,'E'],[7,'D']],
#     'F':[[16,'G']],
#     'E':[[5,'G']],
#     'D':[[4,'E']],
#     'G':[], 
# }
# heuristic={
#     'S':14,
#     'B':12,
#     'C':11,
#     'F':11,
#     'E':4,
#     'D':6,
#     'G':0,
# }
# EXAMPLE GRAPH NO 3 FOR A*
graph={
    'A':[[10,'B'],[8,'C']],
    'B':[[5,'D'],[3,'F'],[2,'E']],
    'C':[[5,'F']],
    'D':[[]],
    'E':[[2,'F']],
    'F':[[]], 
}
heuristic={
    'A':10,
    'B':27,
    'C':25,
    'D':13,
    'E':9,
    'F':0,
}

# COST FINDING FUNCTION
def calculateTotalCost(preCost,item,heuristic):
    totalCost=preCost+item[0]+heuristic[item[1]]
    return [totalCost,item[0],item[1]]


q = PriorityQueue()


# for item in graph['D']:
#     cost=calculateTotalCost(4,item,heuristic)
#     q.put(cost)

# print(q.queue)

def BFS(graph,heuristic,node,goal):
    previousPathCost=0
    if node==goal: 
        print("Goal Found ",node)
        return
    #Finding the shortest path
    print(node,end="->")

    for item in graph[node]:
        cost=calculateTotalCost(previousPathCost,item,heuristic)
        q.put(cost)
    # print(q.queue)
    # if len(graph[node])>=2:
    # for items in graph[node]:
    #     q.put(items)
    # print(q.queue)    
    while not q.empty():
    # while q:
        currnode=q.get()
        # print(currnode[0],currnode[1],currnode[2])
        
        previousPathCost=previousPathCost+currnode[1]
        # print(previousPathCost)
        # print(previousPathCost ," is for", currnode[2])
        # # print(currnode[1])

        if currnode[2]==goal: #Checking if the goal is already reached or not
            print(currnode[2])
            return
        print(currnode[2],end="->") #prints the path of the minimun cost node
        # if len(graph[currnode[1]])<1:
        #     continue
        for items in graph[currnode[2]]:
            cost=calculateTotalCost(previousPathCost,items,heuristic)
            q.put(cost)
            # print(items)
            # q.put(items)

# BFS(graph,'Arad','Bucharest')
BFS(graph,heuristic,'A','D')




