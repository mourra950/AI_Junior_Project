
import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
G.add_node("Tom")

G.add_node("Jerry")
G.add_edge("Tom","Jerry",weight=5) #It creates nodes if they dont exist
#print(list(G))
#for i in G:
#    print(i)
#names=[("willy","jack"),("wilma","Betty"),("lalala","no"),("Tom","Jerry"),("Tom","jack"),("wilma","willy"),("willy","no")]
#G.add_edges_from(names) #better for tuples
#print(nx.nodes(G))
#G2=nx.Graph()
#G2.add_node("Lucy")
#G2.add_node("Betty")
#len(G)=nx.number_of_nodes(G)
plt.figure(1) #to make the G graph in a seperate figure
pos=nx.spring_layout(G)
nx.draw(G,pos,with_labels=True,font_size=10,font_color="#2A659A",bbox=dict(facecolor="#24517A"))
nx.draw_networkx_edge_labels(G,pos,edge_labels=nx.get_edge_attributes(G,'weight'))
#plt.figure(2)
#nx.draw(G2,node_color="red")

plt.show() 

def path_cost(path):
    total_cost=0
    for(node,cost) in path:
        total_cost+=cost
        return total_cost,path[-1][0]

    
def ucs(graph,s,g):
    visited=[]
    queue=[[(s,0)]]
    while queue:
        queue.sort(key=path_cost)
        path=queue.pop(0)
        node=path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node==g:
            return path
        else:
            adj_nodes=graph.get(node,[])
            for(node2,cost) in adj_nodes:
                new_path=path.copy()
                new_path.append((node2,cost))
                queue.append(new_path)
        
        
    
    
