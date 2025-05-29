# -*- coding: utf-8 -*-
"""
Created on Thu May  8 17:29:52 2025

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
        
    def drawDimetrico(self):
        win = GraphWin("Cubo Dimétrico", 400, 400)
        win.setBackground("white")

        offset_x = self.aresta * 0.5
        offset_y = self.aresta * 0.75
        size = self.aresta * 0.5

        p = Point(150, 150)

        front = [
            p,
            Point(p.getX() + size, p.getY()),
            Point(p.getX() + size, p.getY() + size),
            Point(p.getX(), p.getY() + size)
     ]
        back = [
            Point(pt.getX() + offset_x, pt.getY() - offset_y)
            for pt in front
        ]

        for i in range(4):
            Line(front[i], front[(i+1)%4]).draw(win)            
            Line(back[i], back[(i+1)%4]).draw(win)
            Line(front[i], back[i]).draw(win)

        return win
    
        win.getMouse()
        win.close()
