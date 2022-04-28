# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os

import networkx as nx
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from pyvis.network import Network
from PyQt5 import QtWebEngineWidgets
g=nx.DiGraph()
def addNode(node,heuiristic):
    g.add_node(node,h=heuiristic,id=node)
def addEdge(froom,to,w):
    g.add_edge(froom,to,weight=w)







def getPath(node):
    path=[]
    #cost=0
    path.append(node)
    while not(g.nodes[node]['parent'] is None):
        path.append(g.nodes[node]['parent'])
        #cost += nx.get_edge_attributes(g, 'weight')[(g.nodes[node]['parent'],node)]
        node=g.nodes[node]['parent']
    path.reverse()
    return path

def getH(node):
    return g.nodes[node]['h']
def greedy(g,start,goal):
    fringe=[]
    visited=[]
    if not(start in g.nodes):
        print("not in the graph")
        return
    else:
        fringe.append(start)
        x=fringe[0]
        while not(len(fringe)==0):
            x=fringe[0]
            visited.append(x)
            fringe.pop(0)
            if x in goal:
                print("Goal is "+ str(x),sep=" ")
                print(getPath(x))
                return getPath(x)
            for y in nx.all_neighbors(g,x):
                if not(y in visited):
                    fringe.append(y)
                    nx.set_node_attributes(g, {y: x}, name="parent")

            fringe.sort(key=getH)
class Ui_MainWindow(object):
    def showPath(self,path):
        N = Network(height='100%', width='100%', directed=True)
        # N.from_nx(g)
        for i in nx.nodes(g):
            if i in path:
                N.add_node(i,color='#643A71')
            else:
                N.add_node(i)
        for i in nx.nodes(g):
            for j in nx.neighbors(g, i):
                N.add_edge(i, j,color='#Fcc201')
        N.write_html('Graph.html')
        self.web.load(QUrl.fromLocalFile(os.path.abspath(os.path.join(os.path.dirname(__file__), "Graph.html"))))

    def greedygui(self,graph):
        p=greedy(g,1,[4])
        print(p)
        self.showPath(p)

    def getnodeID(self):
        return int(self.lineEdit_3.text())

    def getnodeH(self):
        return int(self.lineEdit_4.text())

    def getedgeFrom(self):
        return int(self.lineEdit_2.text())

    def getedgeTo(self):
        return int(self.lineEdit.text())
    def addNodegui(self):
        g.add_node(self.getnodeID(),h=self.getnodeH(),id=self.getnodeID(),parent=None)
        self.lineEdit_4.clear()
        self.lineEdit_3.clear()
        self.visualize()

    def addEdgegui(self):
        g.add_edge(self.getedgeFrom(),self.getedgeTo())
        self.visualize()

    def visualize(self):
        N = Network(height='100%', width='100%', directed=True)
        #N.from_nx(g)
        for i in nx.nodes(g):
            N.add_node(i)
        for i in nx.nodes(g):
            for j in nx.neighbors(g,i):
                N.add_edge(i,j,color='#Fcc201')
        N.write_html('Graph.html')
        self.web.load(QUrl.fromLocalFile(os.path.abspath(os.path.join(os.path.dirname(__file__), "Graph.html"))))
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Greedy Test")
        MainWindow.resize(808, 603)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(380, 0, 421, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.web = QtWebEngineWidgets.QWebEngineView(self.verticalLayoutWidget)
        self.web.setObjectName("web")
        self.verticalLayout.addWidget(self.web)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 211, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(220, 120, 161, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 230, 211, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(220, 40, 161, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Insert Node"))
        self.pushButton_2.clicked.connect(lambda :self.addNodegui())
        self.pushButton.clicked.connect(lambda: self.addEdgegui())
        self.pushButton.setText(_translate("MainWindow", "Insert Edge"))
        self.pushButton_3.setText(_translate("MainWindow", "Solve"))
        self.pushButton_3.clicked.connect(lambda: self.greedygui(g))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
