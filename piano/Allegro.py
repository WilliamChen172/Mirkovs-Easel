'''
Created on Jul 18, 2015

@author: William
'''
import math
import random
import pygame
import time
from random import randint




pygame.mixer.init()
noteC4 = pygame.mixer.Sound("C:\\Users\\William\\Desktop\\Piano Notes\\C4.wav")
noteD4 = pygame.mixer.Sound("C:\\Users\\William\\Desktop\\Piano Notes\\D4.wav")
noteE4 = pygame.mixer.Sound("C:\\Users\\William\\Desktop\\Piano Notes\\E4.wav")
noteF4 = pygame.mixer.Sound("C:\\Users\\William\\Desktop\\Piano Notes\\F4.wav")
noteG4 = pygame.mixer.Sound("C:\\Users\\William\\Desktop\\Piano Notes\\G4.wav")
noteA4 = pygame.mixer.Sound("C:\\Users\\William\\Desktop\\Piano Notes\\A4.wav")
noteB4 = pygame.mixer.Sound("C:\\Users\\William\\Desktop\\Piano Notes\\B4.wav")
noteC5 = pygame.mixer.Sound("C:\\Users\\William\\Desktop\\Piano Notes\\C5.wav")
noteE5 = pygame.mixer.Sound("C:\\Users\\William\\Desktop\\Piano Notes\\E5.wav")

class Note:
    def __init__(self, name):
        self.name = name
        self.sound = pygame.mixer.Sound("C:\\Users\\William\\Desktop\\Piano Notes\\" + name + ".wav")
        
    def addNext(self, list_of_next):
        self.list_of_next = list_of_next
        
    def getNext(self):
        random_index = randint(0, len(self.list_of_next) - 1)
        return self.list_of_next[random_index]
    
    def play(self):
        self.sound.play()
        

c4 = Note("C4")
d4 = Note("D4")
e4 = Note("E4")
f4 = Note("F4")
g4 = Note("G4")
a4 = Note("A4")
b4 = Note("B4")    
c5 = Note("C5")    


c4.addNext([e4, g4, c5])
d4.addNext([c4, g4, a4, b4])
e4.addNext([a4, c5])
f4.addNext([d4, g4, b4])
g4.addNext([e4, b4, c4])
a4.addNext([d4, f4])
b4.addNext([d4, g4])
c5.addNext([e4, g4, b4])



note = c4
note.play()
for i in range(20):
    start = time.time()
    note = note.getNext()
    note.play()
    
    while time.time() < 0.5 + start:
        pass
    
    
    
    


    
    
    