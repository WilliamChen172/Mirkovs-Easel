'''
Created on Jul 20, 2015
@author: William
'''
import math, random, pygame, time
from random import randint
from pygame.mixer_music import set_volume

QUARNOTE = 0.4
EIGHTHNOTE = QUARNOTE/2
SIXTEENTHNOTE = QUARNOTE/4
HALFNOTE = QUARNOTE*2
WHOLENOTE = QUARNOTE*4


class Note:
    def __init__(self, name):
        self.name = name
        self.sound = pygame.mixer.Sound("Piano Notes\\" + name + ".wav")
        #print (self.sound.get_length())
        
    def addNext(self, list_of_next):
        self.list_of_next = list_of_next
        
    def getNext(self):
        random_index = randint(0, len(self.list_of_next) - 1)
        return self.list_of_next[random_index]
    
    def play(self):
        self.sound.play()
        
    def stop(self):
        self.sound.stop()
        
    def volume(self, value):
        self.sound.set_volume(value)
        
class Music_Generator():
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 1, 512) 
        pygame.mixer.init()
        self.C4 = Note("C4")
        self.bE4 = Note("bE4")
        self.F4 = Note("F4")
        self.bG4 = Note("bG4")
        self.G4 = Note("G4")
        self.bC5 = Note("bC5")    
        self.C5 = Note("C5") 
        self.bE5 = Note("bE5")
        self.F5 = Note("F5")
        self.bG5 = Note("bG5")
        self.G5 = Note("G5")
        self.bC6 = Note("bC6")
        self.C6 = Note("C6")   
        self.C3 = Note("C3")
        self.C2 = Note("C2")
        self.G2 = Note("G2")
        self.G3 = Note("G3")
        self.F2 = Note("F2")
        self.F3 = Note("F3")
        
        self.C2.volume(0.5)
        self.C3.volume(0.5)
        self.G2.volume(0.5)
        self.G3.volume(0.5)
        self.F2.volume(0.5)
        self.F3.volume(0.5)
                
        self.bassline = [self.C2, self.C3, self.C2, self.C4, self.G2, self.G3, self.F2, self.F3]
        
        self.C4.addNext([self.bE4, self.F4, self.bG4, self.G4, self.bC5])
        self.bE4.addNext([self.C4, self.F4, self.bG4, self.G4, self.bC5, self.C5])
        self.F4.addNext([self.C4, self.bE4, self.bG4, self.G4, self.bC5, self.C5, self.bE5])
        self.bG4.addNext([self.C4, self.bE4, self.F4, self.G4, self.bC5, self.C5, self.bE5, self.F5])
        self.G4.addNext([self.C4, self.bE4, self.F4, self.bG4, self.bC5, self.C5, self.bE5, self.F5, self.bG5])
        self.bC5.addNext([self.C4, self.bE4, self.F4, self.bG4, self.G4, self.C5, self.bE5, self.F5, self.bG5, self.G5])
        self.C5.addNext([self.bE4, self.F4, self.bG4, self.G4, self.bC5, self.bE5, self.F5, self.bG5, self.G5, self.bC6])
        self.bE5.addNext([self.F4, self.bG4, self.G4, self.bC5, self.C5, self.F5, self.bG5, self.G5, self.bC6, self.C6])
        self.F5.addNext([self.bG4, self.G4, self.bC5, self.C5, self.bE5, self.bG5, self.G5, self.bC6, self.C6])
        self.bG5.addNext([self.G4, self.bC5, self.C5, self.bE5, self.F5, self.G5, self.bC6, self.C6])
        self.G5.addNext([self.bC5, self.C5, self.bE5, self.F5, self.bG5, self.bC6, self.C6])
        self.bC6.addNext([self.C5, self.bE5, self.F5, self.bG5, self.G5, self.C6])
        self.C6.addNext([self.bE5, self.F5, self.bG5, self.G5, self.bC5])
        
    def start_the_music(self):
        start = time.time()
        note = self.C4
        bass = self.C3 
        
        while time.time() < QUARNOTE + start:
                pass
            
        for o in range(2048):
            for i in range(32):
                bassPos = i % 8 
                bass = self.bassline[bassPos] 
                bass.play()
                start = time.time()
                note = note.getNext()
                self.rhythm1(i, note)
                bass.stop()
                
            for i in range(32):
                bassPos = i % 8 
                bass = self.bassline[bassPos] 
                bass.play()
                start = time.time()
                note = note.getNext()
                self.rhythm2(i, note)
                 
                bass.stop()
                
                note.stop()
        


# self.C4.addNext([self.bE4, self.F4, self.bG4, self.G4, self.bC5, self.C5])
# self.bE4.addNext([self.C4, self.F4, self.bG4, self.G4, self.bC5, self.C5, self.bE5])
# self.F4.addNext([self.C4, self.bE4, self.bG4, self.G4, self.bC5, self.C5, self.bE5, self.F5])
# self.bG4.addNext([self.C4, self.bE4, self.F4, self.G4, self.bC5, C5, self.bE5, self.F5, self.bG5])
# self.G4.addNext([self.C4, self.bE4, self.F4, self.bG4, self.bC5, C5, self.bE5, self.F5, self.bG5, self.G5])
# self.bC5.addNext([self.C4, self.bE4, self.F4, self.bG4, self.G4, self.C5, self.bE5, self.F5, self.bG5, self.G5, self.bC6])
# self.C5.addNext([self.C4, self.bE4, self.F4, self.bG4, self.G4, self.bC5, self.bE5, self.F5, self.bG5, self.G5, self.bC6, self.C6])
# self.bE5.addNext([self.bE4, self.F4, self.bG4, self.G4, self.bC5, self.C5, self.F5, self.bG5, self.G5, self.bC6, self.C6])
# self.F5.addNext([self.F4, self.bG4, self.G4, self.bC5, self.C5, self.bE5, self.bG5, self.G5, self.bC6, self.C6])
# self.bG5.addNext([self.bG4, self.G4, self.bC5, self.C5, self.bE5, self.F5, self.G5, self.bC6, self.C6])
# self.G5.addNext([self.G4, self.bC5, self.C5, self.bE5, self.F5, self.bG5, self.bC6, self.C6])
# self.bC6.addNext([self.bC5, self.C5, self.bE5, self.F5, self.bG5, self.G5, self.C6])
# self.C6.addNext([self.C5, self.bE5, self.F5, self.bG5, self.G5, self.bC5])

    def rhythm1(self, i, note):
        if i%8 == 0:
            time.sleep(EIGHTHNOTE)
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            note.getNext()
            note = note.getNext()
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            note.getNext()
            note = note.getNext()
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            note.getNext()
            note = note.getNext()
            
        elif i%8 == 1:
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            note.getNext()
            note = note.getNext()
            note.play()
            time.sleep(EIGHTHNOTE + QUARNOTE)
            note.stop()
            note.getNext()
            note = note.getNext()
                   
        elif i%8 == 2:
            time.sleep(EIGHTHNOTE)
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            note.getNext()
            note = note.getNext()
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            note.getNext()
            note = note.getNext()
            
        elif i%8 == 3:
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            note.getNext()
            note = note.getNext()
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            note.getNext()
            note = note.getNext()
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            note.getNext()
            note = note.getNext()
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            note.getNext()  
            note = note.getNext()
        elif i%8 == 4:
            note.play()
            time.sleep(QUARNOTE*2)
            note.getNext()
            note = note.getNext()
        elif i%8 == 5:
            time.sleep(QUARNOTE)
            note.stop()
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            note.getNext()
            note = note.getNext()
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            note.getNext()
            note = note.getNext()
             
        elif i%8 == 6 :
            note.play()
            time.sleep(HALFNOTE)
            note.getNext()
            note = note.getNext()
            
        elif i%8 == 7:
            time.sleep(HALFNOTE)
            note.stop()
    
    def rhythm2(self, i, note): 
        if  i%8 == 0:
            note.play()
            time.sleep(QUARNOTE)
            note.stop()
            
            note = note.getNext()
            
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            
            note = note.getNext()
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop
        elif i%8 == 1:
            time.sleep(EIGHTHNOTE)
            note.play()
            time.sleep(QUARNOTE)
            note.stop()
            
            note = note.getNext()
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            
            note = note.getNext()
            
        elif i%8 == 2:
            time.sleep(EIGHTHNOTE)
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            
            note = note.getNext()
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            note = note.getNext()
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            note = note.getNext()
        elif i%8 == 3:
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            note = note.getNext()
            note.play()
            time.sleep(SIXTEENTHNOTE)
            note.stop()
            note = note.getNext()
            note.play()
            time.sleep(SIXTEENTHNOTE)
            note.stop()
            note = note.getNext()
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            note = note.getNext()
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            
        elif i%8 == 4:
            note.play()
            time.sleep(QUARNOTE)
            note.stop()
            
            note = note.getNext()
            
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            
            note = note.getNext()
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop
            
        elif i%8 == 5:
            time.sleep(EIGHTHNOTE)
            note.play()
            time.sleep(QUARNOTE)
            note.stop()
            
            note = note.getNext()
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            
            note = note.getNext()
            
        elif i%8 == 6:
    
            time.sleep(EIGHTHNOTE)
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            
            note = note.getNext()
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            note = note.getNext()
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            note = note.getNext()
            
        elif i%8 == 7:
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            note = note.getNext()
            note.play()
            time.sleep(SIXTEENTHNOTE)
            note.stop()
            note = note.getNext()
            note.play()
            time.sleep(SIXTEENTHNOTE)
            note.stop()
            note = note.getNext()
            note.play()
            time.sleep(SIXTEENTHNOTE)
            note.stop()
            note = note.getNext()
            note.play()
            time.sleep(SIXTEENTHNOTE)
            note.stop()
            note = note.getNext()
            note.play()
            time.sleep(EIGHTHNOTE)
            note.stop()
            
if __name__ == '__main__':
    new_gen = Music_Generator()
    new_gen.start_the_music()
    
#         loops = []
#         for s in range(4):
#             note = note.getNext()
#             loops.append(note)
#          
#         for d in range(4):
#             loops[d].play()
#             time.sleep(EIGHTHNOTE)
#             loops[d].stop()
#               
#     else:
#         note.play()
#         time.sleep(QUARNOTE)
    