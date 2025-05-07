# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 19:13:57 2025

@author: ALFIBRAGA
"""
from Table import Table 
from graphics import *
from Waiter import Waiter
import time

def main():
    win = GraphWin("Planta da Sala", 650, 650)
    win.setCoords(0, 0, 150, 150)

    # Mesas
    mesa1 = Table(22, 40, 40, 54)
    mesa2 = Table(22, 68, 40, 82)
    mesa3 = Table(22, 96, 40, 110)
    mesa4 = Table(44, 40, 62, 54)
    mesa5 = Table(44, 68, 62, 82)
    mesa6 = Table(44, 96, 62, 110)
    mesa7 = Table(88, 40, 106, 54)
    mesa8 = Table(88, 68, 106, 82)
    mesa9 = Table(88, 96, 106, 110)
    mesa10 = Table(110, 40, 128, 54)
    mesa11 = Table(110, 68, 128, 82)
    mesa12 = Table(110, 96, 128, 110)
    mesalonga1 = Table(40.5, 20, 43.5, 130)
    mesalonga2 = Table(106.5, 20, 109.5, 130)
    docking1 = Table(62, 140, 75, 150)
    recolhapratos = Table(75, 140, 88, 150)
    entregapratos = Table(62, 0, 88, 10)

    mesas = [mesa1, mesa2, mesa3, mesa4, mesa5, mesa6,
             mesa7, mesa8, mesa9, mesa10, mesa11, mesa12,
             mesalonga1, mesalonga2, docking1, recolhapratos, entregapratos]

    for mesa in mesas:
        mesa.desenhar(win, "brown" if mesa in [mesa1, mesa2, mesa3, mesa4, mesa5, mesa6, mesa7, mesa8, mesa9, mesa10, mesa11, mesa12] else
                      "black" if mesa in [mesalonga1, mesalonga2] else
                      "grey" if mesa == docking1 else
                      "yellow" if mesa == recolhapratos else
                      "green")

        # Cria o Waiter na docking station superior
    waiter = Waiter(win, 68, 145)

    mesas_cliente = [mesa1, mesa2, mesa3, mesa4, mesa5, mesa6,
                     mesa7, mesa8, mesa9, mesa10, mesa11, mesa12]

    ponto_meio_esquerdo = Point(35, 75)
    ponto_meio_direito = Point(93, 75)
    ponto_docking_baixo = entregapratos.getCenter()
    ponto_docking_cima = docking1.getCenter()

    for mesa in mesas_cliente:
        destino = mesa.getCenter()

        # Evita obstáculos dependendo da posição da mesa
        if destino.getX() < 75:
            waiter.move_to(ponto_meio_esquerdo)  # Desvia pela esquerda
        else:
            waiter.move_to(ponto_meio_direito)  # Desvia pela direita

        waiter.move_to(destino)
        time.sleep(0.5)

        # Vai para a docking inferior (entrega de pratos)
        waiter.move_to(ponto_docking_baixo)
        time.sleep(0.5)

        # Volta para docking superior
        waiter.move_to(ponto_docking_cima)
        time.sleep(0.5)


main()
