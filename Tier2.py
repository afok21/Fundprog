#--Grupo 19, Hugo Silva--107203, Miguel Dinis--109318

#--Tier2.py (Implementação 1)

from graphics import *
import time
from Tables import *
from Waiter import *
from button import *


def Implementacao2():
    #Gerar janela
    win1 = GraphWin("IMplementação 2", 800, 600)
    win1.setBackground("#DCDCDC")
    raiomesac = 70


    #Gerar Mesas
    mesa1 = TableC(win1, 590, 160, "#986B41", raiomesac)
    mesa2 = TableR(win1, 110, 100, "#986B41")
    mesa3 = TableC(win1, 180, 440, "#986B41", raiomesac)
    mesa4 = TableR(win1, 530, 380, "#986B41")


    #Gerar as docking station
    dock1 = Dock(win1, 0, 540, "#DCDCDC", "black")
    dock2 = Dock(win1, 740, 0, "#DCDCDC", "black")
    balcao = Dock(win1, 370, 0, "#DCDCDC", "black")
    kitchen = Text(Point(400, 30), "Cozinha")
    kitchen.draw(win1)

    #Gerar o robo
    radius = 30
    robo = Waiter(win1, 770, radius)
    dx = 0
    dy = 1
    ypagina = 600
    xpagina = 800
    click = win1.getMouse()

    distXclick_robo =abs(robo.getCenter().getX() - click.getX())
    distYclick_robo = robo.getCenter().getY() - click.getY()

    norma1 = distance(robo.getCenter(), mesa1.getCenter())
    norma2 = distance(robo.getCenter(), mesa2.getCenter())
    norma3 = distance(robo.getCenter(), mesa3.getCenter())
    norma4 = distance(robo.getCenter(), mesa4.getCenter())
    distancia = raiomesac + radius




    while True:  
        clicked = False
        
        if 520 < click.getX() < 660 and 90 < click.getY() < 230:
            clicked = True
            movey = False

            distancia_atual = distance(robo.getCenter(), mesa1.getCenter())
            
            while clicked:
                if not movey and robo.getCenter().getX() >= mesa1.getCenter().getX() and distancia_atual >= distancia: #faz com que o robo se dirija a mesa clicada no eixo dos X
                    dx = -1
                    dy = 0
                    robo.move(dx, dy)
                    time.sleep(0.005)
                    distancia_atual = distance(robo.getCenter(), mesa1.getCenter())
                    
                if robo.getCenter().getX() <= mesa1.getCenter().getX(): #torna movey verdadeiro para que o robo se possa dirigir no eixo dos y
                    movey = True

                if movey and robo.getCenter().getY() <= mesa1.getCenter().getY() and  distancia_atual >= distancia:#faz com que o robo se dirija a mesa clicada no eixo dos Y
                    dx = 0
                    dy = 1
                    robo.move(dx, dy)
                    time.sleep(0.005)
                    distancia_atual = distance(robo.getCenter(), mesa1.getCenter())
                    if distancia_atual == distancia:
                        break
                
            time.sleep(2)
            while True:
                movey = False
                distancia_cozinha = distance(robo.getCenter(), balcao.getCenter())
                if not movey and robo.getCenter().getX() >= balcao.getCenter().getX(): #faz com que o robo se dirija a mesa clicada no eixo dos X
                    dx = -1
                    dy = 0
                    robo.move(dx, dy)
                    time.sleep(0.005)
                    distancia_cozinha = distance(robo.getCenter(), balcao.getCenter())

                if robo.getCenter().getX() <= balcao.getCenter().getX(): #torna movey verdadeiro para que o robo se possa dirigir no eixo dos y
                    movey = True

                if movey and robo.getCenter().getY() >= balcao.getCenter().getY():#faz com que o robo se dirija a mesa clicada no eixo dos Y
                    dx = 0
                    dy = -1
                    robo.move(dx, dy)
                    time.sleep(0.005)
                    distancia_cozinha = distance(robo.getCenter(), balcao.getCenter())
                    
                    if distancia_cozinha == 1:
                        break
            time.sleep(2)  
                
            while True:
                movey = False 
                distancia_atual = distance(robo.getCenter(), mesa1.getCenter())
                if not movey and robo.getCenter().getX() <= mesa1.getCenter().getX() and distancia_atual >= distancia: #faz com que o robo se dirija a mesa clicada no eixo dos X
                    dx = 1
                    dy = 0
                    
                    robo.move(dx, dy)
                    time.sleep(0.005)
                    distancia_atual = distance(robo.getCenter(), mesa1.getCenter())
                    
                if robo.getCenter().getX() <= mesa1.getCenter().getX(): #torna movey verdadeiro para que o robo se possa dirigir no eixo dos y
                    movey = True

                if movey and robo.getCenter().getY() <= mesa1.getCenter().getY() and  distancia_atual >= distancia:#faz com que o robo se dirija a mesa clicada no eixo dos Y
                    dx = 0
                    dy = 1
                    
                    robo.move(dx, dy)
                    time.sleep(0.005)
                    distancia_atual = distance(robo.getCenter(), mesa1.getCenter())
                    if distancia_atual == distancia:
                        break   
            time.sleep(2)          
            while True:
                movey = False
                distancia_dock1 = distance(robo.getCenter(), dock1.getCenter())
                if not movey and robo.getCenter().getX() <= dock1.getCenter().getX(): #faz com que o robo se dirija a mesa clicada no eixo dos X
                    dx = 1
                    dy = 0
                    robo.move(dx, dy)
                    time.sleep(0.005)
                    distancia_dock1 = distance(robo.getCenter(), dock1.getCenter())

                if robo.getCenter().getX() <= dock1.getCenter().getX(): #torna movey verdadeiro para que o robo se possa dirigir no eixo dos y
                    movey = True

                if movey and robo.getCenter().getY() >= dock1.getCenter().getY():#faz com que o robo se dirija a mesa clicada no eixo dos Y
                    dx = 0
                    dy = -1
                    robo.move(dx, dy)
                    time.sleep(0.005)
                    distancia_dock1 = distance(robo.getCenter(), dock1.getCenter())
                    
                    if distancia_dock1 == 1:
                        break 


        if 110 < click.getX() < 250 and 100 < click.getY() < 240:
                clicked = True
                movey = False

                distancia_atual = distance(robo.getCenter(), mesa2.getCenter())
                
                while clicked:
                    if not movey and robo.getCenter().getX() >= mesa2.getCenter().getX() and distancia_atual >= distancia: #faz com que o robo se dirija a mesa clicada no eixo dos X
                        dx = -1
                        dy = 0
                        robo.move(dx, dy)
                        time.sleep(0.005)
                        distancia_atual = distance(robo.getCenter(), mesa2.getCenter())
                        
                    if robo.getCenter().getX() <= mesa2.getCenter().getX(): #torna movey verdadeiro para que o robo se possa dirigir no eixo dos y
                        movey = True

                    if movey and robo.getCenter().getY() <= mesa2.getCenter().getY() and  distancia_atual >= distancia:#faz com que o robo se dirija a mesa clicada no eixo dos Y
                        dx = 0
                        dy = 1
                        robo.move(dx, dy)
                        time.sleep(0.005)
                        distancia_atual = distance(robo.getCenter(), mesa2.getCenter())
                        if distancia_atual == distancia:
                            break
                    
                time.sleep(2)
                while True:
                    movey = False
                    distancia_cozinha = distance(robo.getCenter(), balcao.getCenter())
                    if not movey and robo.getCenter().getX() <= balcao.getCenter().getX(): #faz com que o robo se dirija a mesa clicada no eixo dos X
                        dx = 1
                        dy = 0
                        robo.move(dx, dy)
                        time.sleep(0.005)
                        distancia_cozinha = distance(robo.getCenter(), balcao.getCenter())

                    if robo.getCenter().getX() <= balcao.getCenter().getX(): #torna movey verdadeiro para que o robo se possa dirigir no eixo dos y
                        movey = True

                    if movey and robo.getCenter().getY() >= balcao.getCenter().getY():#faz com que o robo se dirija a mesa clicada no eixo dos Y
                        dx = 0
                        dy = -1
                        robo.move(dx, dy)
                        time.sleep(0.005)
                        distancia_cozinha = distance(robo.getCenter(), balcao.getCenter())
                    
                        if robo.getCenter() == (221, 29):
                            break
                time.sleep(2)  
                    
                while True:
                    movey = False 
                    
                    if not movey and robo.getCenter().getX() >= mesa2.getCenter().getX() and distancia_atual >= distancia: #faz com que o robo se dirija a mesa clicada no eixo dos X
                        dx = -1
                        dy = 0
                        
                        robo.move(dx, dy)
                        time.sleep(0.005)
                        distancia_atual = distance(robo.getCenter(), mesa2.getCenter())
                        
                    if robo.getCenter().getX() >= mesa2.getCenter().getX(): #torna movey verdadeiro para que o robo se possa dirigir no eixo dos y
                        movey = True

                    if movey and robo.getCenter().getY() <= mesa2.getCenter().getY() and  distancia_atual >= distancia:#faz com que o robo se dirija a mesa clicada no eixo dos Y
                        dx = 0
                        dy = 1
                        
                        robo.move(dx, dy)
                        time.sleep(0.005)
                        distancia_atual = distance(robo.getCenter(), mesa2.getCenter())
                        if distancia_atual == distancia:
                            break    
                    

        if 110 < click.getX() < 250 and 370 < click.getY() < 510:
                clicked = True
                movey = False

                distancia_atual = distance(robo.getCenter(), mesa3.getCenter())
                while clicked:
                    if not movey and robo.getCenter().getX() >= mesa3.getCenter().getX() and distancia_atual >= distancia: #faz com que o robo se dirija a mesa clicada no eixo dos X
                        dx = -1
                        dy = 0
                        robo.move(dx, dy)
                        time.sleep(0.005)
                        distancia_atual = distance(robo.getCenter(), mesa3.getCenter())
                        
                    if robo.getCenter().getX() <= mesa3.getCenter().getX(): #torna movey verdadeiro para que o robo se possa dirigir no eixo dos y
                        movey = True

                    if movey and robo.getCenter().getY() <= mesa3.getCenter().getY() and  distancia_atual >= distancia:#faz com que o robo se dirija a mesa clicada no eixo dos Y
                        dx = 0
                        dy = 1
                        robo.move(dx, dy)
                        time.sleep(0.005)
                        distancia_atual = distance(robo.getCenter(), mesa3.getCenter())

                    

        if 530 < click.getX() < 670 and 380 < click.getY() < 520:
                clicked = True
                movey = False

                distancia_atual = distance(robo.getCenter(), mesa4.getCenter())
                while clicked:
                    if not movey and robo.getCenter().getX() >= mesa4.getCenter().getX() and distancia_atual >= distancia: #faz com que o robo se dirija a mesa clicada no eixo dos X
                        dx = -1
                        dy = 0
                        robo.move(dx, dy)
                        time.sleep(0.005)
                        distancia_atual = distance(robo.getCenter(), mesa4.getCenter())
                        
                    if robo.getCenter().getX() <= mesa4.getCenter().getX(): #torna movey verdadeiro para que o robo se possa dirigir no eixo dos y
                        movey = True

                    if movey and robo.getCenter().getY() <= mesa4.getCenter().getY() and  distancia_atual >= distancia:#faz com que o robo se dirija a mesa clicada no eixo dos Y
                        dx = 0
                        dy = 1
                        robo.move(dx, dy)
                        time.sleep(0.005)
                        distancia_atual = distance(robo.getCenter(), mesa4.getCenter())
                    

    win1.getMouse()
    win1.close()

if __name__ == "__main__":
    Implementacao2()