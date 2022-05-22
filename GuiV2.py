# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from ast import Global
from ntpath import join
import os
from turtle import color
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from pyvis.network import Network
from PyQt5 import QtWebEngineWidgets
import networkx as nx
import Algorithms.BFS as bfs
import Algorithms.DFS as dfs
import Algorithms.DFSLimited as dfps
import Algorithms.astarsearch as Astar
import Algorithms.UniformCost as Ucs


# import Greedy as gr
Gt = nx.DiGraph()
G = nx.Graph()
counter = 1


def getPath(node):
    path = []
    cost = 0
    path.append(node)
    while not (G.nodes[node]['parent'] is None):
        path.append(G.nodes[node]['parent'])
        cost += nx.get_edge_attributes(G,
                                       'weight')[(G.nodes[node]['parent'], node)]
        node = G.nodes[node]['parent']
    path.reverse()
    return path, cost


def getH(node):
    return G.nodes[node]['h']


def greedy(g, start, goal):
    fringe = []
    visited = []
    fringe.append(start)
    x = fringe[0]
    while not (len(fringe) == 0):
        x = fringe[0]
        visited.append(x)
        fringe.pop(0)
        if x in goal:
            # print("Goal is " + str(x), sep=" ")
            return visited, getPath(x)
        for y in nx.all_neighbors(g, x):
            if not (y in visited):
                fringe.append(y)
                nx.set_node_attributes(g, {y: x}, name="parent")

        fringe.sort(key=getH)


class Ui_MainWindow(object):
    def Example(self):
        print("x")
        # G.add_node('a')
        # G.add_node('b')
        # G.add_node('c')
        # G.add_node('d')
        # G.add_node('s')
        # G.add_node('g')
        # G.add_node('gs')

        # #creating edges
        # G.add_edge('s', 'a', weight=1)
        # G.add_edge('a', 'b', weight=3)
        # G.add_edge('b', 'd', weight=3)
        # G.add_edge('a', 'c', weight=1)
        # G.add_edge('c', 'd', weight=1)
        
    #show the path 🎉🎈 
    def pathshow(self):
        color='#FF0000'
        self.GraphType()
        try:
            if self.getAlgoSelection() == "BFS":
                path, cost = bfs.bfs_path(G, self.getS(), self.getGs())
                temp = ''.join(path)
                temp += ' and the cost is: ' + str(cost)
                self.showPathcost.setText(temp)
                self.showPath(path, len(path), color)
            elif self.getAlgoSelection() == "Greedy":
                x, pathandcost = greedy(G, self.getS(), self.getGs())
                path, cost = pathandcost
                temp = ''.join(path)
                temp += ' and the cost is: ' + str(cost)
                self.showPathcost.setText(temp)
                self.showPath(path, len(path), color)
            elif self.getAlgoSelection() == "DFS":
                path, cost = dfs.dfs_path(G, self.getS(), self.getGs())
                temp = ''.join(path)
                temp += ' and the cost is: ' + str(cost)
                self.showPathcost.setText(temp)
                self.showPath(path, len(path), color)
            elif self.getAlgoSelection() == "Uniform Cost":
                path, cost = Ucs.UCS(G, self.getS(), self.getGs())
                temp = ''.join(path)
                temp += ' and the cost is: ' + str(cost)
                self.showPathcost.setText(temp)
                self.showPath(path, len(path), color)
                # Add UCS call
            elif self.getAlgoSelection() == "Iterative Deepening":
                path, cost = dfs.dfs_path(G, self.getS(), self.getGs())
                temp = ''.join(path)
                temp += ' and the cost is: ' + str(cost)
                self.showPathcost.setText(temp)
                self.showPath(path, len(path), color)
            elif self.getAlgoSelection() == "A*":
                path = nx.astar_path(G, self.getS(), self.getGs()[0], heuristic=None, weight='weight')
                cost = nx.astar_path_length(G, self.getS(),self.getGs()[0], heuristic=None, weight='weight')
                for i in self.getGs():
                    temppath = nx.astar_path(G, self.getS(), i, heuristic=None, weight='weight')
                    tempcost = nx.astar_path_length(G, self.getS(),i, heuristic=None, weight='weight')
                    if cost>tempcost:
                        cost=tempcost
                        path=temppath
                temp = ''.join(path)
                temp += ' and the cost is: ' + str(cost)
                self.showPathcost.setText(temp)
                self.showPath(path, len(path), color)
        except:
            pass

    def Reset(self):
        global counter
        counter = 1
        self.draw()
        self.showPathcost.clear()
        self.infobox('Reset done', 'hope you keep enjoying the program😉')

    def showPath(self, visited, counter, Mcolor):
        N = Network(height='100%', width='100%', directed=True)
        count = 0
        for i in visited:
            if counter > count:
                N.add_node(i, color=Mcolor)
                count += 1
            else:
                N.add_node(i)
        for i in nx.nodes(G):
            if i not in visited:
                N.add_node(i)
        for i in nx.nodes(G):
            for j in nx.neighbors(G, i):
                N.add_edge(i, j, color='#Fcc201')
        N.write_html('Graph.html')
        self.web.load(QUrl.fromLocalFile(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "Graph.html"))))

    def loadGraph(self):
        global counter
        color='#FFFF00'
        self.GraphType()
        try:
            if self.getAlgoSelection() == "Greedy":
                visited, path = greedy(G, self.getS(), self.getGs())
                self.showPath(visited, counter, color)
                counter += 1
                visited.clear()
            elif self.getAlgoSelection() == "BFS":
                visited = bfs.bfs_iterate_till_goal(G, self.getS(), self.getGs())
                self.showPath(visited, counter, color)
                counter += 1
                visited.clear()
            elif self.getAlgoSelection() == "DFS":
                visited = dfs.dfs_iterate_till_goal(G, self.getS(), self.getGs())
                print(visited)
                self.showPath(visited, counter, color)
                counter += 1
                visited.clear()
            elif self.getAlgoSelection() == "A*":
                visited = Astar.A_visited_nodes(G, self.getS(), self.getGs())
                self.showPath(visited, counter, color)
                counter += 1
                visited.clear()
            elif self.getAlgoSelection() == "Uniform Cost":
                visited = Ucs.ucs_visited_nodes(G, self.getS(), self.getGs())
                
                self.showPath(visited, counter, color)
                counter += 1
                visited.clear()
            elif self.getAlgoSelection() == "Iterative Deepening":
                visited = dfps.dfs_iterate_till_goal(G, self.getS(), self.getGs())
                self.showPath(visited, counter, color)
                counter += 1
                visited.clear()
        except:
            pass
        # Iterative Deepening




    def getS(self):
        if (self.StartNode.text() != ''):
            if (self.StartNode.text() in nx.nodes(Gt)):

                return self.StartNode.text()
            else:
                self.errorbox('start error', 'start is not found')
        else:
            self.errorbox('start error', 'start cant be empty')
        

    def getGs(self):
        temp=list(self.Goals.text().split(','))
        
        return temp

    def errorbox(self, Title, Text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(Text)
        msg.setWindowTitle(Title)
        msg.exec_()

    def infobox(self,Title,Text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(Text)
        msg.setWindowTitle(Title)
        msg.exec_()
    # custom funtions
    def GraphType(self):
        global G
        if (self.Directed.isChecked()):
            G = Gt
        else:
            G = Gt.to_undirected()
        

    def getNodeName(self):
        return self.InsertedNode.text()

    def getHe(self):
        return self.HeuristicNode.text()

    def getWe(self):
        return self.WeightEdge.text()

    def getFromNode(self):
        return self.FromNode.text()

    def getToNode(self):
        return self.ToNode.text()

    def insertNode(self):
        if self.getNodeName() == "":
            self.errorbox('Node error', 'N can not be null')
        elif self.getNodeName() in nx.nodes(Gt):
            self.errorbox('Exists already', 'Node exists')
        else:
            if (self.getHe().isdigit()):

                Gt.add_node(self.getNodeName(), h=int(
                    self.getHe()), parent=None)
                print(G.nodes)
                self.draw()
                self.HeuristicNode.clear()
                self.InsertedNode.clear()
            else:
                self.errorbox('Heuristic error', 'H must be integer')

    def insertEdge(self):
        if self.getFromNode() == "":
            self.errorbox("Node 1 Error","Please insert node 1")
        elif self.getToNode()=="":
            self.errorbox("Node 2 Error","Please insert node 2")
        elif not self.getFromNode() in nx.nodes(G):
            self.errorbox("Node 1 Error","Node 1 is not found")
        elif not self.getToNode() in nx.nodes(G):
            self.errorbox("Node 2 Error","Node 2 is not found") 
        elif self.getWe()=="":
            self.errorbox("Weight Error","Please insert weight")
        else:
            if (self.getWe().isdigit()):
                Gt.add_edge(self.getFromNode(), self.getToNode(),
                           weight=int(self.getWe()))
                self.ToNode.clear()
                self.FromNode.clear()
                self.draw()
            else:
                self.errorbox('error', 'weight must be an integer')

            self.WeightEdge.clear()

    def deleteNode(self):
        if self.getNodeName() not in nx.nodes(Gt):
            self.errorbox('error', 'Node doesnt exist')
        else:
            Gt.remove_node(self.getNodeName())
            self.draw()
        self.InsertedNode.clear()

    def draw(self):
        self.GraphType()
        # if(self.Directed.isChecked()):
        N = Network(height='100%', width='100%', directed=True)
        # else:
        #     N = Network(height='100%', width='100%',directed=True)
        for i in nx.nodes(G):
            N.add_node(i,title=str(G.nodes[i]['h']))
        for i in nx.nodes(G):
            for j in nx.neighbors(G, i):
                N.add_edge(i, j, color='#Fcc201', title=G[i][j]['weight'])
        N.write_html('Graph.html')
        self.web.load(QUrl.fromLocalFile(os.path.abspath(
            os.path.join(os.path.dirname(__file__), "Graph.html"))))

    def getAlgoSelection(self):
        return self.comboBox.currentText()

    def deleteEdge(self):
        if self.getFromNode() == "":
            self.errorbox("Node 1 Error","Please insert node 1")
        elif self.getToNode()=="":
            self.errorbox("Node 2 Error","Please insert node 2")
        elif not self.getFromNode() in nx.nodes(G):
            self.errorbox("Node 1 Error","Node 1 is not found")
        elif not self.getToNode() in nx.nodes(G):
            self.errorbox("Node 2 Error","Node 2 is not found") 
        elif not Gt.has_edge(self.getFromNode(), self.getToNode()):
            self.errorbox('error', 'Enter Valid edge')
        else:
            Gt.remove_edge(self.getFromNode(), self.getToNode())
            self.draw()
        self.ToNode.clear()
        self.FromNode.clear()

        # end of custom functions

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 623)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(600, 1200))
        self.widget.setStyleSheet("QGroupBox {border:0;}\n"
                                  "font: 75 14pt \"8514oem\";")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 7, -1, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_4.setStyleSheet("border-color: rgba(255, 255, 255, 0);")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setContentsMargins(-1, 30, -1, 30)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.InsertNode = QtWidgets.QPushButton(self.groupBox_4)
        self.InsertNode.setObjectName("InsertNode")
        self.verticalLayout_4.addWidget(self.InsertNode)
        self.DeleteNode = QtWidgets.QPushButton(self.groupBox_4)
        self.DeleteNode.setObjectName("DeleteNode")
        self.verticalLayout_4.addWidget(self.DeleteNode)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.InsertEdge = QtWidgets.QPushButton(self.groupBox_5)
        self.InsertEdge.setObjectName("InsertEdge")
        self.verticalLayout_5.addWidget(self.InsertEdge)
        self.DeleteEdge = QtWidgets.QPushButton(self.groupBox_5)
        self.DeleteEdge.setObjectName("DeleteEdge")
        self.verticalLayout_5.addWidget(self.DeleteEdge)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setStyleSheet("\n"
                                    "border:0;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setContentsMargins(-1, 30, 9, 80)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.InsertedNode = QtWidgets.QLineEdit(self.groupBox_2)
        self.InsertedNode.setToolTip("")
        self.InsertedNode.setObjectName("InsertedNode")
        self.verticalLayout_8.addWidget(self.InsertedNode)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.HeuristicNode = QtWidgets.QLineEdit(self.groupBox_2)
        self.HeuristicNode.setObjectName("HeuristicNode")
        self.verticalLayout_8.addWidget(self.HeuristicNode)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setContentsMargins(-1, 30, -1, 73)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.FromNode = QtWidgets.QLineEdit(self.groupBox_3)
        self.FromNode.setObjectName("FromNode")
        self.verticalLayout_3.addWidget(self.FromNode)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.ToNode = QtWidgets.QLineEdit(self.groupBox_3)
        self.ToNode.setObjectName("ToNode")
        self.verticalLayout_3.addWidget(self.ToNode)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.WeightEdge = QtWidgets.QLineEdit(self.groupBox_3)
        self.WeightEdge.setObjectName("WeightEdge")
        self.verticalLayout_3.addWidget(self.WeightEdge)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_6 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_6.setMinimumSize(QtCore.QSize(210, 0))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setFlat(True)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.groupBox_6)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_6.addWidget(self.comboBox)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_7.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.groupBox_7)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.StartNode = QtWidgets.QLineEdit(self.groupBox_7)
        self.StartNode.setText("")
        self.StartNode.setObjectName("StartNode")
        self.verticalLayout_7.addWidget(self.StartNode)
        self.label_8 = QtWidgets.QLabel(self.groupBox_7)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.Goals = QtWidgets.QLineEdit(self.groupBox_7)
        self.Goals.setObjectName("Goals")
        self.verticalLayout_7.addWidget(self.Goals)
        self.verticalLayout_6.addWidget(self.groupBox_7)
        self.StartAlgo = QtWidgets.QPushButton(self.groupBox_6)
        self.StartAlgo.setObjectName("StartAlgo")
        self.verticalLayout_6.addWidget(self.StartAlgo)
        self.Directed = QtWidgets.QRadioButton(self.groupBox_6)
        self.Directed.setObjectName("Directed")

        self.verticalLayout_6.addWidget(self.Directed)
        self.ResetGraph = QtWidgets.QPushButton(self.groupBox_6)
        self.ResetGraph.setObjectName("ResetGraph")
        self.verticalLayout_6.addWidget(self.ResetGraph)
        self.NextButton = QtWidgets.QPushButton(self.groupBox_6)
        self.NextButton.setObjectName("NextButton")
        self.verticalLayout_6.addWidget(self.NextButton)
        self.pathShow = QtWidgets.QPushButton(self.groupBox_6)
        self.pathShow.setObjectName("pathShow")
        self.verticalLayout_6.addWidget(self.pathShow)
        self.showPathcost = QtWidgets.QLineEdit(self.groupBox_6)
        self.showPathcost.setEnabled(False)
        self.showPathcost.setObjectName("showPathcost")
        self.verticalLayout_6.addWidget(self.showPathcost)
        self.horizontalLayout_2.addWidget(self.groupBox_6)
        self.horizontalLayout.addWidget(self.widget)
        self.web = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.web.setMinimumSize(QtCore.QSize(250, 0))
        self.web.setStyleSheet("border-color: rgb(0, 255, 0);\n"
                               "border: 4px;\n"
                               "background-color: rgb(170, 255, 0);")
        self.web.setObjectName("web")
        self.horizontalLayout.addWidget(self.web)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1120, 26))
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
        # Node functions
        self.InsertNode.setText(_translate("MainWindow", "Insert Node"))
        self.InsertNode.clicked.connect(lambda: self.insertNode())
        self.DeleteNode.setText(_translate("MainWindow", "Delete Node"))
        self.DeleteNode.clicked.connect(lambda: self.deleteNode())
        # end
        #
        # Edge function
        self.InsertEdge.setText(_translate("MainWindow", "Insert Edge"))
        self.InsertEdge.clicked.connect(lambda: self.insertEdge())
        self.DeleteEdge.setText(_translate("MainWindow", "Delete Edge"))
        self.DeleteEdge.clicked.connect(lambda: self.deleteEdge())
        # end
        self.label_3.setText(_translate("MainWindow", "Node name"))
        self.label_5.setText(_translate("MainWindow", "Node Heuristics"))
        self.label_6.setText(_translate("MainWindow", "Edge from :"))
        self.label_4.setText(_translate("MainWindow", "Edge to:"))
        self.label_7.setText(_translate("MainWindow", "Edge Weight"))
        self.label.setText(_translate(
            "MainWindow",
            "<html><head/><body><p><span style=\" font-size:11pt;\">Select Algorithm</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "BFS"))
        self.comboBox.setItemText(1, _translate("MainWindow", "DFS"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Uniform Cost"))
        self.comboBox.setItemText(3, _translate(
            "MainWindow", "Iterative Deepening"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Greedy"))
        self.comboBox.setItemText(5, _translate("MainWindow", "A*"))
        self.label_2.setText(_translate("MainWindow", "Start Node"))
        self.label_8.setText(_translate(
            "MainWindow", "Goal(insert \',\' between goals)"))
        self.StartAlgo.setText(_translate("MainWindow", "Example"))
        self.StartAlgo.clicked.connect(lambda: self.Example())
        self.Directed.setText(_translate("MainWindow", "Directed"))
        self.Directed.clicked.connect(lambda: self.Reset())
        # reset functionality
        self.ResetGraph.setText(_translate("MainWindow", "reset"))
        self.ResetGraph.clicked.connect(lambda: self.Reset())
        # reset end
        # NEXT FUNCTION
        self.NextButton.setText(_translate("MainWindow", "Next"))
        self.NextButton.clicked.connect(lambda: self.loadGraph())
        # END NEXT FUNCTION

        self.pathShow.setText(_translate("MainWindow", "show path"))
        self.pathShow.clicked.connect(lambda: self.pathshow())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
