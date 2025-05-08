# -*- coding: utf-8 -*-
"""
Created on Thu May  8 17:41:00 2025

@author: ALFIBRAGA
"""

from graphics import *
from math import *

class Cubo:
    def __init__(self, aresta):
        self.aresta = aresta
        
    def faceArea(self):
        self.area = self.aresta**2
        print("A área é", self.area)
    
    def surfaceArea(self):
        self.areatotal = 6*self.aresta**2
        print("A area total é", self.areatotal)
        
    def drawIsometrico(self):
      win = GraphWin("Cubo Isométrico", 400, 400)
      win.setBackground("white")

      offset = self.aresta
      p = Point(100, 100)

      front = [
          p,
          Point(p.getX() + self.aresta, p.getY()),
          Point(p.getX() + self.aresta, p.getY() + self.aresta),
          Point(p.getX(), p.getY() + self.aresta)
      ]

      back = [
          Point(pt.getX() + offset, pt.getY() - offset)
          for pt in front
      ]

      for i in range(4):
          Line(front[i], front[(i+1)%4]).draw(win)
          Line(back[i], back[(i+1)%4]).draw(win)
          Line(front[i], back[i]).draw(win)

      return win
    
      win.getMouse()
      win.close()