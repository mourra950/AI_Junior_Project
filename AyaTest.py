
import networkx as nx
import matplotlib.pyplot as plt
#G=nx.Graph()
#G.add_node("Tom")

#G.add_node("Jerry")
#G.add_edge("Tom","Jerry",weight=5) #It creates nodes if they dont exist
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
#plt.figure(1) #to make the G graph in a seperate figure
#pos=nx.spring_layout(G)
#nx.draw(G,pos,with_labels=True,font_size=10,font_color="#2A659A",bbox=dict(facecolor="#24517A"))
#nx.draw_networkx_edge_labels(G,pos,edge_labels=nx.get_edge_attributes(G,'weight'))
#plt.figure(2)
#nx.draw(G2,node_color="red")

#plt.show() 
visited=[]
def path_cost(path):
    total_cost=0
    for(node,cost) in path:
        total_cost+=cost
    return total_cost,path[-1][0]
#Trying PathCost function
#path=[('S',0),('D',5),('G',5)]
#print(path_cost(path))
    
def ucs(graph,s,g):#return list of nodes 
    #visited=[]
    queue=[[(s,0)]]
    while queue:
        queue.sort(key=path_cost)
        path=queue.pop(0)
        node=path[-1][0]
        print("ana hena")
        #print(node)
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
        
def ayhaga():
    
    print("Visited nodes are ")
    for i in visited:
        print (i)

        
        
                
#Testing the ucs function    
graph={
'S':[('A',2),('B',3),('D',5)],
'A':[('C',4)],
'B':[('D',4)],
'C':[('D',1),('G',2)],
'D':[('G',5)],
'G':[],
    }   

solution=ucs(graph,'A','C')
print("Solution is ", solution)
print("Path Cost is ", path_cost(solution)[0])
ayhaga()
nodes=[("S","A"),("S","B"),("S","D"),("A","C"),("B","D"),("C","D"),("C","G"),("D","G")]
graph=nx.Graph()
graph.add_edges_from(nodes)
nx.draw(graph,with_labels=True,font_size=10,font_color="#2A659A",bbox=dict(facecolor="#24517A"))
pos=nx.spring_layout(graph)
nx.draw_networkx_edge_labels(graph,pos,edge_labels=nx.get_edge_attributes(graph,'weight'))

plt.show()
#goal is a list 
#return visited nodes , path
#path cost