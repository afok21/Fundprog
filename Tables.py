#--Grupo 19, Hugo Silva--107203, Miguel Dinis--109318

#--Tables.py 


from graphics import *
from button import *


class TableR: #Função para criar as mesas quadradas
    def __init__(self, win, x, y, color):
        self.x = x
        self.y = y
        self.width = 140 
        self.height = 140 
        self.rect = Rectangle(Point(x, y), Point(x + self.width, y + self.height))
        self.rect.setFill(color)
        self.rect.draw(win)

    def getCenter(self):
        return Point(self.x + self.width / 2 , self.y + self.height / 2)
    
    def getP1(self):
        return self.rect.getP1()

    def contains(self,  click):
        
        return (self.x <= click.getX() <= self.x + self.width and
                self.y <= click.getY() <= self.y + self.height)

class TableC: #Função para criar as mesas redondas
    def __init__(self, win, x, y, color, radius):
        self.center = Point(x, y)
        self.radius = radius
        self.circle = Circle(self.center, radius)
        self.circle.setFill(color)
        self.circle.draw(win)

    def getCenter(self):
        return self.center



    def getP1(self):
        return self.circle.getP1()
    
    def contains(self, click):
        distance = ((click.getX() - self.center.getX()) ** 2 + (click.getY() - self.center.getY()) ** 2) ** 0.5
        return distance <= self.radius

    
 