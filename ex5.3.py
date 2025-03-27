#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 21:10:06 2025

@author: afok21
"""

from graphics import *
import time

def main():
    janela = GraphWin("Aqui está a sua cara",500,500)
    janela.setBackground("white")
    
    face = Circle(Point(250, 250), 100)
    face.setOutline("pink")
    face.setFill("beige")
    face.setWidth(2)
    face.draw(janela)
    
    eye1 = Circle(Point(220,200), 20)
    eye1.setOutline("black")
    eye1.setFill("lightblue")
    eye1.setWidth(1)
    eye1.draw(janela)
    
    eye2 = Circle(Point(280, 200), 20)
    eye2.setOutline("black")
    eye2.setFill("lightgreen")
    eye2.setWidth(1)
    eye2.draw(janela)
    
    mouth = Line(Point(220,300), Point(280, 300))
    mouth.setOutline("red")
    mouth.setWidth(1)
    mouth.draw(janela)
    
    nose = Polygon(Point(250, 250), Point(250,280), Point(270,280))
    nose.setOutline("black")
    nose.setFill("brown")
    nose.setWidth(1)
    nose.draw(janela)
    
    dx, dy = 10, 10
        
    while True:
        face.move(dx, dy)
        eye1.move(dx, dy)
        eye2.move(dx, dy)
        mouth.move(dx, dy)
        nose.move(dx, dy)
         
        centro = face.getCenter()
        if centro.getX() + 100 >= 500 or centro.getX() - 100 <= 0:
            dx = -dx
        if centro.getY() + 100 >= 500 or centro.getY() - 100 <= 0:
            dy = -dy
            
        update(60)

        
        if janela.checkMouse():
            break
    
   
    janela.getMouse()
    janela.close()
    
main()