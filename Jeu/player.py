import pygame

class pl():
    def __init__(self):
        self.x=350
        self.y=220
        self.vitesse=4
        self.ret=None
        self.rec=pygame.Rect(self.x,self.y,20,20)
        self.score=0

        self.mx=self.x+5
        self.my=self.y+5
        self.ml=10
        self.mv=7
        self.mrect=pygame.Rect(self.mx,self.my,self.ml,self.ml)
        self.GOO=False
        
    def bouger(self,Game):        
        if self.ret=="h" and self.y >1:
            self.y-=self.vitesse
        if self.ret=="b"and self.y < Game.size[1]-20 :
            self.y+=self.vitesse       
        if self.ret=="d" and self.x <Game.size[0]-20:
            self.x+=self.vitesse      
        if self.ret=="g" and self.x >0:
            self.x-=self.vitesse  

    def touches(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game=False
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ret="d"
                elif event.key==pygame.K_LEFT:
                    self.ret="g"
                elif event.key==pygame.K_UP:
                    self.ret="h"
                elif event.key==pygame.K_DOWN:
                    self.ret="b"
                elif event.key==pygame.K_SPACE:
                    self.GOO=True
                    self.mret=self.ret
                    self.tvol=0
    def afficherscre(self,screen):
        font = pygame.font.Font('freesansbold.ttf', 26)
        score = font.render("Score : " + str(self.score), True, (0,0,0))
        screen.blit(score, (0,0))

    def verifybestscore(self):
        fic = open("Cubeez/playerdata.txt", "r")
        score=fic.read()
        fic.close()
        if self.score >int(score):
            fic = open("playerdata.txt", "w")
            fic.write(str(self.score))

        
    def tirer(self):
        if self.GOO:
            if self.mret=="d":
                self.mx+=self.mv
            if self.mret=="g":
                self.mx-=self.mv
            if self.mret=="b":
                self.my+=self.mv
            if self.mret=="h":
                self.my-=self.mv
            if self.tvol>=45:
                self.GOO=False
            self.tvol+=1
        elif not self.GOO:
            self.mx=self.x+5
            self.my=self.y+5     

    def upd(self,Game, screen):
        self.tirer()
        self.mrect=pygame.Rect(self.mx,self.my,self.ml,self.ml)
        pygame.draw.rect(screen,'red',self.mrect)
        
        self.bouger(Game)
        self.touches()
        self.afficherscre(screen)
        self.rec=pygame.Rect(self.x,self.y,20,20)
        pygame.draw.rect(screen,'black',self.rec)
        self.winsize=pygame.display.get_window_size()
        self.verifybestscore()