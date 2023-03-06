import sys
import pygame
from PIL import Image
import os
pygame.init()
WIDTH = 1280
HEIGHT = 720
class playerObject: #Creates the player controllable object
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    def move(self, up = False, down = False, left = False, right = False):
        if right:
            self.pos.right += self.speed
        if left:
            self.pos.right -= self.speed
        if down:
            self.pos.top += self.speed
        if up:
            self.pos.top -= self.speed
        if self.pos.right > WIDTH:
            self.pos.left = 0
        if self.pos.top > HEIGHT-SPRITE_HEIGHT:
            self.pos.top = 0
        if self.pos.right < SPRITE_WIDTH:
            self.pos.right = WIDTH
        if self.pos.top < 0:
            self.pos.top = HEIGHT-SPRITE_HEIGHT
    def animate(self):
        
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
playerImgPG = pygame.image.load('loogeySprite.png').convert_alpha() #opens and converts the image
playerImgPil = Image.open('loogeySprite.png')
SPRITE_HEIGHT = playerImgPil.height
SPRITE_WIDTH = playerImgPil.width
background = pygame.image.load('ResizedGameMenu.png').convert() #Opens and converts the image
screen.blit(background, (0, 0)) #Creates the background
objects = []            #Object list
props = []              #The props list
player = playerObject(playerImgPG, 0, 5) #Creates the player object
rectangle = gameObjectStatic((3, 3, 3), WIDTH, 60, 0, 660)
while True: #Main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(background, player.pos, player.pos)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.move(up=True)
    if keys[pygame.K_DOWN]:
        player.move(down=True)
    if keys[pygame.K_LEFT]:
        player.move(left=True)
    if keys[pygame.K_RIGHT]:
        player.move(right=True)
    rectangle.draw()
    screen.blit(player.image, player.pos)
    pygame.display.update()
    clock.tick(60)