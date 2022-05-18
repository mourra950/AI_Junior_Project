import networkx as nx
# G = nx.Graph()
# #creating a test graph using sheet 2 in ai
# #creating nodes
# G.add_node('a')
# G.add_node('b')
# G.add_node('c')
# G.add_node('d')
# G.add_node('s')
# G.add_node('g')
# G.add_node('gs')

# #creating edges
# G.add_edge('s', 'gs', weight=12)
# G.add_edge('gs', 'g', weight=12)
# G.add_edge('s', 'a', weight=1)
# G.add_edge('a', 'b', weight=3)
# G.add_edge('b', 'd', weight=3)
# G.add_edge('a', 'c', weight=1)
# G.add_edge('c', 'd', weight=1)

visited=[]
edgesVisited=[]

def bfspath(graph, start, Goal):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == Goal:
            return path
        # enumerate all adjacent nodes, construct a 
        # new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
def bfs_path(MGraph,start,Goal):#we need to make goal list
    cost=0
    Iterator=nx.bfs_successors(MGraph, source=start)
    adj={}
    for i in Iterator:
        adj[i[0]]=i[1]
    #get the path
    path=bfspath(adj,start,Goal)
    for i in range(len(path)-1):
        cost+=MGraph[path[i]][path[i+1]]['weight']
    return path,cost
#function when called return list with visited edges and visited nodes when bfs is used
def bfs_iterate_till_goal(MGraph,start,Goal):#we need to make goal list
    cost=0
    Iterator=nx.bfs_successors(MGraph, source=start)
    adj={}
    for i in Iterator:
        adj[i[0]]=i[1]
    #get the path
    path=bfspath(adj,start,Goal)
    for i in range(len(path)-1):
        cost+=MGraph[path[i]][path[i+1]]['weight']
    
    #networkx function that return a list sorted by visited nodes
    T = nx.bfs_tree(MGraph, source=start)
    for i in T:
        visited.append(i)
        if(i==Goal):
            return visited,path,cost

        
        
# #/////////////////////////////////////////////////////////////////////////////////////
# #networkx function that return a list sorted by visited edges    
#     EdgeIterator=nx.dfs_edges(MGraph,source=start)
# #turn the edge to list
#     Edgelist=list(EdgeIterator)
# #create a list of visited edges until goal
#     for i in Edgelist:
        
#         edgesVisited.append(i)
#         if(i[1]==Goal):
#             break
# #create list of visited nodes until goal
#     for succesors in NodesIterator:
#         for childnodes in succesors[1]:
#             visited.append(childnodes)
#             if(childnodes==Goal):
#                 return visited,edgesVisited 
# #return the 2 lists
#     return visited,edgesVisited 
           
            
            
#test drive            
# def main():
#     bfs_iterate_till_goal(G,'s','g')
# main()