'''
Created on Jul 15, 2015

@author: Damien & Howie & Matt (Matt did this line [at least part of it])
'''

import pygame, sys, random
import time
import math
from pygame.locals import *

limegreen = [50, 255, 80]
bg = [93, 27, 55]
grey4 = [196, 196, 196]
red = [255,0,0]
green = [7,150,11]
blue = [0,0,255]
white = [117,221,221]
black = [146,151,196]
yellow = [255,255,0]
purple = [147,104,183]
brown = [170,62,152]
gold = [255,215,0]
orange = [61,102,156]

#white black yellow purple brown orange

pygame.display.init()

class Art:
    
    background_color = bg
    
    '''mus = []  
    for m in range(6):
        mus.append(m)
           
    nameCall = mus[random.randrange(0, 6)]
    song = str(nameCall) + ".mp3"    

    pygame.mixer.init()
    pygame.mixer.music.load(song)
    pygame.mixer.music.set_volume(.5)
    pygame.mixer.music.play(-1, 0.0)'''
    
    def __init__(self):
        self.running = True
        self.screen_size = [700, 700]
        self.screen = pygame.display.set_mode(self.screen_size)
        self.goButton = Button([325, 625], self.screen, 'GO.png')
        self.againButton = Button([325, 625], self.screen, 'AGAIN.png')
        #self.musButton = Button([0,0], self.screen, 'crouton.png')
        '''
        self.smallButton = Button([3/4*self.screen_size[0]-50, 75], self.screen, 'GO.png')
        self.mediumBbutton = Button([1/4*self.screen_size[0]-25, 75], self.screen, 'GO.png')
        self.largeButton = Button([1/2*self.screen_size[0]-25, 75], self.screen, 'GO.png')
        self.button6 = Button([3/4*self.screen_size[0]-25, 75], self.screen, 50, 50, green)
        '''
        
    '''def nextSong(self):    
        mus = []  
        for m in range(6):
            mus.append(m)
           
        nameCall = mus[random.randrange(0, 5)]
        song = str(nameCall) + ".mp3"    
        nameCall = nameCall+1
        if nameCall == 6:
            nameCall = 0
        song = str(nameCall) + ".mp3"  
        
        pygame.mixer.music.load(song)
        pygame.mixer.music.set_volume(.5)
        pygame.mixer.music.play(-1, 0.0)  '''   
        
    def again(self):
        self.otherMain()
        
    def otherMain(self):
            
        self.goButton.rect.move(0, 0)

        while self.running == True:
            pygame.display.set_caption("Markov's Easel")
            crouton = pygame.transform.scale(pygame.image.load('crouton.png').convert_alpha(), (32, 32))
            pygame.display.set_icon(crouton)
            self.againButton.draw()
            #self.musButton.draw()
            pygame.display.update()
            self.update()
                
        
   
    def go(self):       
        def intToRGB(int):
            blue =  int % 256
            green = int // 256 % 256
            red =   int // 256 // 256 % 256
            return(red, blue, green)
        
        
        #GENERATOR
        arr=[]
        arr.append(white)
        arr.append(black)
        arr.append(yellow)
        arr.append(purple)
        arr.append(brown)
        arr.append(orange)
        SCREEN_X=500
        SCREEN_Y=500
        
        square = pygame.Surface((20, 20))
        
        for i in range (0+100, SCREEN_X+50, 20):
            for j in range (0+100, SCREEN_Y +100, 20):
                num = random.randrange (0, 6)
                square.fill(arr[num])
                draw_me=pygame.Rect((j+1), (i+1), 20, 20)
                self.screen.blit(square, draw_me)
                self.againButton.draw()
                pygame.display.flip()
                pygame.Surface.unlock(square)
        
        #pxarray = pygame.PixelArray(self.screen)
        #for i in range (0,SCREEN_X,20):
        #    for j in range (0,SCREEN_Y,20):
        #       pixelList.append(intToRGB(pxarray[i][j]))
        #       pass
            
        pygame.event.set_allowed(None)        
        pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
        if self.againButton.rect.collidepoint(pygame.mouse.get_pos()):
            self.again()
        #elif self.musButton.rect.collidepoint(pygame.mouse.get_pos()):
        #    self.nextSong()

    def update(self):    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.goButton.rect.collidepoint(pygame.mouse.get_pos()):
                    self.go()
                #elif self.musButton.rect.collidepoint(pygame.mouse.get_pos()):
                #     self.nextSong()
                    
    def firstMain(self):
        while self.running == True:
            self.screen.fill(self.background_color)
            self.update()
            pygame.display.set_caption("Markov's Easel")
            crouton = pygame.transform.scale(pygame.image.load('crouton.png').convert_alpha(), (32, 32))
            pygame.display.set_icon(crouton)
            self.goButton.draw()
            #self.musButton.draw()
            pygame.display.update()
                       
class Button:        
    def __init__(self, position, screen, image):
        self.position = position
        self.screen = screen 
        self.surface = pygame.image.load(image)
        self.rect = self.surface.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
                
    def draw(self):
        self.surface.unlock()
        self.screen.unlock()
        self.screen.blit(self.surface, self.position)

art = Art()
art.firstMain()            