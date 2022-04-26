from turtle import pos
import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
def uniform_cost(G,start,goal):
    visited=[]
    queue=[[start,0]]
    while queue:
        queue.sort(key=path_cost)
        path=queue.pop(0)
        node=path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node==goal:
            return path
        else:
            adjacent_nodes=G.get(node,[])
            for (node2,cost)in adjacent_nodes:
                new_path=path.copy()
                new_path.append(node2,cost)
                queue.append(new_path)
                
G.add_edge('a','b',weight=3)
G.add_edge('a','c',weight=2)
G.add_edge('c','e',weight=5)
G.add_edge('c','f',weight=8)
G.add_edge('a','d',weight=7)
pos=nx.spring_layout(G)
nx.draw_networkx(G,pos,with_labels=True,node_size=1500)
nx.draw_networkx_edge_labels (G,pos,edge_labels=nx.get_edge_attributes(G,'weight'))
print("shortest path from b to f is :" , nx.shortest_path(G,'b','f',weight='weight'))
plt.show()