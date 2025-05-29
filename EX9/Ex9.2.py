#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 29 18:11:15 2025

@author: afok21
"""

from graphics import *
from tkinter.filedialog import askopenfilename
import tkinter as tk

def fileWindow(infile, wWidth, wHeight):
    win = GraphWin("Imagem convertida", wWidth, wHeight)
    infile.draw(win)

    height = 1
    while height < wHeight:
        for i in range(wWidth - 1):
            r, g, b = infile.getPixel(i + 1, height)
            brightness = int(round(0.299 * r + 0.587 * g + 0.114 * b))
            infile.setPixel(i + 1, height, color_rgb(brightness, brightness, brightness))
        win.update()
        height += 1

    return win

def main():
    # Abre janela para selecionar o ficheiro
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal do tkinter
    fname = askopenfilename(title="Selecione uma imagem .gif", filetypes=[("GIF files", "*.gif")])

    if not fname:
        print("Nenhum ficheiro selecionado.")
        return

    tempImage = Image(Point(0, 0), fname)
    wWidth = tempImage.getWidth()
    wHeight = tempImage.getHeight()

    infile = Image(Point(wWidth / 2, wHeight / 2), fname)
    win = fileWindow(infile, wWidth, wHeight)

    outfileName = "imagem_convertida.gif"
    infile.save(outfileName)

    msg = Text(Point(wWidth / 2, 10), f"Imagem salva como {outfileName}")
    msg.setFill("green")
    msg.draw(win)

    win.getMouse()
    win.close()

main()