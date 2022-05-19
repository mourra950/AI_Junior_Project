import networkx as nx

g=nx.Graph()
g.add_node('s',h=13)
g.add_node('a',h=12)
g.add_node('b',h=4)
g.add_node('c',h=7)
g.add_node('d',h=3)
g.add_node('e',h=8)
g.add_node('f',h=2)
g.add_node('h',h=4)
g.add_node('i',h=9)
g.add_node('g',h=0)
g.add_edge('s', 'a',weight=3)
g.add_edge('s', 'b',weight=2)
g.add_edge('a', 'd',weight=1)
g.add_edge('a', 'c',weight=4)
g.add_edge('b', 'e',weight=3)
g.add_edge('b', 'f',weight=1)
g.add_edge('e', 'h',weight=5)
g.add_edge('f', 'i',weight=2)
g.add_edge('f', 'g',weight=3)

H_table=nx.get_node_attributes(g,"h")
print(H_table)


def path_f_cost(path):
    g_cost=0
    for(node,cost) in path:
        g_cost+=cost
    last_node=path[-1][0]
    h_cost=H_table[last_node]
    f_cost=g_cost+h_cost
    return f_cost,last_node


def A_visited(Graph,s,g):#return list of nodes
    graph1=dict(Graph.adjacency())
    graph={}
    print(graph1.keys())
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
        queue.sort(key=path_f_cost)
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

def A_visited_nodes(g,start,Goals):
    lst=list(A_visited(g,start,Goals))

    print(lst)
    
