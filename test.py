class Graph:
    
    def __init__(self):
        self._nodedict = {}
        self._nodelist = []
        self._edgedict = {}
        self._edgelist = []
    
    @property
    def node(self):
        return self._nodedict
    
    @property
    def edge(self):
        return self._edgedict
    
    def nodes(self):
        return self._nodelist
    
    def edges(self):
        return self._edgelist
    
    def add_node(self, node, attr_dict=None):
        if(attr_dict==None):
            self._nodedict[node] = {}
        else:
            self._nodedict[node] = attr_dict
        if(node not in self._nodelist):        
            self._nodelist.append(node)
    
    def add_edge(self, node1, node2, attr_dict=None):
        if(node1 in self._edgedict):
            if(attr_dict==None):
                temp = self._edgedict[node1]
                temp[node2] = {}
                temp2 = {node1 : {}}
                self._edgedict[node1] = temp
                self._edgedict[node2] = temp2
            else:
                temp = self._edgedict[node1]
                temp[node2] = attr_dict
                temp2 = {node1 : attr_dict}
                self._edgedict[node1] = temp
                self._edgedict[node2] = temp2
        else:
            if(attr_dict==None):
                temp = {node2 : {}}
                temp2 = {node1 : {}}
                self._edgedict[node1] = temp
                self._edgedict[node2] = temp2
            else:
                temp = {node2 : attr_dict}
                temp2 = {node1 : attr_dict}
                self._edgedict[node1] = temp
                self._edgedict[node2] = temp2
        self._edgelist.append((node1,node2))
    
    def add_nodes_from(self, node_list, attr_dict=None):
        for i in node_list:
            self.add_node(i,attr_dict)

    def add_edges_from(self, edge_list, attr_dict=None):
        for n in edge_list:
            self.add_node(n[0])
            self.add_node(n[1])
            self.add_edge(n[0],n[1],attr_dict)
                
    def degree(self,n):
        grade = 0
        for edges in self.edges():
            for node in edges:
                if(node == n):
                    grade += 1
        print(grade)
        return grade
    
    def __getitem__(self, node):
        pass
    
    def __len__(self):
        pass
    
    def neighbors(self, node):
        pass
    
    def remove_node(self, node1):
        pass
    
    def remove_edge(self, node1, node2):
        pass
    
    def remove_nodes_from(self, node_list):
        pass
    
    def remove_edges_from(self, edge_list):
        pass

import sys
import traceback

try:
    G = Graph()
    G.add_edges_from(((1,2), (2,3), (2,4)))
    assert G.degree(2) == 3
    assert G.degree(1) == 1
    print(G[2])
    print(G.node)
    assert G[2] == {1: {}, 3: {}, 4: {}}
    assert len(G) == 4
    assert G.neighbors(1) == [2]
    assert G.neighbors(2) == [1,3,4]
    G.remove_node(1)
    assert G.node == {2: {}, 3: {}, 4: {}}
    assert G.edge == {2: {3: {}, 4: {}}, 3: {2: {}}, 4: {2: {}}}
    G.remove_edge(2,3)
    assert G.edge == {2: {4: {}}, 3: {}, 4: {2: {}}}
    assert G.node == {2: {}, 3: {}, 4: {}}
    assert G.neighbors(2) == [4]
    G.remove_edges_from(((2,4), (4,3)))
    assert G.edge == {2: {}, 3: {}, 4: {}}
    assert G.node == {2: {}, 3: {}, 4: {}}
    G.remove_nodes_from((2,3))
    assert G.edge == {4: {}}
    assert G.node == {4: {}}
    assert G.neighbors(4) == []
    assert len(G) == 1
    assert G.degree(4) == 0
    
    print("All test passed!")
except AssertionError:
    _, _, tb = sys.exc_info()
    traceback.print_tb(tb) # Fixed format