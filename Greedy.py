import networkx as nx
g=nx.Graph()
g.add_node(1,h=3,id=1,parent=None)
g.add_node(3,h=6,id=3)
g.add_node(2,h=0,id=2)
g.add_edge(1,2,weight=6)
g.add_edge(1,3,weight=4)
g.add_node(4,h=0,id=1)
g.add_edge(3,4,weight=6)



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
                print(x) # get path and get path cost
                return
            for y in nx.all_neighbors(g,x):
                if not(y in visited):
                    fringe.append(y)
        fringe.sort(key=getH)

goal=[2,4]
greedy(1,goal)
