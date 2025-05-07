#--Grupo 19, Hugo Silva--107203, Miguel Dinis--109318

#--main.py

from graphics import *
from button import *

win= GraphWin("Menu", 800, 600)


title = Text(Point(350, 110), "Robô ajudante")
title.setSize(27)
title.draw(win)
robot = Image((Point(550,110)), "robot.png")
robot.draw(win)

class botão: #Classe para criar os butões
    def __init__(self, win, x, y, color, label,  width=250, height= 40, radius=10):
    # Desenhar forma do butão
        self.circuloQSe= Circle(Point(x, y),radius)
        self.circuloQSe.setFill("lightblue")
        self.circuloQSe.setOutline("lightblue")
        self.circuloQSe.draw(win)



        self.circuloQIe= Circle(Point(x,y + height),radius)
        self.circuloQIe.setFill("lightblue")
        self.circuloQIe.setOutline("lightblue")
        self.circuloQIe.draw(win)


        self.circuloQSd= Circle(Point(x + width, y),radius)
        self.circuloQSd.setFill("lightblue")
        self.circuloQSd.setOutline("lightblue")
        self.circuloQSd.draw(win)


        self.circuloQId= Circle(Point(x + width, y + height),radius)
        self.circuloQId.setFill("lightblue")
        self.circuloQId.setOutline("lightblue")
        self.circuloQId.draw(win)

        self.retangulo1 = Rectangle(Point(x,y-radius), Point (x + width , y + height + radius))
        self.retangulo1.setFill("lightblue")
        self.retangulo1.setOutline("lightblue")
        self.retangulo1.draw(win)

        self.retangulo2 = Rectangle(Point(x- radius, y),Point(x + width + radius, y + height))
        self.retangulo2.setFill("lightblue")
        self.retangulo2.setOutline("lightblue")
        self.retangulo2.draw(win)

        self.label = Text(Point(x  + width/2, y + height/2), label)
        self.label.setFill("Black")
        self.label.draw(win)

        
        botao = Button(win,Point(x  + width/2, y + height/2), 250, 40, label)
        
        return 
    
     

       
                 


        
class exit_botao: #Class para criar o butão exit       

    def __init__(self, win, x= 719, y= 556, width = 81, height = 44):

        self.exit = Rectangle(Point(x,y),Point(x + 81, y + 64 ))
        self.exit.setFill("lightgrey")
        self.exit.setOutline("Black")
        self.exit.draw(win)
        self.sair = Button(win,Point(x  + width/2, y + height/2), 81, 44, "Exit")
        self.image = Image((Point(760,580)), "exit.png")
        self.image.draw(win)

        return

    
    
                 
butao1 = botão(win, 265, 220,"lightblue", "Implementação 1")
butao2 = botão(win, 265, 340,"lightblue", 'Implementação 2') 
butao3 = botão(win, 265, 460,"lightblue", 'Implementação 3')
butaoexit = exit_botao(win)   




while True: #Função para verificar qual dos butões foi clickado e efetuar o que é desejado.
    clicked = False
    click = win.getMouse()
    if 719 < click.getX() < 800 and 556 < click.getY() < 600:
        clicked = True
        if clicked == True:
            win.close()
    
    if 265 < click.getX() < 515 and 220 < click.getY() < 280:
            clicked = True
            if clicked == True:
                  exec(open("Tier1.py").read())
                  
    if 265 < click.getX() < 515 and 340 < click.getY() < 400:
            clicked = True
            if clicked == True:
                  exec(open("Tier2.py").read())
  
    if 265 < click.getX() < 515 and 460 < click.getY() < 520:
            clicked = True
            if clicked == True:
                  exec(open("Tier3.py").read())
    

                




