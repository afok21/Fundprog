# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 18:44:56 2025

@author: ALFIBRAGA
"""
from graphics import *
from facenew import Face
    
def main():

    win = GraphWin("Dice Roller", 500, 500)
    win.setBackground("white")
    
    cool = Face(win, Point(250, 250), 50)
    dx, dy = 1, 1
    
    while True:
        cool.move(dx, dy)
        centro = cool.getCenter()
        if centro.getX() + 50 >= 500 or centro.getX() - 50 <= 0:
            dx = -dx
        if centro.getY() + 50 >= 500 or centro.getY() - 50 <= 0:
            dy = -dy
            
        update(30)
        
        if win.checkMouse():
            break
        
    win.getMouse()
    win.close()
        
main()
        