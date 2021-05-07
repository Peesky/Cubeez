import pygame

class bouton:
    def __init__(self,img,taille,x,y,overimg=False):
        self.img=pygame.transform.scale(pygame.image.load(img),taille)
        self.taille = taille
        self.x=x
        self.y=y


        self.overbtn=False
        self.mousestate=pygame.mouse.get_pressed()
        self.mousePos=pygame.mouse.get_pos()
        self.overimg(overimg,taille,img)
        self.appuyé=False
        self.size=pygame.display.get_window_size()

        self.rect=self.img.get_rect()
        self.rect.x=self.size[0]/2+self.x
        self.rect.y=self.size[0]/2+self.y

    def afficherimg(self,screen):
        if self.overbtn:
            screen.blit(self.overimg,self.rect)
        else:
            screen.blit(self.img,self.rect)

    def overimg(self,inp,taille,img):
        if inp != False:
            self.overimg=pygame.transform.scale(pygame.image.load(inp),taille)
        else:
            self.overimg=pygame.transform.scale(pygame.image.load(img),taille)

    def isoverbtn(self):
        xmin=self.rect.x
        xmax=self.rect.x+self.taille[0]
        ymin=self.rect.y
        ymax=self.rect.y+self.taille[1]
        
        if xmin<self.mousePos[0]<xmax and ymin<self.mousePos[1]<ymax:
            self.overbtn=True
        else:
            self.overbtn=False

    def clickbtn(self,):
        if self.overbtn:
            if self.mousestate[0]:
                self.appuyé=True                
    
    def update(self,screen,):
        self.mousePos=pygame.mouse.get_pos()
        self.afficherimg(screen)
        self.isoverbtn()
        self.clickbtn()
        self.mousestate=pygame.mouse.get_pressed()
        self.size=pygame.display.get_window_size()
        
        
        self.rect.x=self.size[0]/2+self.x
        self.rect.y=self.size[1]/2+self.y
        
        

