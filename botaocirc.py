#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 12:23:54 2025

@author: afok21
"""

from graphics import *

class BotaoCircular:
    def __init__(self, win, centro, raio, legenda):
        self.centro = centro
        self.raio = raio
        self.win = win
        
        self.circulo = Circle(centro, raio)
        self.circulo.setFill("lightgray")
        self.circulo.draw(win)
        
        self.xmin = centro.getX() - raio
        self.xmax = centro.getX() + raio
        self.ymin = centro.getY() - raio
        self.ymax = centro.getY() + raio


        self.legenda = Text(centro, legenda)
        self.legenda.draw(win)
        
        self.active = False
        
    def activate(self):
        "Sets this button to 'active'."
        self.legenda.setFill('black')
        self.circulo.setWidth(2)
        self.active = True
    
    def deactivate(self):
        self.legenda.setFill('darkgrey')
        self.circulo.setWidth(1)
        self.active = False
        
    def getLabel(self):    
        return self.legenda.getText()
    
    def clicked(self, p):
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def dentro(self, ponto):
        return (ponto.getX() - self.centro.getX())**2 + (ponto.getY() - self.centro.getY())**2 <= self.raio**2

    def setCor(self, cor):
        self.circulo.setFill(cor)
    
    def update(self, win, legenda):
        self.legenda.undraw()
        center = self.center
        self.legenda = Text(center, legenda)
        self.active = False
        self.legenda.draw(win)
        
        
    