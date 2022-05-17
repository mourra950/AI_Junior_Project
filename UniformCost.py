import networkx as nx
g=nx.Graph()
g.add_node(1)
g.add_node(3)
g.add_node(2)
g.add_edge(1,2,weight=6)
g.add_edge(1,3,weight=4)
g.add_node(4)
g.add_node(5)
g.add_edge(3,4,weight=10)
g.add_edge(1,4,weight=6)
g.add_edge(4,5,weight=2)
g.add_edge(3,5,weight=2)
def UCS(Graph,Start,Goal):
    solutionPath=nx.shortest_path(Graph, source=Start, target=Goal, weight='weight', method='dijkstra')

    Cost=0
    for i in range(len(solutionPath)-1):
        
        Cost+=Graph[solutionPath[i]][solutionPath[i+1]]['weight']
    print(Cost)
    return solutionPath,Cost
UCS(g,1,5)