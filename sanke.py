class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def print(self):
        print("(",self.x ,",", self.y,")")
class GameObject:

    def __init__(self,symbol,point):
        self.symbol = symbol
        self.coordinates = point

class Snake:
    def __init__(self,headSymbol,point):
        self.headSymbol = headSymbol
        self.tailSymbol = "-"
        self.coordinates = point
        self.tailList = [
            GameObject(self.tailSymbol,Point(self.coordinates.x-1,self.coordinates.y)),
            GameObject(self.tailSymbol,Point(self.coordinates.x-2,self.coordinates.y)),
            GameObject(self.tailSymbol,Point(self.coordinates.x-3,self.coordinates.y)),
            GameObject(self.tailSymbol,Point(self.coordinates.x-4,self.coordinates.y)),
            GameObject(self.tailSymbol,Point(self.coordinates.x-5,self.coordinates.y))
        ]
    def toGameObjectList(self):
        objectsList=[]
        objectsList.append(GameObject(self.headSymbol,self.coordinates))
        for item in self.tailList:
            objectsList.append(item)
        return objectsList


def gridToString(width, height, gameObjectList, defaultSymbol=" "):
    for gameObject in gameObjectList:
        if gameObject.coordinates.x >= width:
            print("X points is bigger than width")
            return
        elif gameObject.coordinates.y >= height:
            print("y points is bigger than height")
            return
    grid=[""] *height
    for i in range(height):
      grid[i]=[str(defaultSymbol)] * width
    for gameObject in gameObjectList:
        grid[gameObject.coordinates.y][gameObject.coordinates.x] = gameObject.symbol
    for i in range(height):
        print(''.join(grid[i]))

width=50
height=20

border=[]

#Borders loop
for x_axis in range(width):
        border.append(GameObject("+",Point(x_axis, 0)))
for y_axis in range(height - 1):
        border.append(GameObject("+",Point(0, y_axis+1)))
for x_axis in range(width):
        border.append(GameObject("+",Point(x_axis, height-1)))
for y_axis in range(height):
       border.append(GameObject("+",Point(width-1, y_axis)))
grid=[]
x = 30
headSymbol = '>'
tailSymbol = '='
shamshom = Snake(headSymbol,Point(x+5,8))
for item in shamshom.toGameObjectList():
    grid.append(item)
for item in border:
    grid.append(item)
gridToString(width, height, grid, )




