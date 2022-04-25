import networkx as nx
G = nx.path_graph(5)
T = nx.dfs_tree(G, source=0, depth_limit=2)
list(T.edges())
[(0, 1), (1, 2)]
T = nx.dfs_tree(G, source=0)
list(T.edges())
[(0, 1), (1, 2), (2, 3), (3, 4)]
