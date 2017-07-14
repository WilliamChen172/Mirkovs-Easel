'''
Created on Jul 18, 2015

@author: William
'''
import pygame
import random
import time
from random import randint

pygame.mixer.init()

noteC4 = pygame.mixer.Sound("C:\\Users\\William\\Desktop\\Piano Notes\\C4.wav")
noteD4 = pygame.mixer.Sound("C:\\Users\\William\\Desktop\\Piano Notes\\D4.wav")
notebE4 = pygame.mixer.Sound("C:\\Users\\William\\Desktop\\Piano Notes\\bE4.wav")
noteE4 = pygame.mixer.Sound("C:\\Users\\William\\Desktop\\Piano Notes\\E4.wav")
noteF4 = pygame.mixer.Sound("C:\\Users\\William\\Desktop\\Piano Notes\\F4.wav")
notebG4 = pygame.mixer.Sound("C:\\Users\\William\\Desktop\\Piano Notes\\bG4.wav")
noteG4 = pygame.mixer.Sound("C:\\Users\\William\\Desktop\\Piano Notes\\G4.wav")
noteA4 = pygame.mixer.Sound("C:\\Users\\William\\Desktop\\Piano Notes\\A4.wav")
notebC5 = pygame.mixer.Sound("C:\\Users\\William\\Desktop\\Piano Notes\\bC5.wav")
#majorScale = [noteC4, noteD4, notebE4, noteE4, noteG4, noteA4]
minorScale = [noteC4, notebE4, noteF4, notebG4, noteG4, notebC5]





# def major():
#     for y in range(0,20):
#         for x in range(0,8):
#             start = time.time()
#             random_index = random.randint(0,5)
#             majorScale[random_index].play()
#              
#             while time.time() < majorScale[random_index].get_length()/4 + start:
#                 pass
            
def minor():
    for y in range(0,20):
        for x in range(0,8):
            start = time.time()
            random_index = random.randint(0,5)
            minorScale[random_index].play()
             
            while time.time() < minorScale[random_index].get_length()/4 + start:
                pass


minor()










