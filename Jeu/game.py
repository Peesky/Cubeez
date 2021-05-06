import pygame
from sprites import *


class game():
    def __init__(self):
        Color=[255,255,255]
        self.player=pl()
        self.Me=[mech()]
        self.nb=len(self.Me)
        self.Nombre=0
        self.size=pygame.display.get_window_size()
        self.game=True
    
    def afficherimgmenu(self):
        self.icone=pygame.transform.scale(pygame.image.load("Cubeez/JEU/iconn.PNG"),(440,130))

        x=self.size[0]/2

        self.rect=self.icone.get_rect()
        self.rect.x=x-220
        self.rect.y=0


    def afficherbestscre(self,screen):
        fic = open("Cubeez/playerdata.txt", "r")
        score=fic.read()
        fic.close()
        x=self.size[0]/2-100
        y=self.size[1]/2-18
        font = pygame.font.Font('freesansbold.ttf', 32)
        score = font.render("BEST SCORE : " + str(score), True, (0,0,0))
        screen.blit(score, (x,y))


    def upd(self,screen):
        self.size=pygame.display.get_window_size()
        self.player.upd(self,screen)
        self.nb=len(self.Me)
        self.Nombre+=1
        
        if self.Nombre%500==0:
            self.Me.append(mech())
        for i in range(self.nb):
            self.Me[i].upd(self,screen)

    def update(self,screen):
        self.afficherbestscre(screen)
        self.size=pygame.display.get_window_size()
        self.afficherimgmenu()
        screen.blit(self.icone,self.rect)
