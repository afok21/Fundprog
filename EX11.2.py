#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 18:13:14 2025

@author: afok21
"""

def ano_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def data_valida(dia, mes, ano):
    if mes < 1 or mes > 12:
        return False

    # Dias máximos por mês
    dias_por_mes = [31, 29 if ano_bissexto(ano) else 28, 31, 30, 31, 30,
                    31, 31, 30, 31, 30, 31]

    if dia < 1 or dia > dias_por_mes[mes - 1]:
        return False

    return True

def main():
    data = input("Digite uma data no formato dia/mês/ano: ")
    partes = data.split('/')
    if len(partes) != 3:
        print("Formato inválido. Use dia/mês/ano.")
        return

    dia = int(partes[0])
    mes = int(partes[1])
    ano = int(partes[2])
    if data_valida(dia, mes, ano):
        print(f"A data {data} é válida.")
    else:
        print(f"A data {data} NÃO é válida.")
main()