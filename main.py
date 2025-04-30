# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 19:13:57 2025

@author: ALFIBRAGA
"""

from Table import Table
from graphics import *

def main():
    
    win = GraphWin("Planta da Sala", 650, 650)
    win.setCoords(0, 0, 150, 150)
    
    mesa1= Table(22, 40, 40, 54)
    mesa1.desenhar(win, "brown")
    
    mesa2= Table(22, 68, 40, 82)
    mesa2.desenhar(win, "brown")
    
    mesa3 = Table(22, 96, 40, 110)
    mesa3.desenhar(win, "brown")
    
    mesa4 = Table(44, 40, 62, 54)
    mesa4.desenhar(win, "brown")
    
    mesa5 = Table(44, 68, 62, 82)
    mesa5.desenhar(win, "brown")
    
    mesa6 = Table(44, 96, 62, 110)
    mesa6.desenhar(win, "brown")
    
    mesa7 = Table(88, 40, 106, 54)
    mesa7.desenhar(win, "brown")
    
    mesa8 = Table(88, 68, 106, 82)
    mesa8.desenhar(win, "brown")
    
    mesa9 = Table(88, 96, 106, 110)
    mesa9.desenhar(win, "brown")
    
    mesa10 = Table(110, 40, 128, 54)
    mesa10.desenhar(win, "brown")
    
    mesa11 = Table(110, 68, 128, 82)
    mesa11.desenhar(win, "brown")
    
    mesa12 = Table(110, 96, 128, 110)
    mesa12.desenhar(win, "brown")
    
    mesalonga1 = Table(40.5, 20, 43.5, 130)
    mesalonga1.desenhar(win, "black")
    
    mesalonga2 = Table(106.5, 20, 109.5, 130)
    mesalonga2.desenhar(win, "black")
    
    win.getMouse()
    win.close()
    
main()



