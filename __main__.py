import sys
import pygame
from PIL import Image
import os
pygame.init()

class gameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    def move(self, up = False, down = False, left = False, right = False):
        self.pos = self.pos.move(0, self.speed)

screen = pygame.display.set_mode((1280, 720)) #Creates the screen
clock = pygame.time.Clock()            #get a pygame clock object
playerImg = pygame.image.load('fabioSprite.png').convert() #opens and converts the image
background = pygame.image.load('ResizedGameMenu.png').convert() #Opens and converts the image
screen.blit(background, (0, 0)) #Creates the background
objects = [] #The object list
                    #create 10 objects
player = gameObject(playerImg, 1, 1) #Creates the player object
while True: #Main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(background, player.pos, player.pos)
    player.move()
    screen.blit(player.image, player.pos)
    pygame.display.update()
    clock.tick(60)