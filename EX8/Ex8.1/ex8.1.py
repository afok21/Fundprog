#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 13 19:56:47 2025

@author: afok21
"""

from graphics import *
from grupo_grafico import GrupoGrafico  

def main():
    win = GraphWin("Mover Cara", 400, 400)

    # Criar ponto âncora no meio da janela
    ancora = Point(200, 200)
    grupo = GrupoGrafico(ancora)

    # Criar os objetos gráficos (cara)
    face = Circle(ancora, 50)
    face.setFill("yellow")

    olho_esq = Circle(Point(180, 180), 5)
    olho_esq.setFill("black")

    olho_dir = Circle(Point(220, 180), 5)
    olho_dir.setFill("black")

    boca = Line(Point(180, 220), Point(220, 220))

    # Adicionar objetos ao grupo
    grupo.AdicionaObjeto(face)
    grupo.AdicionaObjeto(olho_esq)
    grupo.AdicionaObjeto(olho_dir)
    grupo.AdicionaObjeto(boca)

    # Desenhar os objetos na janela
    grupo.desenha(win)

    # Mover a figura inteira para onde o usuário clicar
    while True:
        click = win.getMouse()
        dx = click.getX() - grupo.retornaAncora().getX()
        dy = click.getY() - grupo.retornaAncora().getY()

        grupo.move(dx, dy)

    # win.close()  # opcional, se quiser permitir fechar a janela (poderia colocar um botão)

if __name__ == "__main__":
    main()