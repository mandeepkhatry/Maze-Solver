from Graph.Graph import Graph
from ImageManipulation.BoxMaze import ImageManipulation
from PIL import Image
from Graph.Node import Node
from ImageManipulation.Crash import Crash

#s = ImageManipulation("Maze.png")

#print(s.getTerminatingPoints().end.y)

maze = "Maze.png"

s = ImageManipulation(maze)

start_obj = s.getTerminatingPoints().start

end_obj = s.getTerminatingPoints().end


visted_nodes = []

queue = []
queue.append(start_obj)

print(start_obj.p)


