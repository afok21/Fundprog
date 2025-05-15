#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 13 19:27:59 2025

@author: afok21
"""

from graphics import *

class GrupoGrafico:
    def __init__(self, ancora):
        self.ancora = ancora
        self.objetos = []

    def retornaAncora(self):
        # Retorna um clone do ponto âncora
        return Point(self.ancora.getX(), self.ancora.getY())

    def AdicionaObjeto(self, objeto):
        self.objetos.append(objeto)

    def move(self, dx, dy):
        # Move a âncora e todos os objetos no grupo
        self.ancora.move(dx, dy)
        for obj in self.objetos:
            obj.move(dx, dy)

    def desenha(self, win):
        for obj in self.objetos:
            obj.draw(win)

    def apaga(self):
        for obj in self.objetos:
            obj.undraw()


