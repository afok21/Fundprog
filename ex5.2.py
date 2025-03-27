#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 19:36:52 2025

@author: afok21
"""


def main():
    
    
    palavras = input("Escreva uma frase e direi quantas palavras que a mesma tem: ").strip()
    
    if not palavras:
        print("0 palavras")
        return
    
    espaços = " "
    quantidade =palavras.count(espaços) + 1
    print(f"existem {quantidade} palavras")
    
    # Dúvida, o que fazer para impedir que a pessoa coloque dois espaços entre as palavras?
    
main()
    
