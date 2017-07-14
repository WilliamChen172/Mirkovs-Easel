'''
Created on Jul 13, 2015

@author: Burned Orphans
'''

import pygame

white = [255, 255, 255]
black = [0, 0, 0]
red = [255,0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
peach_puff = [255, 218, 185]


class Game:
    background_color = peach_puff
    def __init__(self):
        self.screen_size = [700, 700]
        self.screen = pygame.display.set_mode(self.screen_size)
        self.player = Player([500, 0], self.screen)
        self.barrier1 = Barrier([100, 100], self.screen)
        self.barrier2 = Barrier([440, 440], self.screen)
        self.game_running = True
        self.clock = pygame.time.Clock()
        self.barriers = [self.barrier1, self.barrier2]
        
    def check_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:           
                    self.player.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    self.player.moving_right = True
                elif event.key == pygame.K_UP:
                    self.player.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.player.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:           
                    self.player.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    self.player.moving_right = False
                elif event.key == pygame.K_UP:
                    self.player.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.player.moving_down = False

    def main(self):
        while self.game_running:
            self.clock.tick(30)
            self.screen.fill(self.background_color)
            self.player.draw()
            self.barrier1.draw()
            self.barrier2.draw()
            self.check_input()
            self.player.update()
            self.barrier1.update()
            self.barrier2.update()
            self.player.check_for_collisions_with(self.barriers)
            pygame.display.update()
        
class Player:
    def __init__(self, position, screen):
        self.position = position
        self.width = 30
        self.speed = 10
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down= False
        self.surface = pygame.image.load('crouton.png')
        self.screen = screen
        self.rect = self.surface.get_rect()
        
    def move_left(self):
        self.position[0] -= self.speed
    
    def move_right(self):
        self.position[0] += self.speed
    
    def move_up(self):
        self.position[1] -= self.speed
    
    def move_down(self):
        self.position[1] += self.speed
    
    def update(self):
        if self.moving_left:
            self.move_left()
        if self.moving_right:
            self.move_right()
        if self.moving_up:
            self.move_up()
        if self.moving_down:
            self.move_down()
            
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
    
    def draw(self):
        self.screen.blit(self.surface, self.position)
        
    def check_for_collisions_with(self, list_of_objects):
        for obj in list_of_objects:
            if self.rect.colliderect(obj.rect):
                print ("Collision y[e]")
                print (self.rect.x, self.rect.y)
                print (obj.rect.x, obj.rect.y)

class Barrier:
    def __init__(self, position, screen):
        self.position = position
        self.screen = screen
        self.width = 60
        self.color = black
        self.surface = pygame.image.load('salad.png')
        self.rect = self.surface.get_rect()
    
    def update(self):
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]

    
    def draw(self):
        self.screen.blit(self.surface, self.position)
        
game = Game()
game.main()