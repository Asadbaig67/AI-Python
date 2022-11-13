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

def RBFS(graph,heuristic,goal,node):
    if(node==goal):
        print(node)
        return
        