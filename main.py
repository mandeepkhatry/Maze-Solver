from Graph.Graph import Graph
from ImageManipulation.BoxMaze import ImageManipulation
from PIL import Image
from Graph.Node import Node
from ImageManipulation.Crash import Crash
from ImageManipulation.BoxMaze import Pixel
from ImageManipulation.Solution import getSolution

#s = ImageManipulation("Maze.png")

#print(s.getTerminatingPoints().end.y)

maze = "Maze.png"

s = ImageManipulation(maze)

pix = s.getPixelObj()

# End points of rectangular maze

end1 = s.getImageBound()[0]
end2 = s.getImageBound()[1]


start = Pixel(s.getTerminatingPoints().start.x,s.getTerminatingPoints().start.y,s.getTerminatingPoints().start.p)


end = Pixel(s.getTerminatingPoints().end.x,s.getTerminatingPoints().end.y,s.getTerminatingPoints().end.p)

visted_nodes = []

queue = []

queue.append(start)

for i in range(1000):
    visted_nodes.append([False]*1000)

final_destination =False


def withinBound(x,y):
    if(x >= end1.x and x <= end2.x):
        if(y >= end1.y and y <= end2.y):
            return True
    else:
        return False


while len(queue)>0:

    node_pix = queue.pop(0)

    if(node_pix.x == end.x and node_pix.y == end.y):
        final_destination = node_pix
        break
    # For upper node pixel
    if(withinBound(node_pix.x, node_pix.y-1) and pix[node_pix.x,node_pix.y-1] != (0,0,0,255) and visted_nodes[node_pix.x][node_pix.y-1]==False):
        queue.append(Pixel(node_pix.x,node_pix.y-1,node_pix))
        visted_nodes[node_pix.x][node_pix.y-1] = True

    # For lower node pixel
    if(withinBound(node_pix.x, node_pix.y+1) and pix[node_pix.x,node_pix.y+1] != (0,0,0,255) and visted_nodes[node_pix.x][node_pix.y+1]==False):
        queue.append(Pixel(node_pix.x,node_pix.y+1,node_pix))
        visted_nodes[node_pix.x][node_pix.y+1] = True

    # For left node pixel
    if(withinBound(node_pix.x-1, node_pix.y) and pix[node_pix.x-1,node_pix.y] != (0,0,0,255) and visted_nodes[node_pix.x-1][node_pix.y]==False):
        queue.append(Pixel(node_pix.x-1,node_pix.y,node_pix))
        visted_nodes[node_pix.x-1][node_pix.y] = True

    # For right node pixel
    if(withinBound(node_pix.x+1, node_pix.y) and pix[node_pix.x+1,node_pix.y] != (0,0,0,255) and visted_nodes[node_pix.x+1][node_pix.y]==False):
        queue.append(Pixel(node_pix.x+1,node_pix.y,node_pix))
        visted_nodes[node_pix.x+1][node_pix.y] = True


while final_destination:

    pix[final_destination.x, final_destination.y] = (150, 0, 50, 100)
    final_destination = final_destination.p

getSolution(s.getImg())