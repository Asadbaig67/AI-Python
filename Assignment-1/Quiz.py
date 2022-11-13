from queue import PriorityQueue

graph = {
  'S' : [[3,'A'],[2,'D']],
  'A' : [[10,'C'],[5,'B']],
  'D' : [[1,'B'],[4,'E']],
  'C' : [[4,'G']],
  'B' : [[1,'E'],[2,'C']],
  'E' : [[3,'G']],
  'G': []
}
heuristic={
    'S' :7,
    'A' :9,
    'D' :5,
    'C' :2,
    'B' :4,
    'E' :3,
    'G': 0,
}

# Using PriorityQueue so that we dont have to explicitly sort the values
q = PriorityQueue()

# Function To Calculate Path Cost And Heuristic Cost
def calculateTotalCost(preCost,item,heuristic):
    totalCost=preCost+item[0]+heuristic[item[1]]
    return [totalCost,item[0],item[1]]

# Function For Greedy DFS
def gdfs(graph,node,goal,heuristic,previousPathCost):

    # Checking if the goal has reached or not
    if node==goal:
        print(node)
        return

    # Printing the node with shortest F(n)
    print(node,end="->")
   
    # Loop to calculate the cost F(n) of childs of the Parent Node
    for item in graph[node]:
        cost=calculateTotalCost(previousPathCost,item,heuristic)
        q.put(cost)

    # the shortest path from the parent
    currnode=q.get()
    # print("Total Cost")
    # print(currnode[0])
    
    # In this case we do not need back tracking that is why we empty the queue everytime to remove chances of backtracking
    while not q.empty():
        q.get()

    # Adding the cost from starting node to the currnode
    previousPathCost=previousPathCost+currnode[1]
    print("Total Cost Till ",currnode[2])
    print(previousPathCost)

    # Calling the recursive function
    gdfs(graph,currnode[2],goal,heuristic,previousPathCost)
# End Of function


# Cost initially is zero from starting node
previousPathCost=0

gdfs(graph,'S','G',heuristic,previousPathCost)

      