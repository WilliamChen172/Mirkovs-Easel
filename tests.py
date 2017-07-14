
#GROUP 40
import pygame, sys, random
import time
import math
from pygame.locals import *

arr=[]
stuff=[]
RED=(255,10,10)
BLU=(10,255,10)
GRN=(10,10,255)
arr.append(RED)
arr.append(BLU)
arr.append(GRN)
SCREEN_X=200
SCREEN_Y=200

screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
square = pygame.Surface((1,1))


for j in range (SCREEN_Y):
    for i in range (SCREEN_X):
        r = random.random()
        if r<.5:
            num = 0
        if r>.95:
            num = 1
        if r<.95 and r>.5:
            num = 2
        square.fill(arr[num])
        draw_me=pygame.Rect((j+1), (i+1), 1, 1)
        screen.blit(square, draw_me)
        pygame.display.flip()

pxarray = pygame.PixelArray(square)
print(square.unmap_rgb(pxarray))
time.sleep(1)



'''
is dis gud stuf
hoo noes

pxarray = pygame.PixelArray(screen)

print(screen.unmap_rgb(pxarray[1]))

8/8 m8

pixel = square.get_at_mapped((i, j))
col = square.unmap_rgb(pixel) 
stuff.append(col)
'''