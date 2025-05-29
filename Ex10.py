#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 29 14:02:41 2025

@author: afok21
"""

from graphics import *
import random

def main():
    win = GraphWin("Three Button Monte", 600, 500)
    win.setBackground("lightgray")
    
    title = Text(Point(300, 30), "Three Button Monte")
    title.setSize(20)
    title.setStyle("bold")
    title.draw(win)
    
    # Desenha as portas
    doors = []
    for i, x in enumerate([150, 300, 450]):
        rect = Rectangle(Point(x-50, 150), Point(x+50, 250))
        rect.setFill("lightblue")
        rect.draw(win)
        label = Text(Point(x, 200), f"Porta {i+1}")
        label.draw(win)
        doors.append({
            "rect": rect,
            "label": label,
            "center": Point(x, 200)
        })
    
    # Botão para sair
    quit_btn = Rectangle(Point(250, 400), Point(350, 450))
    quit_btn.setFill("red")
    quit_btn.draw(win)
    quit_text = Text(Point(300, 425), "Quit")
    quit_text.draw(win)
    
    # display de comentários
    message = Text(Point(300, 100), "Escolhe uma porta")
    message.setSize(14)
    message.draw(win)
    
    # marcador
    wins = 0
    losses = 0
    score = Text(Point(300, 330), f"Vitórias: {wins}  Derrotas: {losses}")
    score.setSize(14)
    score.draw(win)

    playing = True
    while playing:
        # Seleciona porta correta aleatoriamente
        winner = random.randint(0, 2)
        win_door = doors[winner]
        
        choice = None
        while choice is None:
            click = win.getMouse()
            
            # Verifica se clicou numas das portas
            for i, door in enumerate(doors):
                if (click.x >= door["rect"].getP1().x and 
                    click.x <= door["rect"].getP2().x and
                    click.y >= door["rect"].getP1().y and 
                    click.y <= door["rect"].getP2().y):
                    choice = i
                    break
            
            # verfica se Quit foi clicado
            if (click.x >= quit_btn.getP1().x and 
                click.x <= quit_btn.getP2().x and
                click.y >= quit_btn.getP1().y and 
                click.y <= quit_btn.getP2().y):
                playing = False
                break
        
        # processa a escolha da porta
        if playing:
            chosen_door = doors[choice]
            
            # Verifica vitória
            if choice == winner:
                wins += 1
                message.setText("Ganhaste!")
                chosen_door["rect"].setFill("green")
            else:
                losses += 1
                message.setText(f"Perdeste, a porta certa era {winner+1}")
                chosen_door["rect"].setFill("red")
                win_door["rect"].setFill("green")
            
            # atualiza os vitorias e derrotas
            score.setText(f"Vitórias: {wins}  Derrotas: {losses}")
            
            time.sleep(1.5)
            
            # cores das portas inicias
            for door in doors:
                door["rect"].setFill("lightblue")
    
    # Fecha a janela ao sair
    win.close()

if __name__ == "__main__":
    main()