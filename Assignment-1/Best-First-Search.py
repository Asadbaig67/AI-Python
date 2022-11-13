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
graph = {
  'Arad' : [[140,'Sibiu'],[118,'Timisoara'],[75,'Zerind']],
  'Sibiu' : [[140,'Arad'], [99,'Fagaras'],[151,'Oradea'],[80,'Rimnicu Vilcea']],
  'Timisoara' : [[118,'Arad'],[111,'Lugoj']],
  'Zerind' : [[75,'Arad'],[71,'Oradea']],
  'Fagaras' : [[99,'Sibiu'],[211,'Bucharest']],
  'Oradea' : [[71,'Zerind'],[151,'Sibiu']],
  'Rimnicu Vilcea' : [[146,'Craiova'],[80,'Sibiu'],[97,'Pitesti']],
  'Lugoj' : [[111,'Timisoara'],[70,'Mehadia']],
  'Craiova' : [[146,'Rimnicu Vilcea'],[120,'Drobeta'],[138,'Pitesti']],
  'Pitesti' : [[97,'Rimnicu Vilcea'],[138,'Craiova'],[101,'Bucharest']],
  'Mehadia' : [[70,'Lugoj'],[75,'Drobeta']],
  'Drobeta' : [[75,'Mehadia'],[120,'Craiova']],
  'Bucharest' : [[101,'Pitesti'],[211,'Fagaras'],[90,'Giurgiu'],[85,'Urziceni']],
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

BFS(graph,'Arad','Bucharest')




