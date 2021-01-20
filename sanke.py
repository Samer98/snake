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
grid=[]
for i in range(height):
    for j in range(1, width):
        grid.append(Point(i, j))

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
# for num in range(len(border)):
#   border[num].print()
x = 30
border.append(GameObject("h",Point(x,9)))
border.append(GameObject("i",Point(x+1,9)))
border.append(GameObject("s",Point(x+2,9)))
border.append(GameObject("h",Point(x+3,9)))
border.append(GameObject("a",Point(x+4,9)))
border.append(GameObject("m",Point(x+5,9)))
gridToString(width, height, border, )




