# Each vertex in theoritical array of vertices
class Vertex:
    def __init__(self,v):
        self.id = v
        self.adjacent = []

    def addAdjacent(self,vertex,weight=0):
        self.adjacent.append([vertex,weight])

class Graph:
    def __init__(self):
        #List of vertex objects
        #In form of []->[[],[],[]]
        self.vertices = []

        #Visited vertices( from_v nodes)  to check for repeated starting vertex
        self.visitedVertices = []

    def addEdge(self,from_v,to_v,weight=0):

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

    def result(self):
        for from_v in self.vertices:
            for i in range(len(from_v.adjacent)):
                print("Weight of edge from " + from_v.id + " to "+ from_v.adjacent[i][0] + " is " + str(from_v.adjacent[i][1]))




