class Node:
    def _init_(self,val):
        self.val=val
        self.edges=[]
class Graph:
    def _init_(self,nodes=[]):
        self.nodes=nodes
    def add_node(self,val):
        newNode=Node(val)
        self.nodes.append(newNode)
    def add_edge(self,node1,node2):
        node1.edges.append(node2)
        node2.edges.append(node1)
    def BFS(self):
        if self.node is None:    
            return []
        visited,toVisit=[] ,[self.nodes[0]]
        while toVisit:
            node=toVisit.pop()
            visited.append(node)
            print(node.val)
            for nd in node.edges:
                if nd not in visited and nd not in toVisit:
                    toVisit.insert(0,nd)
            return visited
graph=Graph()
graph.add_node(5)
graph.add_node(6)
graph.add_node(7)
graph.add_node(8)
graph.add_node(9)
graph.add_node(10)
graph.add_edge(graph.nodes[0],graph.nodes[1])
graph.add_edge(graph.nodes[2],graph.nodes[3])
graph.add_edge(graph.nodes[3],graph.nodes[4])
graph.BFS()

