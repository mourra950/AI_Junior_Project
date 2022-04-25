import networkx as nx
g=nx.Graph()
g.add_node(1,h=3,id=1,parent=None)
g.add_node(3,h=6,id=3)
g.add_node(2,h=0,id=2)
g.add_edge(1,2,weight=6)
g.add_edge(1,3,weight=4)
g.add_node(4,h=0,id=1)
g.add_edge(3,4,weight=10)

def getPath(node):
    path=[]
    cost=0
    path.append(node)
    while not(g.nodes[node]['parent'] is None):
        path.append(g.nodes[node]['parent'])
        cost += nx.get_edge_attributes(g, 'weight')[(g.nodes[node]['parent'],node)]
        node=g.nodes[node]['parent']
    path.reverse()
    return path,cost

def getH(node):
    return g.nodes[node]['h']
def greedy(start,goal):
    fringe=[]
    visited=[]
    if not(start in g.nodes):
        print("not in the graph")
        return
    else:
        fringe.append(start)
        x=fringe[0]
        while not(len(fringe)==0):
            x=fringe[0]
            visited.append(x)
            fringe.pop(0)
            if x in goal:
                print("Goal is "+ str(x),sep=" ")
                print(getPath(x))
                return
            for y in nx.all_neighbors(g,x):
                if not(y in visited):
                    fringe.append(y)
                    nx.set_node_attributes(g, {y: x}, name="parent")

        fringe.sort(key=getH)

goal=[4]
greedy(1,goal)
