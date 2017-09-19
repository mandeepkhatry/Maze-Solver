class Vertex:
    def __init__(self,v):
        self.id = v
        self.adjacent = []

    def addAdjacent(self,vertex,weight):
        self.adjacent.append([vertex,weight])



class Graph:
    def __init__(self):
        #List of vertex objects
        #In form of []->[[],[],[]]
        self.vertices = []

    #Add Edges in form of (V1,[V2,V3... connected vertices],[w2,w3....weight of edges])
    def addEdge(self,from_v,to_v,weight):
        for i in range(len(to_v)):
            newV = Vertex(from_v)
            newV.addAdjacent(to_v[i], weight[i])
        self.vertices.append(newV)


    def display(self):
        print(len(self.vertices))

#g =Graph()
#g.addEdge('A',['B','C'],[3,2])
#g.addEdge('B',['A','C'],[3,2])
#g.addEdge('C',['A','B'],[3,2])
#g.display()




