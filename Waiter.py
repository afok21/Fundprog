#--Grupo 19, Hugo Silva--107203, Miguel Dinis--109318

#--Waiter.py 

from graphics import *
import math
from Tables import *

# medidas padrão -> robot_radius=30
class Waiter: #Função para criar o robo e as suas funções
    def __init__(self, win, x, y):
        robo = Circle(Point(x , y), 30)
        robo.setFill("#DCDCDC")
        robo.setOutline("red")
        robo.draw(win)
        self.robo = robo
    
    def getCenter(self):
        return self.robo.getCenter()

    def move(self, dx, dy):
        self.robo.move(dx,dy)
    
    def getP1(self):
        return self.robo.getP1()
    
    def getP2(self):
        return self.robo.getP2()
    
    
def distance(p1, p2):
    return math.sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)

class Pratos: #Função para criar os pratos
    def __init__(self, win, x, y):
        prato1 = Circle(Point(x + 45, y), 20)
        prato2 = Circle(Point(x - 45, y), 20)
        prato3 = Circle(Point(x, y + 45), 20)
        prato4 = Circle(Point(x, y - 45), 20)
        sombra1 = Circle(Point(x + 45, y), 13)
        sombra2 = Circle(Point(x - 45, y), 13)
        sombra3 = Circle(Point(x, y + 45), 13)
        sombra4 = Circle(Point(x, y - 45), 13)
        sombra1.setFill("#DBDCCF")
        sombra2.setFill("#DBDCCF")
        sombra3.setFill("#DBDCCF")
        sombra4.setFill("#DBDCCF")
        prato1.setFill("white")
        prato2.setFill("white")
        prato3.setFill("white")
        prato4.setFill("white")
        prato1.setOutline("black")
        prato2.setOutline("black")
        prato3.setOutline("black")
        prato4.setOutline("black")
        prato1.draw(win)
        prato2.draw(win)
        prato3.draw(win)
        prato4.draw(win)
        sombra1.draw(win)
        sombra2.draw(win)
        sombra3.draw(win)
        sombra4.draw(win)

class Dock: #Função para criar as docking station
    def __init__(self, win, x, y, color, outline, side = 60):
        dock = Rectangle(Point(x , y), Point(x + side , y + side))
        dock.setFill("#DCDCDC")
        dock.setOutline("black")
        dock.draw(win)
        self.dock = dock

    def getCenter(self):
        return self.dock.getCenter()
    def getCenter(self):
        return self.dock.getCenter()



