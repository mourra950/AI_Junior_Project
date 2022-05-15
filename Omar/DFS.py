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
G.add_edge('s', 'g', weight=12)
G.add_edge('s', 'a', weight=1)

G.add_edge('a', 'b', weight=3)
G.add_edge('b', 'd', weight=3)
G.add_edge('a', 'c', weight=1)
G.add_edge('c', 'd', weight=1)
print(nx.number_of_nodes(G))

visited=[]
edgesVisited=[]



#function when called return list with visited edges and visited nodes when bfs is used
def dfs_iterate_till_goal(MGraph,start,Goal):

#networkx function that return a list sorted by visited nodes
    NodesIterator=nx.dfs_successors(MGraph, source=start)
    # print(NodesIterator)
    # for i in NodesIterator:
    #     print(i)
    
    T = nx.dfs_tree(MGraph, source=start)
    print('here')
    for i in T:
        visited.append(i)
        print(i)
        if(i==Goal):
            return visited
    print('here')
    
    
#networkx function that return a list sorted by visited edges    
    EdgeIterator=nx.dfs_edges(MGraph,source=start)
#create a list of visited edges until goal
    Edgelist=list(EdgeIterator)
#create a list of visited edges until goal
    for i in Edgelist:
        edgesVisited.append(i)
        if(i[1]==Goal):
            return visited
#create list of visited nodes until goal
    for succesors in NodesIterator:
        for childnodes in succesors:
            
            if(childnodes==Goal):
                return visited,edgesVisited
#return the 2 lists            
             
            
            
            
def main():            
    s=dfs_iterate_till_goal(G,'s','g')
    print(s)
main()