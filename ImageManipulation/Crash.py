from PIL import Image

class Crash:
    def __init__(self,passImage):
        img = Image.open(passImage)
        self.weight, self.height = img.size
        self.pixObj = img.load()

    def getPixObj(self):
        return  self.pixObj

    def checkCrash(self):
        if(self.pixObj[x,y]==(0, 0, 0, 255)):
            return True
        else:
            return  False


