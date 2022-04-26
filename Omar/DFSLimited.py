import networkx as nx
G = nx.Graph()
#creating a test graph using sheet 2 in ai
#creating nodes
G.add_node('a')
G.add_node('b')
G.add_node('c')
G.add_node('d')
G.add_node('s')
G.add_node('g')
#creating edges
G.add_edge('s', 'a', weight=1)
G.add_edge('s', 'g', weight=12)
G.add_edge('a', 'b', weight=3)
G.add_edge('b', 'd', weight=3)
G.add_edge('a', 'c', weight=1)
G.add_edge('c', 'd', weight=1)
print(nx.number_of_nodes(G))

visited=[]
edgesVisited=[]



#function when called return list with visited edges and visited nodes when bfs is used
def dfs_iterate_till_goal(MGraph,start,Goal,Depthlimit):
#add the start node immediatly
    visited.append(start)
    
    NodesIterator=nx.dfs_successors(MGraph, source=start,depth_limit=Depthlimit)
    
    EdgeIterator=nx.dfs_edges(MGraph,source=start,depth_limit=Depthlimit)
    Edgelist=list(EdgeIterator)
    
    for i in Edgelist:
        edgesVisited.append(i)
        if(i[1]==Goal):
            break
    
    for succesors in NodesIterator:
        for childnodes in succesors:
            visited.append(childnodes)
            if(childnodes==Goal):
                return visited,edgesVisited        
    return visited,edgesVisited
            
            
def main():            
    dfs_iterate_till_goal(G,'s','g')
    
    for i in visited:
        print(i)
    for i in edgesVisited:
        print(i) 
main()