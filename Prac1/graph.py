class Graph:
    
    def __init__(self, n = None, e = None):
        self._nodedict = {} if not n else n
        self._nodelist = []
        self._edgedict = {} if not n else e
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
        if node1 not in self.node.keys():
            self.add_node(node1)
        if node2 not in self.node.keys():
            self.add_node(node2)
        if attr_dict:
            self.edge.setdefault(node1,{})[node2] = attr_dict
            self.edge.setdefault(node2,{})[node1] = attr_dict
        else:
            self.edge.setdefault(node1,{})[node2] = {}
            self.edge.setdefault(node2,{})[node1] = {}
        if (node1,node2) not in self._edgelist or (node1,node2) not in self._edgelist:
           self._edgelist.append((node1,node2))
           self._edgelist.append((node2,node1))
           
        
        """if((node1,node2) in self._edgelist or (node2,node1) in self._edgelist):
            print("L' aresta (node1,node2) ja existeix!")
        else:
            if node1 not in self._nodelist:
                self.add_node(node1)
            if node2 not in self._nodelist:
                self.add_node(node2)
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
            self._edgelist.append((node1,node2))"""
    
    def add_nodes_from(self, node_list, attr_dict=None):
        for i in node_list:
            self.add_node(i,attr_dict)

    def add_edges_from(self, edge_list, attr_dict=None):
        for n in edge_list:
            self.add_edge(n[0],n[1],attr_dict)
                
    def degree(self,n):
        return len(self.edge[n])
    
    def __getitem__(self, node):
        res = {}
        for k in self._nodedict:
            if(k!=node):
                res[k] = self.node[k]
        return res
    
    def __len__(self):
        return len(self.nodes())
    
    def neighbors(self, node):
        res = []
        for n in self._edgedict[node]:
            res.append(n)
        return res
    
    def remove_node(self, node1):
        if(node1 in self._nodelist):
            for v in self._edgedict:
                if(v in self.neighbors(node1)):
                    self._edgedict.get(v).pop(node1)
                    try:
                        self._edgelist.remove((node1,v))
                    except:
                        self._edgelist.remove((v,node1))
                        
            self._edgedict.pop(node1)
            self._nodedict.pop(node1)
            self._nodelist.remove(node1)
            print("Node",node1,"successfully removed.")
        else:
            print("Node",node1,"doesn't exist in this Graph.")
    
    def remove_edge(self, node1, node2):
        if((node1,node2) in self._edgelist):
            self._edgedict[node1].pop(node2)
            self._edgedict[node2].pop(node1)
            self._edgelist.remove((node1,node2))
    
    def remove_nodes_from(self, node_list):
        for node in node_list:
            self.remove_node(node)
    
    def remove_edges_from(self, edge_list):
        for pair in edge_list:
            self.remove_edge(pair[0],pair[1])