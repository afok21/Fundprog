# -*- coding: utf-8 -*-
"""
Created on Wed May  7 14:10:46 2025

@author: ALFIBRAGA
"""

from graphics import *
from math import *

class Esfera:
    def __init__(self, radius):
        self.radius = radius
        
    def surfaceArea(self):
        self.area = pi*self.radius**2
        print("A área é", self.area)
    
    def volume(self):
        self.volume = 4/3 * pi * self.radius**3
        print("O volume é", self.volume)
        