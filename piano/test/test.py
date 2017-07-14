'''
Created on Jul 16, 2015

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

notes = [noteC4, noteC4, noteD4, noteE4, noteF4, noteG4, noteG4, noteA4, noteB4, noteC5]
#noteC4.play(0)
#print(noteC4.get_length())


def scaleC():
    for y in range(0,20):
        for x in range(0,8):
            start = time.time()
            random_index = random.randint(0,9)
            notes[random_index].play()
             
            while time.time() < notes[random_index].get_length()/4 + start:
                pass
             

scaleC()







# time.sleep(100)



