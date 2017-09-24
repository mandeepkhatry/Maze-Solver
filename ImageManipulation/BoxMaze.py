from PIL import Image

class Pixel:
    def __init__(self,x,y,p):
        self. x = x
        self. y = y
        self. p = p

# class of Start and End point for returning in getTerminatingPoints Function
class StartEnd:
    def __init__(self,s,e):
        self.start = s
        self.end = e

class ImageManipulation:


    def __init__(self,passImage):
        img = Image.open(passImage)
        self.weight, self.height = img.size
        self.pixObj = img.load()

    #find maze from image

    def getTerminatingPoints(self):

        #find bounds
        temp1 = Pixel(0, 0, None)
        temp2 = Pixel(0, 0, None)

        for j in range(self.height):
            for i in range(self.weight):
                if self.pixObj[i,j] == (0 ,0 ,0 ,255):
                    if(temp1.x == 0 and temp1.y == 0 and temp1.p == None):
                        temp1.x, temp1.y, temp1.p = i, j, None
                    temp2.x, temp2.y, temp2.p = i,j,None

        #find terminating start end points

        start = Pixel(0, 0, None)
        end = Pixel(0, 0, None)
        for i in range(temp1.x, temp2.x + 1):
            if self.pixObj[i, temp1.y] == (255, 255, 255, 0):
                s = Pixel(i, temp1.y, None)
            if self.pixObj[i, temp2.y] == (255, 255, 255, 0):
                e = Pixel(i, temp2.y, None)

        terminatingPoints = StartEnd(s,e)

        return terminatingPoints


#s = ImageManipulation("Maze.png")

#print(s.getTerminatingPoints().end.y)


