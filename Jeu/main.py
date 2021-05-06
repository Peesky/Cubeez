import pygame
import time
from random import*
from game import *
#from sprites import *

pygame.init()
gameIcon = pygame.image.load("Cubeez/JEU/icon.PNG")
pygame.display.set_icon(gameIcon)
pygame.display.set_caption("")
screen=pygame.display.set_mode((720,500), pygame.RESIZABLE)
backC=pygame.color.Color("#FFFFFF")
jeu=True



def fond():
    for i in range (0,Game.size[0]):
        if i%20==0:
            pygame.draw.line(screen, (75,75,75), [i,0], [i,Game.size[1]])
    for i in range (0,Game.size[1]):
        if i%20==0:
            pygame.draw.line(screen,(75,75,75), [0,i], [Game.size[0],i])

Game=game()
while True:
    while Game.game:
        screen.fill(backC)
        fond()
        #Game.player.afficherscre()
        
        Game.player.touches()
        Game.upd(screen)

        time.sleep(0.02)
        pygame.display.flip()

    while not Game.game:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game=False
                pygame.quit()
        screen.fill(backC)
        Game.update(screen)
        time.sleep(0.02)
        pygame.display.flip()
    
