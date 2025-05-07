#--Grupo 19, Hugo Silva--107203, Miguel Dinis--109318

#--Tier1.py (Implementação 1)

from graphics import * 
import time
from Tables import *
from Waiter import *
import math

def Implementacao1 ():
    #Gerar a janela
    win = GraphWin ("Restaurante", 800, 600)
    win.setBackground("#DCDCDC")

    raiomesac = 70

    #Gerar as mesas
    mesa2 = TableR(win, 110, 100, "#986B41")
    mesa4 = TableR(win, 530, 380, "#986B41")
    mesa3 = TableC(win, 180, 440, "#986B41", raiomesac)
    mesa1 = TableC(win, 590, 160, "#986B41", raiomesac)
    mesasretangulares = [mesa4, mesa2]
    mesascirculares = [mesa1, mesa3]
    pratos = Pratos(win, 590, 160)
    pratos1 = Pratos(win, 180, 440)
    pratos2 = Pratos(win, 600, 450)
    pratos3 = Pratos(win, 180, 170)

    #Gerar as docking station
    dock1 = Dock(win, 0, 540, "#DCDCDC", "black")
    dock2 = Dock(win, 740, 0, "#DCDCDC", "black")

    #Gerar o robo
    radius = 30
    robo = Waiter(win, 770, radius)
    dx = 0
    dy = 1
    ypagina = 600
    xpagina = 800
    distMesasrectangulares = raiomesac + radius #Tamanho do raio das mesas = 70 mais o raio do robo = 30

    Flag = True
    while True:
        Flag = True
        if  robo.getCenter().getY() + radius >= ypagina : #Função para verificar se o robo bate na parte de baixo da pagina
                for i in range(2*radius): # Ao bater na parte de baixo da pagina andar 1 diametro do robo para a esquerda
                    if robo.getCenter().getX() > radius:
                        robo.move(-1,0)
                        time.sleep(0.005)
                robo.move(0,-1)
                dy = dy * -1
        if robo.getCenter().getX() <= 31 and robo.getCenter().getY() >= 569: # Quando chega á dock da esquerda para de trabalhar
            break


        if robo.getCenter().getY() - radius < 0: #Função para verificar se o robo bate na parte de cima da pagina
            for i in range(2*radius): # Ao bater na parte de cima da pagina andar 1 diametro do robo para a esquerda
                if robo.getCenter().getX() > radius:
                    robo.move(-1,0)
                    time.sleep(0.005)
            
            localc = robo.getCenter().getX()
            robo.move(0,1)
            dy = dy * -1

        for mesas in mesascirculares: # Verificar a lista das mesas para verificar se há colisão com as mesas circulares
            tetomesa = mesas.getCenter().getY() - raiomesac - radius# Limita a parte de cima da mesa
            chaomesa = mesas.getCenter().getY() + raiomesac + radius# Limita a parte de baixo da mesa 
            distCentrosX = mesas.getCenter().getX() - robo.getCenter().getX()# Diferença entre o centro das mesas e o centro do robo no eixo do X
            distCentrosY = mesas.getCenter().getY() - robo.getCenter().getY()# Diferença entre o centro das mesas e o centro do robo no eixo do Y
            ladodireitomesa = mesas.getCenter().getX() + radius + raiomesac# Limita o lado direito da mesa 
            ladoresquerdomesa = mesas.getCenter().getX() - radius - raiomesac# Limita o lado esquerdo da mesa
            norma = distance(robo.getCenter(), mesas.getCenter()) #Distância entre os centros da mesa e do robo
            while norma <= distMesasrectangulares: # Quando o robo está perto da mesa
                if robo.getCenter().getX() >= xpagina/2: #Na metade da sala vai realizar estas funções
                    while distCentrosX < 0 and distCentrosY > 0 and robo.getCenter().getX() < ladodireitomesa: # Quando o robo colide na mesa pelo lado direito superior anda 1 para a direita 
                        norma = distance(robo.getCenter(), mesas.getCenter())
                        robo.move(1,0)
                        time.sleep(0.005)
                        
                        while distCentrosY > 0 and norma >= distMesasrectangulares and robo.getCenter().getX() < ladodireitomesa: #Quando a mesa colide pelo lado direito superior da mesa anda 1 para baixo
                            norma = distance(robo.getCenter(), mesas.getCenter())
                            robo.move(0,1)
                            time.sleep(0.005)
        
                    while distCentrosX < 0 and distCentrosY <= 0 and robo.getCenter().getX() <= ladodireitomesa and robo.getCenter().getY() < chaomesa:#Função para o robo contornar a parte de baixo do circulo
                        norma = distance(robo.getCenter(), mesas.getCenter())
                        robo.move(-1,0)
                        time.sleep(0.005)
                        
                        while distCentrosY <= 0 and norma  <= distMesasrectangulares and  mesas.getCenter().getX() <= robo.getCenter().getX() <= ladodireitomesa:#Quando o robo colide pelo lado direito em baixo
                            norma = distance(robo.getCenter(), mesas.getCenter())
                            robo.move(0,1)
                            time.sleep(0.005)
                        dx = 0
                        dy = 1
                        robo.move(dx,dy)
                        time.sleep(0.005)
                    while distCentrosX > 0 and distCentrosY < 0 and robo.getCenter().getX() >= ladoresquerdomesa:# Função para quando colide por baixo mover-se para a esquerda
                        norma = distance(robo.getCenter(), mesas.getCenter())
                        robo.move(-1,0)
                        time.sleep(0.005)
                        while distCentrosX >= 0 and distCentrosY < 0 and robo.getCenter().getX() > ladoresquerdomesa and norma >= distMesasrectangulares and  mesas.getCenter().getY() < robo.getCenter().getY() <= chaomesa :# Função para quando colide por baixo mover-se para cima
                            norma = distance(robo.getCenter(), mesas.getCenter())
                            robo.move(0,-1)
                            time.sleep(0.005)

                if robo.getCenter().getX() <= xpagina/2:
                    while distCentrosX < 0 and distCentrosY < 0 and robo.getCenter().getX() < ladodireitomesa: #Contorna pela parte inferior direita dos circulos
                        norma = distance(robo.getCenter(), mesas.getCenter())
                        robo.move(1,0)
                        time.sleep(0.005)
                        while distCentrosX < 0 and  distCentrosY < 0 and robo.getCenter().getX() < ladodireitomesa and norma >= distMesasrectangulares:
                            norma = distance(robo.getCenter(), mesas.getCenter())
                            robo.move(0,-1)
                            time.sleep(0.005)
                    while distCentrosX < 0 and distCentrosY >= 0 and  mesas.getCenter().getX() <= robo.getCenter().getX() <= ladodireitomesa and tetomesa < robo.getCenter().getY():#Contonar pela parte superior direita dos circulos quando vem de baixo
                        norma = distance(robo.getCenter(), mesas.getCenter())
                        robo.move(-1,0)
                        time.sleep(0.005)
                        while distCentrosX <= 0 and distCentrosY >= 0 and  mesas.getCenter().getX()<= robo.getCenter().getX() <= ladodireitomesa and norma <= distMesasrectangulares:
                            norma = distance(robo.getCenter(), mesas.getCenter())
                            robo.move(0,-1)
                            time.sleep(0.005)
                        dy = -1
                        dx = 0
                        robo.move(dx,dy)
                        time.sleep(0.005)
                    while distCentrosX > 0 and distCentrosY > 0 and robo.getCenter().getX() > ladoresquerdomesa: # Contorna a mesa circular pela parte superior esquerda
                        norma = distance(robo.getCenter(), mesas.getCenter())
                        robo.move(-1,0)
                        time.sleep(0.005)
                        while distCentrosX > 0 and distCentrosY > 0 and robo.getCenter().getX() > ladoresquerdomesa and norma >= distMesasrectangulares:
                            norma = distance(robo.getCenter(), mesas.getCenter())
                            robo.move(0,1)
                            time.sleep(0.005)
                    while distCentrosX > 0 and distCentrosY <= 0 and mesas.getCenter().getX() - 41 > robo.getCenter().getX() >= ladoresquerdomesa:# Contorna a mesa circular pela parte inferior esquerda
                        norma = distance(robo.getCenter(), mesas.getCenter())
                        robo.move(1,0)
                        time.sleep(0.005)
                        while distCentrosX > 0 and distCentrosY <= 0 and norma <= distMesasrectangulares and robo.getCenter().getY() < chaomesa:
                            norma = distance(robo.getCenter(), mesas.getCenter())
                            robo.move(0,1)
                            time.sleep(0.005)
                        dy = 1
                        dx = 0
                        robo.move(dx,dy)
                        time.sleep(0.005)
        for mesas in mesasretangulares: # Verificar a lista das mesas para verificar se há colisão com as mesas retangulares
            distCentrosX = mesas.getCenter().getX() - robo.getCenter().getX() # Diferença entre o centro das mesas e o centro do robo no eixo do X
            distCentrosY = mesas.getCenter().getY() - robo.getCenter().getY() # Diferença entre o centro das mesas e o centro do robo no eixo do Y
            ladodireitomesa = mesas.getCenter().getX() + radius + raiomesac # Limita o lado direito da mesa 
            ladoresquerdomesa = mesas.getCenter().getX() - radius - raiomesac # Limita o lado esquerdo da mesa 
            chaomesa = mesas.getCenter().getY() + raiomesac + radius # Limita a parte de baixo da mesa 
            tetomesa = mesas.getCenter().getY() - raiomesac - radius # Limita a parte de cima da mesa
            local = robo.getCenter().getX()#Sitio onde o robo colidiu na mesa no eixo do X
            
            while ladoresquerdomesa <= robo.getCenter().getX() <= ladodireitomesa and tetomesa <= robo.getCenter().getY() <= chaomesa: #Função para verificar se o robo esta a chegar perto de alguma mesa
                if distMesasrectangulares >= abs(distCentrosY): #Verificar se o robo colide na mesa em relação ao eixo do Y
                    if distCentrosY > 0: #Designa que o robo colidiu pela parte superior da mesa
                        if distCentrosX > 0: #Designa que o robo está á esquerda do centro
                                dx = -1
                                dy = 0
                                robo.move(dx,dy)
                                time.sleep(0.001)
                        if distCentrosX < 0: #Designa que o robo está á direita do centro
                                dx = 1
                                dy = 0
                                robo.move(dx,dy)
                                time.sleep(0.001)
                        distX1 = int(abs(robo.getCenter().getX() - local))
                        while robo.getCenter().getX() == ladodireitomesa and tetomesa <= robo.getCenter().getY() <= chaomesa : 
                            for i in range(201):#Contorna a distância certa da mesa pelo lado direito ao descer
                                dx = 0
                                dy = 1
                                robo.move(dx,dy)
                                time.sleep(0.005)
                            for i in range(distX1): # Deixa de contornar a mesa no mesmo ponto (do eixo X) que colidiu na parte superior da mesa
                                dx = -1
                                dy = 0
                                robo.move(dx,dy)
                                time.sleep(0.005)
                            dx = 0
                            dy = 1
                            robo.move(dx,dy)
                            time.sleep(0.005)
                        while robo.getCenter().getX() == ladoresquerdomesa and tetomesa <= robo.getCenter().getY() <= chaomesa : 
                            for i in range(201):#Contorna a distância certa da mesa pelo lado esquerdo ao descer
                                dx = 0
                                dy = 1
                                robo.move(dx,dy)
                                time.sleep(0.005)
                            for i in range(distX1): # Deixa de contornara a mesa no mesmo ponto (do eixo X) que colidiu na parte superior da mesa 
                                dx = 1
                                dy = 0
                                robo.move(dx,dy)
                                time.sleep(0.005)
                            dx = 0
                            dy = 1
                            robo.move(dx,dy)
                            time.sleep(0.005)
                    if distCentrosY < 0: #Designa que o robo colidiu pela parte inferior da mesa
                        if distCentrosX > 0: #Designa que o robo está á esquerda do centro
                            dx = -1
                            dy = 0
                            robo.move(dx,dy)
                            time.sleep(0.001)
                        if distCentrosX < 0: #Designa que o robo está á direita do centro
                            dx = 1
                            dy = 0
                            robo.move(dx,dy)
                            time.sleep(0.001)
                        if robo.getCenter().getX() >= ladodireitomesa: #Verificar se a disância entre os centro é menor á constante designada (=100) para ele contornar a mesa
                            dx = 0
                            dy = -1
                            robo.move(dx,dy)
                            time.sleep(0.001)
                        distX2 = int(abs(robo.getCenter().getX() -local))
                        while robo.getCenter().getX() == ladoresquerdomesa and tetomesa <= robo.getCenter().getY() <= chaomesa:
                            for i in range(201): #Contorna a distância certa da mesa pelo lado esquerdo ao subir
                                dx = 0
                                dy= -1
                                robo.move(dx,dy)
                                time.sleep(0.001)
                            for i in range(distX2):# Deixa de contornar a mesa no mesmo ponto (eixo X) que colidiu na parte inferior da mesa
                                dx = 1
                                dy = 0
                                robo.move(dx,dy)
                                time.sleep(0.005)
                            dx = 0
                            dy = -1
                            robo.move(dx,dy)
                            time.sleep(0.005)
                        while robo.getCenter().getX() == ladodireitomesa and tetomesa <= robo.getCenter().getY() <= chaomesa:
                            for i in range(201): #Contorna a distância certa da mesa pelo lado esquerdo
                                dx = 0
                                dy= -1
                                robo.move(dx,dy)
                                time.sleep(0.001)
                            for i in range(distX2):# Deixa de contornar a mesa no mesmo ponto (eixo X) que colidiu na parte inferior da mesa
                                dx = -1
                                dy = 0
                                robo.move(dx,dy)
                                time.sleep(0.005)
                            dx = 0
                            dy = -1
                            robo.move(dx,dy)
                            time.sleep(0.005)
        robo.move(dx,dy)
        time.sleep(0.001)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    Implementacao1()