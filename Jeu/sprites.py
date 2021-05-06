import pygame
from random import randint
from player import *

class mech():
    def __init__(self):
        self.x=-20
        self.y=randint(0,500)
        self.vitesse=2
        self.Aug=0
        self.rec=pygame.Rect(self.x,self.y,20,20)
    
    def tch(self,Game,screen):
        if Game.player.x-25<self.x<Game.player.x+25 and Game.player.y-25<self.y<Game.player.y+25:
            Game.game=False
        if Game.player.mx-Game.player.ml<self.x<Game.player.mx+Game.player.ml and Game.player.my-Game.player.ml<self.y<Game.player.my+Game.player.ml:
            self.spawn(Game)
            Game.player.score+=1
        
    def bouger(self,Game):        
        if self.y>Game.player.y:
            self.y-=self.vitesse
        if self.y<Game.player.y:
            self.y+=self.vitesse  
        if self.x<Game.player.x:
            self.x+=self.vitesse      
        if self.x>Game.player.x:
            self.x-=self.vitesse   

    def spawn(self,Game):
        self.Aug=randint(1,4)
        if self.Aug==4:
            self.x=randint(0,Game.size[0])
            self.y=Game.size[1]
        if self.Aug==3:
            self.x=randint(0,Game.size[0])
            self.y=-20
        if self.Aug==2:
            self.x=-20
            self.y=randint(0,Game.size[1])
        else:
            self.x=Game.size[0]
            self.y=randint(0,Game.size[1])
    
    def upd(self,Game,screen):
        self.tch(Game,screen)
        self.bouger(Game)
        self.rec=pygame.Rect(self.x,self.y,20,20)
        pygame.draw.rect(screen,'green',self.rec)