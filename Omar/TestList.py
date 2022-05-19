visited = []
edgesVisited = []
import networkx as nx
G = nx.Graph()
G.add_node('a',h=12)
G.add_node('b',h=4)
G.add_node('c',h=7)
G.add_node('d',h=3)
G.add_node('e',h=8)
G.add_node('f',h=2)
G.add_node('h',h=4)
G.add_node('i',h=9)
G.add_node('s',h=13)
G.add_node('g',h=0)
G.add_edge('s', 'a',weight=3)
G.add_edge('s', 'b',weight=4)
G.add_edge('a', 'c',weight=7)
G.add_edge('a', 'd',weight=3)
G.add_edge('b', 'e',weight=8)
G.add_edge('b', 'f',weight=2)
G.add_edge('e', 'h',weight=4)
G.add_edge('f', 'i',weight=9)
G.add_edge('f', 'g',weight=0)

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
        if node in Goal:
            return path
        # enumerate all adjacent nodes, construct a
        # new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)


def bfs_path(MGraph, start, Goal):  # we need to make goal list
    cost = 0
    Iterator = nx.bfs_successors(MGraph, source=start)
    adj = {}
    for i in Iterator:
        adj[i[0]] = i[1]
    # get the path
    path = bfspath(adj, start, Goal)
    for i in range(len(path) - 1):
        cost += MGraph[path[i]][path[i + 1]]['weight']
    return path, cost


# function when called return list with visited edges and visited nodes when bfs is used
def bfs_iterate_till_goal(MGraph, start, Goal):  # we need to make goal list
    # cost=0
    # Iterator=nx.bfs_successors(MGraph, source=start)
    # adj={}
    # for i in Iterator:
    #     adj[i[0]]=i[1]
    # #get the path
    # path=bfspath(adj,start,Goal)
    # for i in range(len(path)-1):
    #     cost+=MGraph[path[i]][path[i+1]]['weight']

    # networkx function that return a list sorted by visited nodes
    T = nx.bfs_tree(MGraph, source=start)
    for i in T:
        visited.append(i)
        if (i in Goal):
            return visited
test='5,6,7'
test1=test.split(',')
print(test1)
for i in test1:
    print(i)