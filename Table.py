# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 19:13:28 2025

@author: ALFIBRAGA
"""

from graphics import *

class Table:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def desenhar (self, win, cor):
        self.rectangulo = Rectangle(Point(self.x1, self.y1), Point(self.x2, self.y2))
        self.rectangulo.setFill(cor)
        self.rectangulo.draw(win)