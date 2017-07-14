'''
Created on Jul 18, 2015

@author: Damien & Howie & Matt
'''

import pygame, random, UITesting, math, threading
import numpy as np, Blues2FinalProject as B2FP
import pygame._view

def music():
    print("music functions")
    music_gen = B2FP.Music_Generator()
    music_gen.start_the_music()
    
class Palette:
    def loadImage(self):
        imgAmt = 49
        i = random.randrange(imgAmt)
        self.imgFile = 'paletteTest'+ str(i+1) + '.jpg'
        print('Image: ' + self.imgFile)
        return pygame.image.load(self.imgFile)
    
            
    def __init__(self):
        self.running = True
        self.screen_size = [700, 700]
        self.screen = pygame.display.set_mode(self.screen_size)
        crouton = pygame.transform.scale(pygame.image.load('crouton.png').convert_alpha(), (32, 32))
        pygame.display.set_icon(crouton)
        self.goButton = Button([300, 565], self.screen, 'GOApple.png')
        self.againButton = Button([290, 565], self.screen, 'PALETTES.png') 
        self.drawButton = Button([275, 620], self.screen, 'EXAMPLE.png')
        self.oButton = Button([150, 40], self.screen, 'originalButton.jpg')
        self.sButton = Button([275, 40], self.screen, 'simplifiedButton.jpg')
        self.s2Button = Button([425, 40], self.screen, 'palettedButton.jpg')
        self.title = Button([100, 100], self.screen, 'title.png') 
        self.bg = [255, 255, 255]
        self.screen.fill(self.bg)
              
    def firstMain(self):
        while self.running == True:
            self.title.draw()
            pygame.display.set_caption("Markov's Easel v2.0")
            self.goButton.draw()
            pygame.display.update()
            self.update()
            
    def againMain(self):
        while self.running == True:
            pygame.display.set_caption("Markov's Easel v2.0")
            self.againButton.draw()
            self.drawButton.draw()
            self.oButton.draw()
            self.sButton.draw()
            self.s2Button.draw()
            pygame.display.update()
            self.update()  
            
    def update(self):   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.mixer.quit()
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.goButton.rect.collidepoint(pygame.mouse.get_pos()):
                    print('Loading Palette... ')
                    self.newImg()
                    self.go()
                    self.againMain()
                elif self.againButton.rect.collidepoint(pygame.mouse.get_pos()):
                    print('Loading Palette... ')
                    self.newImg()
                    self.go()
                    self.againMain()
                elif self.oButton.rect.collidepoint(pygame.mouse.get_pos()):
                    print('Original Image... ')
                    self.go()
                elif self.sButton.rect.collidepoint(pygame.mouse.get_pos()):
                    print('Simplified Image... ')
                    self.simplify(self.arrrr)
                elif self.s2Button.rect.collidepoint(pygame.mouse.get_pos()):
                    print('Paletted Image... ')
                    self.simplify2(self.arrrr)
                elif self.drawButton.rect.collidepoint(pygame.mouse.get_pos()):
                    print('Loading Example... ')
                    self.againButton.rect.move(700,700)
                    self.drawButton.rect.move(700,700)
                    art = UITesting.Art(self.colList)
                    art.firstMain()
    
    def newImg(self):
        testImage = self.loadImage()
        self.image = pygame.transform.scale(testImage, (480, 300))
        
    def go(self):
                
        def intToRed(num):
            red = num % 256
            return red
        
        def intToGreen(num):
            green = num // 256 % 256
            return green
        
        def intToBlue(num):
            blue = num // 256 // 256 % 256
            return blue
        
        redArray = []
        blueArray = []
        greenArray = []
        newRedArray = []
        newGreenArray = []
        newBlueArray = []
        self.newColorArray = []
        tempColorArray = []
        counts = []
        peaksList = []
        biggerPeaks = []
        lastList = []
        reallyBigPeaksTrunc = []
        colorDistX = 110
        colorDistY = 420
        
        self.screen.fill(self.bg)       
        self.screen.blit(self.image, [110, 100])
        
        pxarray = pygame.PixelArray(self.image)
        
        for i in pxarray:
            for j in range(300):
                redArray.append(intToRed(i[j])) 
                greenArray.append(intToGreen(i[j]))
                blueArray.append(intToBlue(i[j]))
        
        def newArray(oldArray, newArray):        
            for n in oldArray:
                if n in range(50):
                    newArray.append(25)
                elif n in range(50, 100):
                    newArray.append(75)
                elif n in range(100, 150):
                    newArray.append(125)
                elif n in range(150, 200):
                    newArray.append(175)
                elif n in range(200, 256):
                    newArray.append(225)
        
        newArray(redArray, newRedArray)
        newArray(greenArray, newGreenArray)
        newArray(blueArray, newBlueArray)
        
        self.arrrr = []
        self.rgbthree = []

        for i in range(144000):
            self.newColorArray.append(newRedArray[i])
            self.newColorArray.append(newGreenArray[i])
            self.newColorArray.append(newBlueArray[i])
            self.rgbthree = [newRedArray[i], newGreenArray[i], newBlueArray[i]]
            self.arrrr.append(self.rgbthree)
        
        def makeZero():    
            for i in range(5):
                innerCounts = []
                for j in range(5):
                    mostCounts = []
                    for k in range(5):
                        mostCounts.append(0)
                    innerCounts.append(mostCounts)
                counts.append(innerCounts)
                
        makeZero()
            
        for i in range(0, len(self.newColorArray), 3):
            for j in range(3):
                tempColorArray.append(self.newColorArray[i+j])
            counts[tempColorArray[0] // 50][tempColorArray[1] // 50][tempColorArray[2] // 50] += 1
            tempColorArray = []
        
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    if not k == 0 and not k == 4 and counts[i][j][k] > counts[i][j][k+1] and counts[i][j][k] > counts[i][j][k-1]:
                        peaksList.append(counts[i][j][k])
                    elif k == 0:
                        if counts[i][j][k] != 0:
                            peaksList.append(counts[i][j][k])
                    elif k == 4:
                        if counts[i][j][k] != 0:
                            peaksList.append(counts[i][j][k])
        
        def getPeaks(oldPeak, newPeak):                
            for i in range(1, len(oldPeak)-1):
                if oldPeak[i] > oldPeak[i+1] and oldPeak[i] > oldPeak[i-1]:
                    newPeak.append(oldPeak[i])
            newPeak.append(oldPeak[0])
            newPeak.append(oldPeak[len(oldPeak)-1])
        
        getPeaks(peaksList, biggerPeaks)
        
        biggerPeaks.sort()
        
        if len(biggerPeaks) >= 5:
            for i in range(5):
                reallyBigPeaksTrunc.append(biggerPeaks[i])
        else:
            for i in range(len(biggerPeaks)):
                reallyBigPeaksTrunc.append(biggerPeaks[i])
        
        def getIndexNums(peak):
            finalColor = []
            for i in range(5):
                for j in range(5):
                    if peak in counts[i][j]:
                        finalColor.append(i)
                        finalColor.append(j)
                        finalColor.append(counts[i][j].index(peak))
                        return finalColor

        self.colList = []
        for i in reallyBigPeaksTrunc:
            indList = getIndexNums(i)
            for j in indList:
                lastList.append(j * 50 + 25)
            color = lastList
            self.colList.append(color)
            c = ColorDisplay([colorDistX, colorDistY], self.screen, color)
            c.draw()
            colorDistX += 96
            lastList = []
        print('Your Palette: ' + str(self.colList))
            
        
    def simplify(self, arraydeal):
        bigList = []
        count = 0
        for c in range(480):
            rowList = []
            for r in range(300):
                rowList.append(arraydeal[count])
                count += 1
            bigList.append(rowList)
        thing = np.asarray(bigList)
        thingsurf = pygame.surfarray.make_surface(thing)
        self.screen.blit(thingsurf, [110, 100])
        pygame.display.update()
    
    def simplify2(self, arraydeal2):
        print('Loading...')
        for t in range(144000):
            
            distList = []    
              
            for e in range(5):
                dist = ret(arraydeal2[t], self.colList[e])
                distList.append(dist)
                
            m = min(distList)
            
            for c in range(5):
                if distList[c] == m:
                    arraydeal2[t] = self.colList[c]
            
        print("...")
        self.simplify(arraydeal2)
        
def ret(p1, p2):
    dist = math.sqrt((p2[2]-p1[2])**2+(p2[1]-p1[1])**2+(p2[0]-p1[0])**2)
    return dist
                            
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
        
class ColorDisplay:

    def __init__(self, position, screen, color):
        self.position = position
        self.screen = screen
        self.color = color
        self.surface = pygame.Surface((96, 50))
        
    def draw(self):
        self.surface.unlock()
        self.screen.unlock()
        self.surface.fill(self.color)
        self.screen.blit(self.surface, self.position)
        
class RGBDisplay:
    def __init__(self, position, screen, rgb):
        self.position = position
        self.screen = screen
        self.rgb = rgb
        self.surface = pygame.Surface((96, 50))
        
    def draw(self):
        self.surface.unlock()
        self.screen.unlock()
        self.screen.blit(self.surface, self.position)

if __name__ == '__main__':                  
    threading.Thread(target = music).start()
    palette = Palette()
    palette.firstMain()