from .Graph import Graph

class DFT:

    def __init__(self,gObj, start):
        self.graph  = gObj
        self.start = start
        self.state = {}
        self.previousNode = {}

        #states of a node

        self.NV = 0 #Not visited
        self.NF = 1 #Not finished
        self.F = 2  #Finished

        for v in self.graph.getVertices():

            self.state[v] = self.NV
            self.previousNode[v] = None

        self.dfs_visit(self.start)


    def dfs_visit(self,node):

        self.state[node] = self.NF

        for u in self.graph.vertices:
            if u.id == node:
                for v in u.adjacent:
                    if self.state[v[0]] == self.NV:
                        self.previousNode[v[0]] = node
                        self.dfs_visit(v[0])

        self.state[node] = self.F


    def visitTo(self,node):

        path = [node]

        while(node!=self.start):
            node = self.previousNode[node]
            path.insert(0,node)

        return path