from queue import Queue
adj_list={"A":["B","D"] , "B":["C","D"] ,
"D":["A","E","F"]
}
visited={}   
level={}     
parent={}    
bfs_traversal_output=[]
queue =Queue() 
for node in adj_list.keys(): 
    visited[node]=False
    parent[node]=None
    level[node]=-1
print(visited)   
print(level)
print(parent)
start="A"
Goal="D"
visited[start]=True
level[start]=0
queue.put(start)
while not queue.empty() and visited[Goal] ==False :
    u=queue.get()
    bfs_traversal_output.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[u]=True
            parent[v]=u
            level[v]=level[u]+1
            queue.put(start)
print(bfs_traversal_output)
v="D"
path=[]
while v is not None :
    path.append(v)
    v=parent[v]
path.reverse()
print(path)
