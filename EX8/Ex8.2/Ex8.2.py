#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 13 19:30:30 2025

@author: afok21
"""

from graphics import *
from grupo_grafico import*

def main():

    with open("dados_viagem.txt", 'r') as dados: #abrir o txt onde tao os dados
        linhas = dados.readlines()

    hodometro_inicial = float(linhas[0]) #no caso do txt usado é 0
    total_km = 0
    total_combustivel = 0

    print("Consumo de cada trajeto:")

    for linha in linhas[1:]: #começar no valor 1, o 0 é o 0 no caso
        parte = linha.split()  # separa a string em partes
        hodometro_final = float(parte[0])  # primeira parte é velocidade
        combustivel = float(parte[1])     # segunda parte é combustivel
        distancia = hodometro_final - hodometro_inicial
        consumo = (combustivel / distancia) * 100

        print(f"- {distancia:.2f} km, {combustivel:.2f} L -- {consumo:.2f} L/100km")
        
        #calculo para o consumo medio
        total_km = total_km + distancia
        total_combustivel =total_combustivel + combustivel
        hodometro_inicial = hodometro_final

    consumo_medio_total = (total_combustivel / total_km) * 100
    print(f"\nConsumo médio total: {consumo_medio_total:.2f} L/100km")


main()