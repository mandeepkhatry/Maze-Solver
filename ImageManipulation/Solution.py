from PIL import Image

def getSolution(imageObj):
    imageObj.save("MazeSolved.png")
    solved = Image.open("MazeSolved.png")
    solved.show()