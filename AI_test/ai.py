import matplotlib.pyplot as plt
import networkx as nx
from sympy import root
from tkinter import*
from tkinter import Button
import tkinter as tk
from tkinter import ttk
root = Tk()
root.title('Searching App')
# root.iconbitmap('')
root.geometry("1000x800")
G=nx.Graph()
#G.add_node("Tom")
#G.add_node("Jerry")
#for i in G:
    #print(i) 
#print(list(G))
#print(nx.number_of_nodes(G))
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
myBtn1 = Button(root, text="Tap to insert node", padx=20,pady=20, bg='white', fg='black', command=click)
myBtn1.pack()
myBtn2 = Button(root, text="Tap to connect edges", padx=20,pady=20, bg='white', fg='black', command=join)
myBtn2.pack()


#names=[("shaimaa","moahmed"),("a","b"),("c","d"),("e","f")]
#G.add_edges_from(names)
#G.remove_edge("a","b")

root.mainloop()