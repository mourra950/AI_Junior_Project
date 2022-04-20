import matplotlib.pyplot as plt
import networkx as nx
from tkinter import*
from tkinter import Button
import tkinter as tk
from tkinter import ttk
root = Tk()
root.title('Searching App')
root.geometry("1000x800")

class Node:
    def __init__(self, val):
        self.val = val
        self.edges = []
        self.adj_list={}

class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.adj_list={}
    def add_node(self, val):
        newNode = Node(val)
        self.nodes.append(newNode)

    def add_edge(self, node1, node2):
        node1.edges.append(node2)
        node2.edges.append(node1)
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)
    def degree(self,node):
        deg=(len(self.adj_list[node]))
        return deg
    def print_adj_list(self):
        for node in self.nodes:
            print(node," => " ,self.adj_list[node] )
        
    def bfs(self):
        if self.nodes is None:
            return []
        visited, toVisit = [], [self.nodes[0]]
        while toVisit:
            node = toVisit.pop()
            visited.append(node)
            print(node.val)
            for nd in node.edges:
                if nd not in visited and nd not in toVisit:
                    toVisit.insert(0,nd)
        return visited
    def dfs(self):
        if self.nodes is None:
            return []
        visited, toVisit = [], [self.nodes[0]]
        while toVisit:
            node = toVisit.pop()
            visited.append(node)
            print(node.val)
        for nd in node.edges:
            if nd not in visited and nd not in toVisit:
                toVisit.append(nd)
        return visited
G= nx.Graph()
e = Entry(root, width=50, fg='red', font=('Chaucer', 20))
e.pack()
def click():
    G.add_node((e.get()))
    nx.draw(G , node_color='red',with_labels=True ,font_size=8)
    plt.show()  
my_label1 = Label(root, text="from ", font=('Chaucer', 15), fg='red', padx=10, pady=10).pack()
e1 = Entry(root, width=50, fg='red', font=('Chaucer', 20))
e1.pack()
my_label2 = Label(root, text="To ", font=('Chaucer', 15), fg='red', padx=10, pady=10).pack()
e2 = Entry(root, width=50, fg='red', font=('Chaucer', 20))
e2.pack()
def join():
    list=[(e1.get(), e2.get())]
    G.add_edges_from(list)
    nx.draw(G , node_color='red',with_labels=True ,font_size=8)
    plt.show()
graph = Graph()
graph.add_node(5)
graph.add_node(3)
graph.add_node(8)
graph.add_node(1)
graph.add_node(9)
graph.add_node(2)
graph.add_node(10)

#            2
#           /
# 5 - 3 - 8 -  9 - 10
#  \    /
#     1

graph.add_edge(graph.nodes[0], graph.nodes[1])
graph.add_edge(graph.nodes[0], graph.nodes[3])
graph.add_edge(graph.nodes[1], graph.nodes[2])
graph.add_edge(graph.nodes[0], graph.nodes[1])
graph.add_edge(graph.nodes[2], graph.nodes[3])
graph.add_edge(graph.nodes[2], graph.nodes[5])
graph.add_edge(graph.nodes[2], graph.nodes[4])
graph.add_edge(graph.nodes[4], graph.nodes[6])

def BFS_click():
    graph.bfs()
    nx.draw(graph,node_color='blue', with_labels=True)   
    plt.show()
myBtn1 = Button(root, text="Tap to insert node", padx=20,pady=20, bg='white', fg='black', command=click)
myBtn1.pack()
myBtn2 = Button(root, text="Tap to connect edges", padx=20,pady=20, bg='white', fg='black', command=join)
myBtn2.pack()
myBtn3 = Button(root, text="Apply BFS", padx=20,pady=20, bg='white', fg='black', command=BFS_click)
myBtn3.pack()

root.mainloop()

