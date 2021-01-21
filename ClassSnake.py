from GameObject import *
from Point import *
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
