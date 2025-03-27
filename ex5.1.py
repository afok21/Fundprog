#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 15:24:39 2025

@author: afok21
"""

from graphics import *

def main():
    
    win= GraphWin("Animação", 500, 500)
    win.setBackground(color_rgb(100, 100, 150))
    
    circ = Circle(Point(250,250), 50)
    circ.setFill("brown")
    circ.setOutline("black")
    circ.setWidth(2)
    circ.draw(win)
    
    dx, dy = 5, 2
    
    while True:
        circ.move(dx, dy)
        centro = circ.getCenter()
        if centro.getX() + 50 >= 500 or centro.getX() - 50 <= 0:
            dx = -dx
        if centro.getY() + 50 >= 500 or centro.getY() - 50 <= 0:
            dy = -dy
            
        update(60)

        
        if win.checkMouse():
            break
        
    win.getMouse()
    win.close()
        
main()
