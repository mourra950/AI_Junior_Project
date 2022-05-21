
    #     print(i)
    Iterator=nx.dfs_successors(MGraph, source=start)
    adj={}
    graph1=dict(MGraph.adjacency())
    graph={}
    
    key=list(graph1.keys())
    count=0
    for i in graph1.values():
        temp1=list()
        for j in i:
            temp=list(i.get(j).values())
            for e in temp:
                temp1.append((j,int(e)))