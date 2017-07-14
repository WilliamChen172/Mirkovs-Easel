'''
Created on Jul 17, 2015

@author: William
'''

import math
import random
import pygame
import time
from random import randint




pygame.mixer.init()
noteC4 = pygame.mixer.Sound("Piano Notes\\C4.wav")
noteD4 = pygame.mixer.Sound("Piano Notes\\D4.wav")
noteE4 = pygame.mixer.Sound("Piano Notes\\E4.wav")
noteF4 = pygame.mixer.Sound("Piano Notes\\F4.wav")
noteG4 = pygame.mixer.Sound("Piano Notes\\G4.wav")
noteA4 = pygame.mixer.Sound("Piano Notes\\A4.wav")
noteB4 = pygame.mixer.Sound("Piano Notes\\B4.wav")
noteC5 = pygame.mixer.Sound("Piano Notes\\C5.wav")
noteE5 = pygame.mixer.Sound("Piano Notes\\E5.wav")

notes = [noteC4, noteC4, noteD4, noteE4, noteF4, noteG4, noteG4, noteA4, noteB4, noteC5]

# harmony1 = [noteC4, noteE4, noteF4, noteG4, noteC5]
# harmony2 = [noteD4, noteF4, noteG4, noteA4]
# def melody1():
#     for x in range(0,100):
#         start = time.time()
#         random_index = random.randint(0,4)
#         harmony1[random_index].play()
#                  
#         while time.time() < notes[random_index].get_length()/4 + start:
#             pass
#      
# def melody2():
#     for x in range(0,100):
#         start = time.time()
#         random_index = random.randint(0,3)
#         harmony2[random_index].play()
#                  
#         while time.time() < notes[random_index].get_length()/4 + start:
#             pass
#  
# melody2()
# melody1()


chord1 = [[noteE4, False], [noteG4, False], [noteC5, False]]
chord2 = [[noteC4, False], [noteG4, False], [noteA4, False], [noteB4, False]]
chord3 = [[noteA4, False], [noteC5, False]]
chord4 = [[noteD4, False], [noteG4, False], [noteB4, False]]
chord5 = [[noteE4, False], [noteB4, False], [noteC5, False]]
chord6 = [[noteD4, False], [noteF4, False]]
chord7 = [[noteD4, False], [noteG4, False]]
chord8 = [[noteE4, False], [noteG4, False], [noteB4, False]]


# noteC4.play()

def melody3():
    print ("melody3")
    for x in range(20):
        start = time.time()
        random_index = randint(0,2)
        chord1[random_index][0].play()
        chord1[random_index][1] = True
        print (x, random_index)
        #E4
        if chord1[0][1] or chord5[0][1] or chord8[0][1] == True:
             chord3[random_index][0].play()
             chord3[random_index][1] = True
         #G4
        elif chord1[1][1] or chord2[1][1] or chord4[1][1] or chord7[1][1] or chord8[1][1] == True:
             chord5[random_index][0].play()
             chord5[random_index][1] = True
         #D4
        elif chord4[0][1] or chord6[0][1] or chord7[0][1] == True:
             chord2[random_index][0].play() 
             chord2[random_index][1] = True    
         #F4
        
            
        
        
                   
        while time.time() <0.5 + start:
            pass
 
melody3()
# [ [note1, True], [note2, False], [note3, False] ]
# 
# 
# 
# 
# 
# if 5 > 3:
















