import networkx as nx
G = nx.Graph()
#creating a test graph using sheet 2 in ai
print(nx.number_of_nodes(G))

visited=[]
edgesVisited=[]

def dfspath(graph, start, Goal):
    # maintain a queue of paths
    Stack = []
    # push the first path into the queue
    Stack.append([start])
    while Stack:
        # get the first path from the queue
        path = Stack.pop(len(Stack)-1)
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
            Stack.append(new_path)

def dfs_path(MGraph,start,Goal):#we need to make goal list
    cost=0
    Iterator=nx.bfs_successors(MGraph, source=start)
    adj={}
    for i in Iterator:
        adj[i[0]]=i[1]
    #get the path
    path=dfspath(adj,start,Goal)
    for i in range(len(path)-1):
        cost+=MGraph[path[i]][path[i+1]]['weight']
    return path,cost

#function when called return list with visited edges and visited nodes when bfs is used
def dfs_iterate_till_goal(MGraph,start,Goal,Depthlimit):
    T = nx.dfs_tree(MGraph, source=start,depth_limit=Depthlimit)
    for i in T:
        visited.append(i)
        print(i)
        if(i==Goal):
            return visited
            
# def main():            
#     dfs_iterate_till_goal(G,'s','g')
    
#     for i in visited:
#         print(i)
#     for i in edgesVisited:
#         print(i) 
# main()