import pygame
from sprites import *
from bouton import bouton

class menu():
    def __init__(self):
        self.size=pygame.display.get_window_size()
        self.btnplay=pygame.transform.scale(pygame.image.load("Assets/BTN_play1.PNG"),(300,80))
        self.btnplay_over=pygame.transform.scale(pygame.image.load("Assets/BTN_play2.PNG"),(300,80))
        self.mousestate=pygame.mouse.get_pressed()
        self.mousePos=pygame.mouse.get_pos()
        self.play=False
        self.overplay=False
        self.run =False
        self.music=True


        self.btnplay=bouton("Assets/BTN_play1.PNG",(300,80),-135,+20,"Assets/BTN_play2.PNG",)

    
    def fctbtnplay(self):
        if self.btnplay.appuyé==True:
            self.run=True
        
    def fctbtnmusic(self):
        if self.btnmusic.appuyé:
            self.music=True 


    def afficherimgmenu(self,screen):
        self.icone=pygame.transform.scale(pygame.image.load("Assets/iconn.PNG"),(440,130))
        x=self.size[0]/2
        self.rect=self.icone.get_rect()
        self.rect.x=x-220
        self.rect.y=0
        screen.blit(self.icone,self.rect)

    def update(self,screen):
        self.btnplay.update(screen,)

        self.mousePos=pygame.mouse.get_pos()
        self.afficherimgmenu(screen)
        self.size=pygame.display.get_window_size()
        self.mousestate=pygame.mouse.get_pressed()
        self.fctbtnplay()        

class game():
    def __init__(self):
        Color=[255,255,255]
        self.music_on=True
        self.player=pl()
        self.menu=menu()
        self.Me=[mech()]
        self.nb=len(self.Me)
        self.Nombre=0
        self.size=pygame.display.get_window_size()
        self.game=True
        self.plscore=self.player.score
    
    def reinit(self):
        self.player.score=0
        self.player=pl()
        self.Me=[mech()]
        self.nb=len(self.Me)
        self.Nombre=0
        self.game=True

    def btnplay(self):
        if self.menu.run==True:
            self.reinit()
    
    def btnmusic(self):
        if not self.menu.music:
            self.music_on=False
        else:
            self.music_on=True

    def afficherbestscre(self,screen):
        fic = open("playerdata.txt", "r")
        score=fic.read()
        fic.close()
        x=self.size[0]/2-120
        y=self.size[1]/2-18
        font = pygame.font.Font('freesansbold.ttf', 32)
        score = font.render("BEST SCORE : " + str(score), True, (0,0,0))
        screen.blit(score, (x,y))

    def afficherscre(self,screen):
        x=self.size[0]/2-90
        y=self.size[1]/2-50
        score = self.plscore
        font = pygame.font.Font('freesansbold.ttf', 32)
        score = font.render("SCORE : " + str(score), True, (0,0,0))
        screen.blit(score, (x,y))


    def playtheme(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Assets/Cubeez_theme.mp3")
        pygame.mixer.music.play(-1)

    def upd(self,screen):
        self.size=pygame.display.get_window_size()
        self.player.upd(self,screen)
        self.nb=len(self.Me)
        self.Nombre+=1
        self.plscore=self.player.score
        
        if self.Nombre%500==0:
            self.Me.append(mech())
        for i in range(self.nb):
            self.Me[i].upd(self,screen)
        self.menu.btnplay.appuyé=False
        

    def update(self,screen):
        self.size=pygame.display.get_window_size()
        self.afficherbestscre(screen)
        self.afficherscre(screen)
        self.menu.update(screen)
        self.btnplay()
        self.btnmusic()
        self.menu.run=False
        
        

    
