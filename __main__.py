import sys
import pygame
from PIL import Image
import os
pygame.init()

class playerObject: #Creates the player 
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    def move(self, up = False, down = False, left = False, right = False):
        self.pos = self.pos.move(0, self.speed)

class gameObjectStatic:
    def __init__(self, color, width, height, posX, posY):
        self.color = color
        self.width = width
        self.height = height
        self.posX = posX
        self.posY = posY
        
    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.posX, self.posY, self.width, self.height))
    

screen = pygame.display.set_mode((1280, 720)) #Creates the screen
clock = pygame.time.Clock()                   #get a pygame clock object
playerImg = pygame.image.load('fabioSprite.png').convert() #opens and converts the image
background = pygame.image.load('ResizedGameMenu.png').convert() #Opens and converts the image
screen.blit(background, (0, 0)) #Creates the background
objects = []            #
props = []              #The props list
player = playerObject(playerImg, 0, 5) #Creates the player object
rectangle = gameObjectStatic((3, 3, 3), 40, 60, 50, 50)
while True: #Main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(background, player.pos, player.pos)
    player.move()
    rectangle.draw()
    screen.blit(player.image, player.pos)
    pygame.display.update()
    clock.tick(60)