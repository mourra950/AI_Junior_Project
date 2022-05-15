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
G.add_node('gs')

#creating edges
G.add_edge('s', 'gs', weight=12)
G.add_edge('gs', 'g', weight=12)
G.add_edge('s', 'a', weight=1)
G.add_edge('a', 'b', weight=3)
G.add_edge('b', 'd', weight=3)
G.add_edge('a', 'c', weight=1)
G.add_edge('c', 'd', weight=1)

visited=[]
edgesVisited=[]



#function when called return list with visited edges and visited nodes when bfs is used
def bfs_iterate_till_goal(MGraph,start,Goal):#we need to make goal list
#add the start node immediatly
    visited.append(start)
#networkx function that return a list sorted by visited nodes
    NodesIterator=nx.bfs_successors(MGraph, source=start)
    T = nx.bfs_tree(G, source=start)
    print('here')
    for i in T:
        
        visited.append(i)
        if(i==Goal):
            break
    print('here')
#networkx function that return a list sorted by visited edges    
    EdgeIterator=nx.dfs_edges(MGraph,source=start)
#turn the edge to list
    Edgelist=list(EdgeIterator)
#create a list of visited edges until goal
    for i in Edgelist:
        
        edgesVisited.append(i)
        if(i[1]==Goal):
            break
#create list of visited nodes until goal
    for succesors in NodesIterator:
        for childnodes in succesors[1]:
            visited.append(childnodes)
            if(childnodes==Goal):
                return visited,edgesVisited 
#return the 2 lists
    return visited,edgesVisited 
           
            
            
#test drive            
def main():            
    bfs_iterate_till_goal(G,'s','g')
main()