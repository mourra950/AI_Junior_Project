import networkx as nx
# g=nx.Graph()
# g.add_node('s',h=13)
# g.add_node('a',h=12)
# g.add_node('b',h=4)
# g.add_node('c',h=7)
# g.add_node('d',h=3)
# g.add_node('g',h=0)



# g.add_edge('s', 'a',weight=1)

# g.add_edge('a', 'b',weight=3)
# g.add_edge('a', 'c',weight=1)
# g.add_edge('b', 'd',weight=3)
# g.add_edge('c', 'd',weight=1)
# g.add_edge('c', 'g',weight=2)
# g.add_edge('d', 'g',weight=3)
# g.add_edge('s', 'g',weight=12)

# g.add_edge(1,5,weight=3)


def path_cost(path):
    total_cost=0
    for(node,cost) in path:
        total_cost+=cost
    return total_cost,path[-1][0]


def ucs_visited(Graph,s,g):#return list of nodes
    graph1=dict(Graph.adjacency())
    graph={}

    key=list(graph1.keys())
    count=0
    for i in graph1.values():
        temp1=list()
        for j in i:
            temp=list(i.get(j).values())
            for e in temp:
                temp1.append((j,int(e)))
        graph[key[count]]=temp1
        count+=1
    visited=[]
    queue=[[(s,0)]]
    while queue:
        queue.sort(key=path_cost)
        path=queue.pop(0)
        node=path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node in g:
            return visited
        else:
            adj_nodes=graph.get(node,[])
            for(node2,cost) in adj_nodes:
                new_path=path.copy()
                new_path.append((node2,cost))
                queue.append(new_path)




def UCS(Graph,Start,Goal):
    #init to the first goal so we can start comparison
    Cost=0
    solutionPath=nx.shortest_path(Graph, source=Start, target=Goal[0], weight='weight', method='dijkstra')
    for i in range(len(solutionPath)-1):
        Cost+=Graph[solutionPath[i]][solutionPath[i+1]]['weight']


    #iterate over the whole goals to find the shortest one and return it to draw it on the graph    
    for i in Goal:
        tempsolution=nx.shortest_path(Graph, source=Start, target=i, weight='weight', method='dijkstra')
        temp=0
        for i in range(len(tempsolution)-1):
            temp+=Graph[tempsolution[i]][tempsolution[i+1]]['weight']
        if Cost>temp:
            Cost=temp
            solutionPath=tempsolution
            
    return solutionPath,Cost
def ucs_visited_nodes(g,start,Goals):
    lst=list(ucs_visited(g,start,Goals))

    return lst
    

