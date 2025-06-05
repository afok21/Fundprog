#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 18:12:46 2025

@author: afok21
"""

def QuadradoElementos(numeros):
    for i in range(len(numeros)):
        numeros[i] = numeros[i] ** 2

def SomatorioLista(numeros):
    return sum(numeros)

def ConverteEmNumeros(ListaCaracteres):
    for i in range(len(ListaCaracteres)):
        ListaCaracteres[i] = float(ListaCaracteres[i].strip())

nome_ficheiro = input("Digite o nome do ficheiro: ")

with open(nome_ficheiro, "r") as ficheiro:
            linhas = ficheiro.readlines()
            
ConverteEmNumeros(linhas)
QuadradoElementos(linhas)
soma = SomatorioLista(linhas)
        
print(soma)
