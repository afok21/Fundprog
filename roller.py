#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 15:34:21 2025

@author: afok21
"""

from random import randrange
from graphics import GraphWin, Point

from botaocirc import BotaoCircular
from dieview import DieView

def main():

    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")


    die1 = DieView(win, Point(3, 7), 2)
    die2 = DieView(win, Point(7, 7), 2)
    rollButton = BotaoCircular(win, Point(5, 4.5), 1.5, "Roll Dice")
    rollButton.activate()
    quitButton = BotaoCircular(win, Point(5, 1), 1.5, "Quit")


    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1, 7)
            die1.setValue(value1)
            value2 = randrange(1, 7)
            die2.setValue(value2)
            quitButton.activate()  
        pt = win.getMouse()


    win.close()

main()
