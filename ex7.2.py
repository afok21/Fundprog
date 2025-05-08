# -*- coding: utf-8 -*-
"""
Created on Wed May  7 14:53:36 2025

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

def main():
    cubo1 = Cubo(10)
    cubo1.faceArea()
    cubo1.surfaceArea()
    
main()
