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

        #Visited vertices( from_v nodes)  to check for repeated starting vertex
        self.visitedVertices = []

    def addEdge(self,from_v,to_v,weight):

        #Check if starting node is visted
        if from_v in self.visitedVertices:

            #check for object containg starting node(from_v)
            for v in self.vertices:
                if v.id == from_v:
                    v.addAdjacent(to_v, weight)

        else:
            self.visitedVertices.append(from_v)
            newVertex = Vertex(from_v)
            newVertex.addAdjacent(to_v,weight)
            self.vertices.append(newVertex)

    def display(self):
        print(len(self.vertices))


#g = Graph()

#g.addEdge('A','B',1)
#g.addEdge('A','C',2)
#g.addEdge('B','A',3)

#g.display()

